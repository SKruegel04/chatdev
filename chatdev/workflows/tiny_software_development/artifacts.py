"""
This module defines the workflow artifacts for the tiny software development workflow.

Modules Imported:
- `WorkflowArtifact` from `...entities.workflow_artifact`: Represents an artifact in the workflow.

Artifacts:
- `task`: The business task as defined by the customer to be realized as a software product or feature.
- `code`: The code to be written by the workflow participants.
- `tested_code`: Code that was improved with tests that have been written.

Each artifact is defined as a `WorkflowArtifact` with appropriate names and descriptions.
"""

from ...entities.workflow_artifact import WorkflowArtifact

task = WorkflowArtifact(
  name= 'Task',
  description= '''
    The business task as defined by the customer. It should be realised as a software product or feature.
  ''',
)

code = WorkflowArtifact(
  name= "Code",
  description= "The code to be written by the workflow participants"
)

tested_code = WorkflowArtifact(
  name= "Tested Code",
  description= "Code that was improved with tests that have been written"
)
