"""
This module defines the `AnthropicAdapter` class which interacts with Anthropic AI models.

Modules Imported:
- `Message`, `Thread`, `Tool`, `ContentBlock`, `TextBlock`, `ToolResultBlock`, `ToolUseBlock` from `chatdev.entities`: Represents various components of workflows and tool interactions.
- `Adapter` from `.adapter`: Represents the generic adapter interface.
- `Anthropic` from `anthropic`: Initializes the Anthropic client.

Classes:
- `AnthropicAdapter`: Manages interactions with Anthropic AI models.

`AnthropicAdapter` Class:
Attributes:
- `client` (Anthropic): The Anthropic client.
- `model` (str): The model identifier for the Anthropic AI.

Methods:
- `__init__(self, client: Anthropic, model: str)`: Initializes the AnthropicAdapter with the specified client and model.
- `generate_llm_response(self, thread: Thread) -> None`: Generates a response from the Anthropic model based on the provided thread.
- `tool_to_dict(self, tool: Tool) -> dict`: Converts a Tool object to a dictionary representation.
- `message_to_dict(self, message: Message) -> dict`: Converts a Message object to a dictionary representation.
- `dict_to_message(self, message: dict) -> Message`: Converts a dictionary to a Message object.
- `content_block_to_dict(self, block: ContentBlock) -> dict`: Converts a ContentBlock object to a dictionary representation.
- `dict_to_content_block(self, block: dict) -> ContentBlock`: Converts a dictionary to a ContentBlock object.
"""

from chatdev.entities import Message, Thread, Tool, ContentBlock, TextBlock, ToolResultBlock, ToolUseBlock
from .adapter import Adapter
from anthropic import Anthropic

class AnthropicAdapter(Adapter):
  client: Anthropic
  model: str

  def __init__(self, client: Anthropic, model: str):
    super().__init__()

    self.client = client
    self.model = model

  def generate_llm_response(self, thread: Thread) -> None:
    response = self.client.beta.tools.messages.create(
      model= self.model,
      max_tokens= 1000,
      messages= [self.message_to_dict(message= message) for message in thread.messages],
      tools= [self.tool_to_dict(tool= tool) for tool in self.tools]
    )

    message = self.dict_to_message(response)
    thread.append_message(message)
  
  def tool_to_dict(self, tool: Tool) -> dict:
    return {
      "name": tool.name,
      "description": tool.description,
      "input_schema": tool.input_schema
    }

  def message_to_dict(self, message: Message) -> dict:
    return {
      "role": message.role,
      "content": [self.content_block_to_dict(block) for block in message.content]
    }
  
  def dict_to_message(self, message: dict) -> Message:
    return Message(
      role= message.role,
      content= [self.dict_to_content_block(block) for block in message.content]
    )
  
  def content_block_to_dict(self, block: ContentBlock) -> dict:
    if isinstance(block, TextBlock):
      return {
        "type": "text",
        "text": block.text
      }
    elif isinstance(block, ToolUseBlock):
      return {
        "type": "tool_use",
        "id": block.id,
        "name": block.name,
        "input": block.input
      }
    elif isinstance(block, ToolResultBlock):
      return {
        "type": "tool_result",
        "tool_use_id": block.id,
        "content": block.output,
        "is_error": block.error
      }
    else: 
      raise ValueError("Value is not a known content block")
    
  def dict_to_content_block(self, block: dict) -> ContentBlock:
    if block.type == "text":
      return TextBlock(
        text = block.text
      )
    elif block.type == "tool_use": 
      return ToolUseBlock(
        id= block.id,
        name= block.name,
        input= block.input
      )
    elif block.type == "tool_result": 
      return ToolResultBlock(
        id= block.id,
        output= block.content
      )
