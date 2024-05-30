"""
This module contains the WorkflowManager class responsible for executing AI workflows.

Modules Imported:
- `Thread`, `Workflow` from `chatdev.entities`: Represents workflows and their thread execution.
- `AdapterFactory` from `chatdev.adapters`: Manages adapter initialization.
- `generate` from `nanoid`: Generates unique IDs for workflows.
- `Optional` from `typing`: Specifies optional types.

Classes:
- `WorkflowManager`: Manages and executes AI workflows.

`WorkflowManager` Class:
Attributes:
- `adapter_factory` (AdapterFactory): The factory to create specific adapters for tools.

Methods:
- `__init__(self, adapter_factory: AdapterFactory)`: Initializes the WorkflowManager with the adapter factory.
- `execute(self, workflow: Workflow, input: str, workspace_path: Optional[str])`: Executes the provided workflow with specified input and workspace path.

The class further provides methods to manage different phases and conversations within the workflow and handle tool commands.
"""

from chatdev.entities import Thread, Workflow
from chatdev.adapters import AdapterFactory
from nanoid import generate
from typing import Optional

class WorkflowManager:
  """
  A WorkflowManager executes an AI workflow.

  It keeps track of the current phase and conversation and provides methods to move to the next one.
  """

  adapter_factory: AdapterFactory

  def __init__(self, adapter_factory: AdapterFactory):
    """
    Creates a new WorkflowManager with the given OpenAI client, model, assistant ID, description, and phases.
    """
    self.adapter_factory = adapter_factory

  def execute(self, workflow: Workflow, input: str, workspace_path: Optional[str]) -> Thread:
    """
    Executes the workflow with the given input.
    """
    id = generate(size=10)
    thread_workspace_path = workspace_path if not workspace_path is None else f"workspaces/{id}"
    thread = Thread(workspace_path=thread_workspace_path, messages=[])

    model = workflow.current_phase().current_conversation().lead.model
    adapter = self.adapter_factory.adapter(model)

    eol = '\n'
    instructions = f'''
      You are roleplaying a multiple people in a workflow, e.g. a company working on things in a process.
      In each response you always only represent a single person.
      The roleplay is structured in phases and each phase has a conversation.
      Each conversation always has a lead and an assistant role you are to impersonate.
      Each conversation has an input type and an output type you will try to create.
      Use all existing inputs and outputs created to properly create the respective output.

      If requirements or input by the human are unclear, make it up by yourself.

      Your main target is to use the tools given to achieve the respective output.
      You will read and write files to create and further enhance outputs.
      Each output artifact might create one or more new files or modify existing ones.

      In my initial message I will provide instructions that are to be handled by the workflow based on the input of the conversation.
      I provide you with descriptions of the conversations and the phases they belong to so that you know what to do.
  
      When I say "START PHASE <Phase Name>" you will realize you are now in the named phase of the workflow.
      You will respect what the phase is about, what the participating roles are and what the result should be.
      If you understood everything in that phase say only "SUCCESS", if not say only "FAILURE"

      When I say "START CONVERSATION <Conversation Name>" you will impersonate the lead of the conversation.
      You will read the existing thread and everything in it carefully.
      You will find an input per description. You answer to the provided assistant in respect to the roles and inputs described.

      When I say "SWITCH" you will impersonate the assistant, read the whole thread and answer to the lead.

      When I say "SWITCH" again you will impersonate the lead, read the whole thread again and answer to the assistant.

      Each impersonation can explain things or ask questions.
      If you feel like you are done, your message will only contain the conversation's desired
      output and end with "END CONVERSATION". But don't end it just because you can, your target is
      to create quality outputs.

      Always start your responses with the name of the role, e.g.:

      ```
      CEO:

      <the message>
      ```

      ```
      CPO:

      <the message>
      ```
      
      These are the roles you are to impersonate:
      {eol.join([role.gpt_str() for role in workflow.roles()])}

      These are the artifacts that are referenced as inputs and outputs in conversations:
      {eol.join([artifact.gpt_str() for artifact in workflow.artifacts()])}

      These are the conversations you are to hold. They are referenced in phases:
      {eol.join([conversation.gpt_str() for conversation in workflow.conversations()])}

      These are the phases you are going through:
      {eol.join([phase.gpt_str() for phase in workflow.phases])}

      Here is a general description of the workflow for context:
      {workflow.description}

      This is the instruction you will handle with the workflow:
      ({input})

      Don't use tools when you respond with any of the commands like SUCCESS, FAILURE, START, SWITCH, END etc.
      Make sure that if you want to use tools, you first use the tools, wait for the response and only then answer with commands.

      Answer, this once, with only "SUCCESS" if you understood everything and with only "FAILURE" if you didn't.
    '''

    thread.append_text_message(instructions)

    adapter.generate_response(thread)

    if not thread.last_message_text().endswith("SUCCESS"):
      raise RuntimeError(f"Sanity check failed, response was '{thread.last_message_text()}'")

    while not workflow.ended():
      phase = workflow.current_phase()

      print(f"\n=== Phase {phase.name} ===\n")
      thread.append_text_message(f'''
        START PHASE {phase.name}
      ''')

      adapter.generate_response(thread)

      if not thread.last_message_text().endswith("SUCCESS"):
        raise RuntimeError(f"Failed start of phase {phase.name}, last message: {thread.last_message_text()}")
      
      while not workflow.phase_ended():
        conversation = workflow.current_conversation()
        print(f"\n=== Conversation {conversation.name} ===\n")

        thread.append_text_message(f'''
          START CONVERSATION {conversation.name}
        ''')

        adapter.generate_response(thread)

        print(f"{thread.last_message_text()}\n")
        print("=====\n")
      
        message_count = 0
        current_role = "assistant"
        while True:
          model = conversation.lead.model if current_role == "lead" else conversation.assistant.model
          adapter = self.adapter_factory.adapter(model)

          thread.append_text_message("SWITCH")
          adapter.generate_response(thread)

          last_message_text = thread.last_message_text()

          print(f"{last_message_text}\n")
          print("=====\n")

          if message_count >= 10 or "END CONVERSATION" in last_message_text:
            break

          message_count += 1
          current_role = "assistant" if current_role == "lead" else "lead"

        workflow.next_conversation()
      workflow.next_phase()
