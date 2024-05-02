from openai import OpenAI
from openai.types.beta.thread import Thread
from typing import Optional
from time import sleep

class AiThread:
  """
  An AiThread represents a thread in the OpenAI API.

  We can send messages to it and receive the response to that message.
  """

  def __init__(self, oai_client: OpenAI, model: str, assistant_id: str, instructions: str, initial_message: str):
    """
    Creates a new AiThread with the given OpenAI client, model, assistant ID, instructions, and initial message.
    """
    self.oai_client = oai_client
    self.model = model
    self.assistant_id = assistant_id
    self.instructions = instructions
    self.initial_message = initial_message
    self.current_thread: Optional[Thread] = None
    self.last_message_id: Optional[str] = None

  def thread(self) -> Thread:
    """
    Returns the current OpenAI thread.
    """
    if self.current_thread is None:
      self.current_thread = self.oai_client.beta.threads.create(
        messages= [{
          "role": "user",
          "content": self.initial_message
        }]
      )

    return self.current_thread
  
  def send(self, content: str) -> str:
    """
    Sends a message to the thread and returns the response.
    """
    message = self.oai_client.beta.threads.messages.create(
      thread_id= self.thread().id,
      role= "user",
      content= content,
    )

    run = self.oai_client.beta.threads.runs.create(
      thread_id= self.thread().id,
      model= self.model,
      assistant_id= self.assistant_id,
      instructions= self.instructions,
    )

    while run.status == 'queued' or run.status == 'in_progress' or run.status == 'requires_action':
      run = self.oai_client.beta.threads.runs.retrieve(run_id= run.id, thread_id= self.thread().id)
      if run.status != 'queued' and run.status != 'in_progress' and run.status != 'requires_action':
        break

      sleep(5)

    new_messages = self.oai_client.beta.threads.messages.list(
      thread_id= self.thread().id,
      limit= 1,
      before= message.id,
    )

    if len(new_messages.data) == 0:
      raise RuntimeError(f"No new messages found in thread {self.thread().id}")
    
    return new_messages.data[0].content[0].text.value
  
  def destroy(self):
    """
    Destroys the thread.
    """
    if self.current_thread is None:
      return
    
    self.oai_client.beta.threads.delete(thread_id= self.current_thread.id)
