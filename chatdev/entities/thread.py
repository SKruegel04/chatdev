from typing import List, Optional
from .message import Message
from .tool import Tool
from .content_blocks.text_block import TextBlock
from .content_blocks.tool_use_block import ToolUseBlock

class Thread:
  workspace_path: str
  messages: List[Message]

  def __init__(self, workspace_path: str, messages: List[Message]):
    self.workspace_path = workspace_path
    self.messages = messages

  def append_message(self, message: Message):
    self.messages.append(message)

  def append_text_message(self, text: str):
    self.append_message(
      message= Message(role= "user", content= [
        TextBlock(text= text)
      ])
    )

  def last_message(self) -> Optional[Message]:
    return self.messages[-1] if self.messages else None
  
  def last_message_tool_use_blocks(self) -> List[ToolUseBlock]:
    message = self.last_message()
    if message is None:
      return []
    return message.tool_use_blocks()
  
  def last_message_text(self) -> Optional[str]:
    message = self.last_message()
    if message is None:
      return None
    text_block = message.first_text_block()
    if text_block is None:
      return None
    return text_block.text

  def __str__(self):
    message_str = ", ".join([message.__str__() for message in self.messages])
    return f"Thread(messages= {message_str})"
  
  def dict(self) -> dict:
    return {
      "workspace_path": self.workspace_path,
      "messages": [message.dict() for message in self.messages]
    }
