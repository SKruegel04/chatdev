from .phases import coding
from chatdev.entities import Workflow

tiny_software_development_workflow = Workflow(
  name = "Software Development",
  description = "Develops a software project",
  phases = [coding]
)
