"""
This module defines the workflow artifacts for the documentation workflow.

Modules Imported:
- `WorkflowArtifact` from `...entities.workflow_artifact`: Represents an artifact in the workflow.

Artifacts:
- `existing_code`: Represents the existing code that resides in the workspace directory.
- `documented_code`: Represents the code that was documented by the workflow participants.

`existing_code` Artifact:
Attributes:
- `name`: "Existing Code"
- `description`: Description of the existing code that resides in the workspace directory with guidelines to ignore common patterns, e.g., `node_modules`, `build/`, `target/`, `__pycache__`, etc.

`documented_code` Artifact:
Attributes:
- `name`: "Documented Code"
- `description`: Description of the documented code by the workflow participants.
"""

from ...entities.workflow_artifact import WorkflowArtifact

existing_code = WorkflowArtifact(
  name= 'Existing Code',
  description= '''
    The existing code that resides in the workspace directory. You can read, list and write it. Make sure to ignore common ignore patterns, e.g. node_modules, build/, target/, __pycache__ etc.
  ''',
)

documented_code = WorkflowArtifact(
  name= "Documented Code",
  description= "The code that was documented by the workflow participants."
)
