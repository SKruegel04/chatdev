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
