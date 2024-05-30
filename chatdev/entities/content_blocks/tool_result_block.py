"""
This module defines the `ToolResultBlock` class which represents a block of tool result content in a message.

Modules Imported:
- `ContentBlock` from `.content_block`: Represents a generic content block in a message.
- `Any` from `typing`: Specifies any type for the output.

Classes:
- `ToolResultBlock`: Represents a block of tool result content in the workflow messages.

`ToolResultBlock` Class:
Attributes:
- `id` (str): The identifier for the tool result block.
- `output` (Any): The output of the tool result.
- `error` (bool): Indicates whether the tool result contains an error (default is `False`).

Methods:
- `__init__(self, id: str, output: Any, error: bool = False)`: Initializes a ToolResultBlock with the specified id, output, and error status.
- `__str__(self)`: Returns a string representation of the tool result block.
- `dict(self) -> dict`: Returns the dictionary representation of the tool result block.
"""

from .content_block import ContentBlock
from typing import Any

class ToolResultBlock(ContentBlock):
  id: str
  output: Any
  error: bool

  def __init__(self, id: str, output: Any, error: bool = False):
    super().__init__(type= "tool_result")

    self.id = id
    self.output = output
    self.error = error

  def __str__(self):
    return f"ToolResultBlock(id= {self.id}, output= {self.output})"

  def dict(self) -> dict:
    return {
      "id": self.id,
      "output": self.output
    }
