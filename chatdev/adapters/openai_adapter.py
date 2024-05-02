from chatdev.entities import Message
from chatdev.entities.thread import Thread
from ..adapter import Adapter
from openai import OpenAI

class OpenAIAdapter(Adapter):
  def __init__(self, client: OpenAI, model: str):
    super().__init__()

    self.client = client
    self.model = model

  def generate(self, thread: Thread) -> Message:
    response= self.client.chat.completions.create(
      model= self.model,
      messages= [message.dict() for message in thread.messages]
    )
    return Message(
      role= response.choices[0].message.role,
      content= response.choices[0].message.content,
    )
