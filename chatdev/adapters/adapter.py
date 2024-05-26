from typing import List
from chatdev.entities import Thread, Tool, Message, ToolUseBlock, ToolResultBlock
from os import makedirs, path, walk
from json import dumps
from re import Pattern, compile
from subprocess import run
from traceback import format_exception
from requests import request

class Adapter:

  read_file_tool: Tool = Tool(
     name= "read_file",
     description= "allows you to read files and shall be used anytime something similar to reading a file should be achieved. It returns the full content of the file.",
     input_schema= {
      "type": "object",
      "properties": {
        "file_path": {
          "type": "string",
          "description": "path to the file that should be read"
        }
      },
      "required": ["file_path"]
    }
  )

  write_file_tool: Tool = Tool(
    name= "write_file",
    description= "allows you to write files and shall be used anytime something similar to writing a file should be achieved. It returns an empty string.",
    input_schema= {
      "type": "object",
      "properties": {
        "file_path": {
          "type": "string",
          "description": "path to the file that should be written"
        },
        "content": {
          "type": "string",
          "description": "content to write into the file"
        }
      },
      "required": ["file_path", "content"]
    }
  )

  list_files_tool: Tool = Tool(
    name= "list_files",
    description= "allows you to list files and shall be used anytime something similar to listing a file should be achieved. It returns an formatted list of file paths. Always use the first parameter and ignore files like node_modules, .git and similar ones you can think of.",
    input_schema= {
      "type": "object",
      "properties": {
        "ignore_patterns": {
          "type": "array",
          "description": "an array of regular expressions in the format \"/<pattern>/<modifiers>\" that will be matched against the full path of every file. Use it to ignore files you don´t need to look at, e.g. dependency/library and output folders of code projects.",
          "items": {
            "type": "string"
          }
        },
      },
      "required": ["ignore_pattern"]
    }
  )

  docker_tool: Tool = Tool(
    name= "docker",
    description= "Allows you to set up development and execution environments for any kind of content, e.g. programming languages, latex etc. You can test, execute, build and deploy with it. Also create compose.yml files that describe your docker setup and make it reproducible. Always use relative paths for mounts, don't use shell-specific arguments like $(pwd). Your workspace is directly in your project folder (./), mount from there, i.e. \"./:/app\"",
    input_schema= {
      "type": "object",
      "properties": {
        "arguments": {
          "type": "array",
          "description": "the arguments of the docker command to run, e.g. [\"run\", \"-p\", \"8080:8080\", \"-v\", \".:/app\", \"node\", \"index.js\"].",
          "items": {
            "type": "string"
          }
        },
      },
      "required": ["arguments"]
    }
  )

  request_tool: Tool = Tool(
    name= "request",
    description= "Allows you to send HTTP requests to anywhere. You can grab any HTTP resource and construct dynamic requests to get additional content, test HTTP endpoints, request APIs, use search engines, fill out forms etc.",
    input_schema= {
      "type": "object",
      "properties": {
        "method": {
          "type": "string",
          "enum": ["GET", "POST", "PATCH", "PUT", "DELETE", "OPTION", "HEAD", "TRACE"],
          "default": "GET"
        },
        "url": {
          "type": "string",
          "description": "The URL to request."
        },
        "headers": {
          "type": "object",
          "additionalProperties": {
            "type": "string"
          }
        },
        "body": {
          "type": "string"
        }
      },
      "required": ["url"]
    }
  )

  tools: List[Tool] = [
    read_file_tool,
    write_file_tool,
    list_files_tool,
    docker_tool,
    request_tool
  ]

  def generate_llm_response(self, thread: Thread) -> None:
    pass

  def generate_response(self, thread: Thread) -> None: 
    self.generate_llm_response(thread)
    self.dump_thread(thread)
    self.execute_tools(thread)

  def dump_thread(self, thread: Thread) -> None:
    dump_path = f"{thread.workspace_path}/.chatdev-thread.json"
    makedirs(path.dirname(dump_path), exist_ok= True)
    with open(dump_path, 'w') as file:
      file.write(dumps(thread.dict(), indent= 2))

  def execute_tools(self, thread: Thread) -> None:
    while True:
      tool_use_blocks = thread.last_message_tool_use_blocks()
      if len(tool_use_blocks) == 0:
        break

      tool_result_blocks = [self.safe_execute_tool(thread, block) for block in tool_use_blocks]

      if len(tool_result_blocks) > 0:
        thread.append_message(
          Message(
            role= "user",
            content= tool_result_blocks
          )
        )
        self.generate_response(thread)

  def safe_execute_tool(self, thread: Thread, block: ToolUseBlock) -> ToolResultBlock:
    try:
      return self.execute_tool(thread, block)
    except Exception as e:
      error_string = ''.join(format_exception(type(e), value=e, tb= e.__traceback__))
      return ToolResultBlock(
        id= block.id,
        output= error_string,
        error= True
      )

  def execute_tool(self, thread: Thread, block: ToolUseBlock) -> ToolResultBlock:
    if block.name == "read_file":
      input_file_path = block.input["file_path"]
      workspace_file_path = f"{thread.workspace_path}/{input_file_path}"
      with open(workspace_file_path, 'r') as file:
        content = file.read()
        return ToolResultBlock(
          id= block.id,
          output= content
        )
    elif block.name == "write_file":
      input_file_path = block.input["file_path"]
      workspace_file_path = f"{thread.workspace_path}/{input_file_path}"
      input_content = block.input["content"]
      makedirs(path.dirname(workspace_file_path), exist_ok= True)
      with open(workspace_file_path, 'w') as file:
        content = file.write(input_content)
        return ToolResultBlock(
          id= block.id,
          output= ""
        )
    elif block.name == "list_files":
      ignore_patterns = [compile(pattern) for pattern in block.input["ignore_patterns"]]
      files_list = self.list_files_recursive(thread.workspace_path, ignore_patterns)
      return ToolResultBlock(
        id= block.id,
        output= "\n".join(files_list)
      )
    elif block.name == "docker":
      arguments = block.input["arguments"]
      result = run(["docker"] + arguments, capture_output= True, text= True, cwd= thread.workspace_path)
      if not result.returncode == 0:
        raise ChildProcessError(f"Docker tool failed: {result.stderr}")
      return ToolResultBlock(
        id= block.id,
        output= result.stdout
      )
    elif block.name == "request":
      method = block.input.get("method", "GET")
      url = block.input["url"]
      headers = block.input.get("headers", {})
      body = block.input.get("body", None)

      response = request(method, url, headers=headers, data=body)
      
      return ToolResultBlock(
        id= block.id,
        output= response.text if response.ok else f"Request failed: {response.status_code} {response.reason}",
        error= not response.ok
      )
    else:
      raise ValueError(f"Invalid tool name {block.name}!")

  def list_files_recursive(self, base_path: str, ignore_patterns: List[Pattern]) -> List[str]:
    files_list = []
    for root, dirs, files in walk(base_path):
      for file in files:
        file_path = path.join(root, file).removeprefix(base_path).removeprefix("/")
        if not any(pattern.search(file_path) for pattern in ignore_patterns):
          files_list.append(file_path)
    return files_list
