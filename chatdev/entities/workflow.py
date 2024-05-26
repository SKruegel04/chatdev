from .workflow_phase import WorkflowPhase
from .workflow_conversation import WorkflowConversation
from .workflow_role import WorkflowRole
from .workflow_artifact import WorkflowArtifact
from typing import List, Set

class Workflow:
  name: str
  description: str
  phases: List[WorkflowPhase]

  def __init__(self, name: str, description: str, phases: List[WorkflowPhase]):
    self.name = name
    self.description = description
    self.phases = phases
    self.current_phase_index = 0

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

  def __str__(self) -> str:
    return f"Workflow[{self.name}]"
