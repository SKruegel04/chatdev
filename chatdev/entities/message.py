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
