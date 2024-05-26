from .phases import designing, coding, testing, documenting
from chatdev.entities import Workflow

medium_software_development_workflow = Workflow(
  name = "Software Development",
  description = "You are developing a software project. First you analyze the existing files and the software, if available and then you follow the conversation tasks to expand, improve, modernize and stablize the software. You will also run and test the software by creating a docker environment. You will make sure the software works and every file and part of it makes sense and is properly connected.",
  phases = [
    designing,
    coding,
    testing,
    documenting
  ]
)
