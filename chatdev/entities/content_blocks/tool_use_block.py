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
    
