class WorkflowArtifact:
  """
  A workflow artifact describes inputs and outputs of conversations.
  
  Examples
  --------
  WorkflowArtifact("Requirements", "Requirements for the code")
  WorkflowArtifact("Code", "The code that was written")
  """

  def __init__(self, name: str, description: str):
    """
    Creates a new workflow artifact with the given name and description.
    """
    self.name = name
    self.description = description
  
  def gpt_str(self) -> str:
    """
    This is the string representation that ChatGPT will receive
    """
    return f"('artifact' name:[{self.name}], description:[{self.description}])"

  def __str__(self) -> str:
    """
    This is the string representation for debugging or errors
    """
    return f"WorkflowArtifact[{self.name}]"
