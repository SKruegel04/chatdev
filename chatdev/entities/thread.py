from typing import List
from . import Message


class Thread:

  def __init__(self, messages: List[Message]):
    self.messages = messages

