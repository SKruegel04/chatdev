from chatdev.entities import Message, Thread, TextBlock, ToolUseBlock
from .adapter import Adapter
from openai import OpenAI
from typing import List
from itertools import chain
from json import dumps, loads

class OpenAIAdapter(Adapter):
  client: OpenAI
  model: str

  def __init__(self, client: OpenAI, model: str):
    super().__init__()

    self.client = client
    self.model = model

  def generate_llm_response(self, thread: Thread) -> None:

    response= self.client.chat.completions.create(
      model= self.model,
      messages= list(chain.from_iterable([self.split_messages(message) for message in thread.messages])),
      tools= [{
        "type": "function",
        "function": {
          "name": tool.name,
          "description": tool.description,
          "parameters": tool.input_schema
        }
      } for tool in self.tools]
    )

    choice = response.choices[0]
    text_blocks = [TextBlock(choice.message.content)] if not choice.message.content is None else []
    tool_use_blocks = [ToolUseBlock(id= call.id, name= call.function.name, input= loads(call.function.arguments)) for call in choice.message.tool_calls] if not choice.message.tool_calls is None else []
    message = Message(
      role= "assistant",
      content= text_blocks + tool_use_blocks,
    )
    thread.append_message(message)

  def split_messages(self, message: Message) -> List[Message]:

    text_parts = [{ "type": "text", "text": block.text} for block in message.text_blocks()]

    tool_calls = [{
      "id": block.id,
      "type": "function",
      "function": {
        "name": block.name,
        "arguments": dumps(block.input)
      }
    } for block in message.tool_use_blocks()]

    text_part_string = '\n'.join([block["text"] for block in text_parts])

    text_message = { "role": "user", "content": text_parts } if message.role == "user" else self.del_none({
      "role": "assistant",
      "content": None if text_part_string == "" else text_part_string,
      "tool_calls": tool_calls if len(tool_calls) > 0 else None
    })

    tool_messages = [{
      "role": "tool",
      "tool_call_id": block.id,
      "content": dumps(
        { "type": "success", "content": block.output } if not block.error else { "type": "error", "content": block.output }
      )
    } for block in message.tool_result_blocks()]

    if len(text_parts) == 0 and len(tool_calls) == 0:
      return tool_messages
    
    return [text_message] + tool_messages
    
  def del_none(self, d):
    """
    Delete keys with the value ``None`` in a dictionary, recursively.

    This alters the input so you may wish to ``copy`` the dict first.
    """
    for key, value in list(d.items()):
        if value is None:
            del d[key]
        elif isinstance(value, dict):
            self.del_none(value)
    return d