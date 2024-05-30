"""
This module defines the `Message` class representing a message exchanged in the workflow.

Modules Imported:
- `List`, `Optional` from `typing`: Specifies list and optional types.
- `ContentBlock` from `.content_blocks.content_block`: Represents a generic content block in a message.
- `TextBlock` from `.content_blocks.text_block`: Represents a block of text content in a message.
- `ToolUseBlock` from `.content_blocks.tool_use_block`: Represents a block of tool use content in a message.
- `ToolResultBlock` from `.content_blocks.tool_result_block`: Represents a block of tool result content in a message.

Classes:
- `Message`: Represents a message in the workflow.

`Message` Class:
Attributes:
- `role` (str): The role responsible for the message.
- `content` (List[ContentBlock]): List of content blocks associated with the message.

Methods:
- `__init__(self, role: str, content: List[ContentBlock])`: Initializes a Message with role and content blocks.
- `text_blocks(self) -> List[TextBlock]`: Returns a list of text blocks in the message.
- `first_text_block(self) -> Optional[TextBlock]`: Returns the first text block in the message, if any.
- `tool_use_blocks(self) -> List[ToolUseBlock]`: Returns a list of tool use blocks in the message.
- `tool_result_blocks(self) -> List[ToolResultBlock]`: Returns a list of tool result blocks in the message.
- `__str__(self)`: Returns a string representation of the message.
- `dict(self) -> dict`: Returns a dictionary representation of the message.
"""

from typing import List, Optional
from .content_blocks.content_block import ContentBlock
from .content_blocks.text_block import TextBlock
from .content_blocks.tool_use_block import ToolUseBlock
from .content_blocks.tool_result_block import ToolResultBlock

class Message:
  role: str
  content: List[ContentBlock]

  def __init__(self, role: str, content: List[ContentBlock]):
    self.role = role
    self.content = content

  def text_blocks(self) -> List[TextBlock]:
    return [block for block in self.content if isinstance(block, TextBlock)]
  
  def first_text_block(self) -> Optional[TextBlock]:
    for block in self.content:
      if isinstance(block, TextBlock):
        return block
    return None
  
  def tool_use_blocks(self) -> List[ToolUseBlock]:
    return [block for block in self.content if isinstance(block, ToolUseBlock)]

  def tool_result_blocks(self) -> List[ToolResultBlock]:
    return [block for block in self.content if isinstance(block, ToolResultBlock)]

  def __str__(self):
    content_str = ", ".join([block.__str__() for block in self.content])
    return f"Message(role= {self.role}, content= {content_str})"

  def dict(self) -> dict:
    return {
      "role": self.role,
      "content": [block.dict() for block in self.content]
    }
