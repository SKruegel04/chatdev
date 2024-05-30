from .phases import documentation
from chatdev.entities import Workflow

documentation_workflow = Workflow(
  name = "Documentation",
  description = "Write documentation for an existing project. Your only job is to write documentation, don't change any existing code or logic!",
  phases = [documentation]
)
