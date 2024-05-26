from dotenv import load_dotenv
from openai import OpenAI
from anthropic import Anthropic
from chatdev import WorkflowManager
from chatdev.adapters import AdapterFactory
from chatdev.workflows import medium_software_development_workflow

def main():
  load_dotenv(".env")
  load_dotenv(".env.local", override=True)

  factory = AdapterFactory(
    openai_client= OpenAI(),
    anthropic_client= Anthropic()
  )

  workflow_manager = WorkflowManager(
    adapter_factory= factory
  )

  workflow_manager.execute(
    workflow= medium_software_development_workflow,
    input= "Take a look at your workspace project and improve it, modernize it and make it a nice, elegant, well-documented and efficient software.", # input("What do you want to develop today?: ")
    workspace_path= "workspaces/hello-ai"
  )

if __name__ == '__main__':
   main()
