from dotenv import load_dotenv
from openai import OpenAI
from os import getenv
from .ai_thread import AiThread
from .workflow_manager import WorkflowManager
from .workflows.software_development import software_development_phases
from chatdev.adapters import OpenAIAdapter, AnthropicAdapter
from chatdev.entities import Thread, Message
from anthropic import Anthropic
from .adapter_factory import AdapterFactory

def main():
  load_dotenv(".env")
  load_dotenv(".env.local", override=True)

  factory = AdapterFactory(
     openai_client= OpenAI(),
     anthropic_client= Anthropic()
  )


  model = "claude-3-opus-20240229"
#   model = "gpt-4-1106-preview"

  adapter = factory.adapter(model)

  thread = Thread(
     messages= [
        Message(role= "user", content= "Who are you?"),
     ]
  )

  message = adapter.generate(thread)
  print(message.content)

#   workflow_manager = WorkflowManager(
#      oai_client= oai_client,
#      model= oai_model,
#      assistant_id= oai_assistant_id,
#      description= "",
#      phases= software_development_phases
#   )

#   workflow_manager.execute(input("What do you want to develop today?: "))

if __name__ == '__main__':
    main()
