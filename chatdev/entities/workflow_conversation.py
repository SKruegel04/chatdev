from typing import Set
from . import WorkflowArtifact, WorkflowRole

class WorkflowConversation:
  """
  A workflow conversation describes a conversation between two roles in a workflow.

  Examples
  --------
  WorkflowConversation(
    "Code Review",
    "Code review between developer and CEO",
    WorkflowRole("Developer", "Developer working on the code"),
    WorkflowRole("CEO", "CEO of the company"),
    WorkflowArtifact("Requirements", "Requirements for the code"),
    WorkflowArtifact("Code", "The code that was written"),
  )
  """
  def __init__(self, name: str, description: str, lead: WorkflowRole, assistant: WorkflowRole, input: WorkflowArtifact, output: WorkflowArtifact):
    """
    Creates a new workflow conversation with the given name, description, roles, and artifacts.
    """
    self.name = name
    self.description = description
    self.lead = lead
    self.assistant = assistant
    self.input = input
    self.output = output

  def roles(self) -> Set[WorkflowRole]:
    """
    Returns a set of all roles involved in this conversation.
    """
    return {self.lead, self.assistant}

  def artifacts(self) -> Set[WorkflowArtifact]:
    """
    Returns a set of all artifacts involved in this conversation.
    """
    return {self.input, self.output}
  
  def gpt_str(self) -> str:
    """
    This is the string representation that ChatGPT will receive
    """
    return f"('conversation' name:[{self.name}], description:[{self.description}], lead name:[{self.lead.name}], assistant name:[{self.assistant.name}], input name:[{self.input.name}], output name:[{self.output.name}])"

  def __str__(self) -> str:
    """
    This is the string representation for debugging or errors
    """
    return f"WorkflowConversation[{self.name}]"