from typing import List, Set
from . import WorkflowRole, WorkflowArtifact, WorkflowConversation

class WorkflowPhase:
  """
  A workflow phase describes a phase in a workflow, which consists of multiple conversations.

  Examples
  --------
  WorkflowPhase(
    "Code Review",
    "Code review between developer and CEO",
    [
      WorkflowConversation(
        "Code Review",
        "Code review between developer and CEO",
        WorkflowRole("Developer", "Developer working on the code"),
        WorkflowRole("CEO", "CEO of the company"),
        WorkflowArtifact("Code", "The code that was written"),
        WorkflowArtifact("Requirements", "Requirements for the code")
      ),
      WorkflowConversation(
        "Code Review",
        "Code review between developer and CEO",
        WorkflowRole("Developer", "Developer working on the code"),
        WorkflowRole("CEO", "CEO of the company"),
        WorkflowArtifact("Code", "The code that was written"),
        WorkflowArtifact("Requirements", "Requirements for the code")
      )
    ]
  )
  """

  name: str
  description: str
  conversations: List[WorkflowConversation]

  def __init__(self, name: str, description: str, conversations: List[WorkflowConversation]):
    """
    Creates a new workflow phase with the given name, description, and conversations.
    """
    self.name = name
    self.description = description
    self.conversations = conversations
    self.current_conversation_index = 0
  
  def roles(self) -> Set[WorkflowRole]:
    """
    Returns a set of all roles involved in this phase.
    """
    return {role for conversation in self.conversations for role in conversation.roles()}
  
  def artifacts(self) -> Set[WorkflowArtifact]:
    """
    Returns a set of all artifacts involved in this phase.
    """
    return {artifacts for conversation in self.conversations for artifacts in conversation.artifacts()}
  
  def current_conversation(self) -> WorkflowConversation:
    """
    Returns the current conversation in this phase.
    """
    if self.ended():
      raise RuntimeError(f"Conversation {self.name} already ended")
    return self.conversations[self.current_conversation_index]
  
  def next_conversation(self):
    """
    Moves to the next conversation in this phase.
    """
    if self.ended():
      raise RuntimeError(f"Conversation {self.name} already ended")

    self.current_conversation_index += 1
  
  def ended(self) -> bool:
    """
    Returns whether this phase has ended.
    """
    return self.current_conversation_index >= len(self.conversations)
  
  def gpt_str(self) -> str:
    """
    This is the string representation that ChatGPT will receive
    """
    return f"('workflow' name:[{self.name}], description:[{self.description}], conversation names:[{','.join([conversation.name for conversation in self.conversations])}])"

  def __str__(self) -> str:
    """
    This is the string representation for debugging or errors
    """
    return f"WorkflowPhase[{self.name}]"
