"""
This module defines the `ToolUseBlock` class which represents a block of tool use content in a message.

Modules Imported:
- `ContentBlock` from `.content_block`: Represents a generic content block in a message.
- `Any` from `typing`: Specifies any type for the input.

Classes:
- `ToolUseBlock`: Represents a block of tool use content in the workflow messages.

`ToolUseBlock` Class:
Attributes:
- `id` (str): The identifier for the tool use block.
- `name` (str): The name of the tool used.
- `input` (Any): The input provided to the tool.

Methods:
- `__init__(self, id: str, name: str, input: Any)`: Initializes a ToolUseBlock with the specified id, name, and input.
- `__str__(self)`: Returns a string representation of the tool use block.
- `dict(self) -> dict`: Returns the dictionary representation of the tool use block.
"""

from .content_block import ContentBlock
from typing import Any

class ToolUseBlock(ContentBlock):
  id: str
  name: str
  input: Any

  def __init__(self, id: str, name: str, input: Any):
    super().__init__(type= "tool_use")

    self.id = id
    self.name = name
    self.input = input

  def __str__(self):
    return f"ToolUseBlock(id= {self.id}, name= {self.name}, input= {self.input})"

  def dict(self) -> dict:
    return {
      "id": self.id,
      "name": self.name,
      "input": self.input
    }
