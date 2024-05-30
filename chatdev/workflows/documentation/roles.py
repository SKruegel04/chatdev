"""
This module defines the workflow roles for the documentation workflow.

Modules Imported:
- `WorkflowRole` from `...entities`: Represents a role in the workflow.

Roles:
- `programmer_a`: Represents the role of a senior programmer focused on documenting existing code.
- `programmer_b`: Represents the role of another senior programmer focused on documenting existing code.

`programmer_a` Role:
Attributes:
- `name`: "Programmer A"
- `description`: Describes Programmer A as a senior programmer looking at existing code and documenting it properly, following established standards.
- `model`: "gpt-4o"

`programmer_b` Role:
Attributes:
- `name`: "Programmer B"
- `description`: Describes Programmer B as a senior programmer looking at existing code and documenting it properly, following established standards.
- `model`: "gpt-4o"
"""

from ...entities import WorkflowRole

programmer_a = WorkflowRole(
  name= 'Programmer A',
  description= '''
    You are a senior programmer that looks at existing code and documents
    it properly, depending on the language the code is written in.

    You follow a strict format and stick to previously established standards.
    You always stick to standards during documentation.
  ''',
  model= "gpt-4o"
)

programmer_b = WorkflowRole(
  name= 'Programmer B',
  description= '''
    You are a senior programmer that looks at existing code and documents
    it properly, depending on the language the code is written in.

    You follow a strict format and stick to previously established standards.
    You always stick to standards during documentation.
  ''',
  model= "gpt-4o"
)
