
class WorkflowRole:
  """
  A workflow role describes a specific agent or person inside a workflow.
  
  Examples
  --------

  WorkflowRole("CEO", "CEO of the company")
  WorkflowRole("Developer", "Developer working on the code")
  """

  name: str
  description: str
  model: str

  def __init__(self, name: str, description: str, model: str):
    """ 
    Creates a new workflow role with the given name and description.
    """
    self.name = name
    self.description = description
    self.model = model
  
  def gpt_str(self) -> str:
    """
    This is the string representation that ChatGPT will receive
    """
    return f"('role' name:[{self.name}], description:[{self.description}])"

  def __str__(self) -> str:
    """
    This is the string representation for debugging or errors
    """
    return f"WorkflowRole[{self.name}]"
