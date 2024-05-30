"""
This module defines the workflow phases for the documentation workflow.

Modules Imported:
- `WorkflowPhase` from `...entities`: Represents a phase in the workflow.
- `documentation` from `.conversations`: Represents the conversations involved in the documentation phase.

Phases:
- `documentation`: Represents the phase where the documentation for the code is written.

`documentation` Phase:
Attributes:
- `name`: "Documentation"
- `description`: Describes the phase where documentation for the code is written.
- `conversations`: List of conversations involved in this phase, which includes the `documentation` conversation.
"""

from ...entities import WorkflowPhase
from .conversations import documentation

documentation = WorkflowPhase(
  name= 'Documentation',
  description= '''
    In this phase, documentation for the code is written.
  ''',
  conversations= [documentation],
)
