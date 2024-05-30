"""
This script is the main entry point for the ChatDev application.

Modules Imported:
- `load_dotenv` from `dotenv`: Loads environment variables from .env files.
- `OpenAI` from `openai`: Initializes the OpenAI client.
- `Anthropic` from `anthropic`: Initializes the Anthropic client.
- Various components from the `chatdev` module: Initializes WorkflowManager, AdapterFactory, and workflows.

Main Function:
The `main` function is the main entry point for the application and performs the following tasks:
1. Loads environment variables from `.env` and `.env.local` files.
2. Initializes the `AdapterFactory` with OpenAI and Anthropic clients.
3. Creates a `WorkflowManager` instance with the adapter factory.
4. Executes the documentation workflow based on user input.

Usage:
```python
if __name__ == '__main__':
    main()
```

This condition ensures that the `main` function is called when the script is executed directly.
"""

from dotenv import load_dotenv
from openai import OpenAI
from anthropic import Anthropic
from chatdev import WorkflowManager
from chatdev.adapters import AdapterFactory
from chatdev.workflows import medium_software_development_workflow, documentation_workflow

def main():
    """
    The main entry point for the application.

    Loads environment variables, initializes the adapter factory and workflow manager,
    and executes the workflow based on user input.
    """
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
        input= input("What do you want to build?: "),
        workspace_path= None
    )

if __name__ == '__main__':
    main()
