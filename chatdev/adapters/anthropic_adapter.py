from chatdev.entities import Message
from chatdev.entities.thread import Thread
from ..adapter import Adapter
from anthropic import Anthropic
import json

class AnthropicAdapter(Adapter):
  def __init__(self, client: Anthropic, model: str):
    super().__init__()

    self.client = client
    self.model = model

  def generate(self, thread: Thread) -> Message:
    response = self.client.messages.create(
      model= self.model,
      max_tokens= 1000,
      messages= [message.dict() for message in thread.messages]
    )

    return Message(
      role= response.role,
      content= response.content[0].text,
    )
