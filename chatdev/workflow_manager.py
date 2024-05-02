from openai import OpenAI
from typing import List, Optional, Set
from chatdev.entities import WorkflowRole, WorkflowArtifact, WorkflowPhase, WorkflowConversation
from .ai_thread import AiThread

class WorkflowManager:
  """
  A WorkflowManager manages a workflow.

  It keeps track of the current phase and conversation and provides methods to move to the next one.
  """
  def __init__(self, oai_client: OpenAI, model: str, assistant_id: str, description: str, phases: List[WorkflowPhase]):
    """
    Creates a new WorkflowManager with the given OpenAI client, model, assistant ID, description, and phases.
    """
    self.oai_client = oai_client
    self.model = model
    self.assistant_id = assistant_id
    self.description = description
    self.phases = phases
    self.current_phase_index = 0
    self.last_message_id: Optional[str] = None

  def roles(self) -> Set[WorkflowRole]:
    """
    Returns a set of all roles involved in this workflow.
    """
    return {role for phase in self.phases for role in phase.roles()}

  def artifacts(self) -> Set[WorkflowArtifact]:
    """
    Returns a set of all artifacts involved in this workflow.
    """
    return {artifact for phase in self.phases for artifact in phase.artifacts()}

  def conversations(self) -> Set[WorkflowConversation]:
    """
    Returns a set of all conversations involved in this workflow.
    """
    return {conversation for phase in self.phases for conversation in phase.conversations}
  
  def current_phase(self) -> WorkflowPhase:
    """
    Returns the current phase in this workflow.
    """
    if self.ended():
      raise RuntimeError(f"Workflow already ended")
    return self.phases[self.current_phase_index]
  
  def next_phase(self):
    """
    Moves to the next phase in this workflow.
    """
    if self.ended():
      raise RuntimeError(f"Workflow ended")
    self.current_phase_index += 1
  
  def ended(self) -> bool:
    """
    Returns whether this workflow has ended.
    """
    return self.current_phase_index >= len(self.phases)
  
  def current_conversation(self) -> WorkflowConversation:
    """
    Returns the current conversation in this workflow.
    """
    return self.current_phase().current_conversation()

  def next_conversation(self):
    """
    Moves to the next conversation in this workflow.
    """
    self.current_phase().next_conversation()

  def phase_ended(self) -> bool:
    """
    Returns whether the current phase has ended.
    """
    return self.current_phase().ended()
  
  def execute(self, input: str):
    """
    Executes the workflow with the given input.
    """

    eol = '\n'
    instructions = '''
      You are roleplaying a multiple people in a workflow, e.g. a company working on things in a process.
      In each response you always only represent a single person.
      The roleplay is structured in phases and each phase has a conversation.
      Each conversation always has a lead and an assistant role you are to impersonate.
      Each conversation has an input type and an output type you will try to create.
      Use all existing inputs and outputs created to properly create the respective output.

      In my initial message I will provide instructions that are to be handled by the workflow based on the input of the conversation.
      I provide you with descriptions of the conversations and the phases they belong to so that you know what to do.
  
      When I say "START PHASE <Phase Name>" you will realize you are now in the named phase of the workflow.
      You will respect what the phase is about, what the participating roles are and what the result should be.
      If you understood everything in that phase say only "SUCCESS", if not say only "FAILURE"

      When I say "START CONVERSATION <Conversation Name>" you will impersonate the lead of the conversation.
      You will read the existing thread and everything it it carefully.
      You will find an input per description. You answer to the provided assistant in respect to the roles and inputs described.

      When I say "SWITCH" you will impersonate the assistant, read the whole thread and answer to the lead.

      When I say "SWITCH" again you will impersonate the lead, read the whole thread again and answer to the assistant.

      Each impersonation can explain things or ask questions.
      If you feel like you are done, your message will only contain the conversation's desired
      output and end with "END CONVERSATION".

      Always start your responses with the name of the role, e.g.:

      ```
      CEO:

      <the message>
      ```

      ```
      CPO:

      <the message>
      ```
    '''

    initial_message = f'''
      These are the roles you are to impersonate:
      {eol.join([role.gpt_str() for role in self.roles()])}

      These are the artifacts that are referenced as inputs and outputs in conversations:
      {eol.join([artifact.gpt_str() for artifact in self.artifacts()])}

      These are the conversations you are to hold. They are referenced in phases:
      {eol.join([conversation.gpt_str() for conversation in self.conversations()])}

      These are the phases you are going through:
      {eol.join([phase.gpt_str() for phase in self.phases])}

      Here is a general description of the workflow for context:
      {self.description}

      This is the instruction you will handle with the workflow:
      ({input})
    '''

    thread = AiThread(
      oai_client= self.oai_client,
      model= self.model,
      assistant_id= self.assistant_id,
      instructions= instructions,
      initial_message= initial_message,
    )

    # Sanity check
    response = thread.send('''
      Answer with only "SUCCESS" if you understood everything and with only "FAILURE" if you didn't."
    ''')

    if response != "SUCCESS":
      raise RuntimeError(f"Sanity check failed. Response: {response}")

    while not self.ended():
      phase = self.current_phase()

      print(f"\n=== Phase {phase.name} ===\n\n")
      last_response = thread.send(f'''
        START PHASE {phase.name}
      ''')
      if last_response != "SUCCESS":
        raise RuntimeError(f"Failed start of phase {phase.name}")

      while not self.phase_ended():
        conversation = self.current_conversation()
        print(f"\n=== Conversation {conversation.name} ===\n\n")
        last_response = thread.send(f'''
          START CONVERSATION {self.current_conversation().name}
        ''')
        print(f"{last_response}\n")
        print("=====\n")
      
        message_count = 0
        while message_count < 10 and "END CONVERSATION" not in last_response:
          last_response = thread.send("SWITCH")
          print(f"{last_response}\n")
          print("=====\n")
          message_count += 1

        self.next_conversation()
      self.next_phase()

    thread.destroy()

  def __str__(self) -> str:
    return f"WorkflowManager[{self.name}]"