"""
This module defines the workflow artifacts for the medium software development workflow.

Modules Imported:
- `WorkflowArtifact` from `...entities.workflow_artifact`: Represents an artifact in the workflow.

Artifacts:
- `task`: The business task as defined by the customer to be realized as a software product or feature.
- `modalities`: Contains information about development time, budget, human resource costs, and other constraints.
- `language`: Use cases of the task defined in human language.
- `code`: The code written by the programmer, yet to be designed, reviewed, and tested.
- `designed_code`: Code enhanced by the designer considering architectural decisions, UX, best practices, etc.
- `reviewed_code`: The reviewed code with a list of review items and applied corrections, yet to be tested.
- `tested_code`: The tested code with proper tests, ready to be deployed.
- `spec`: The technical specification of the implemented code, declaring technical aspects.
- `manual`: A manual for the customer detailing how to use the changes and integrate with other departments or companies.

Each artifact is defined as a `WorkflowArtifact` with appropriate names and descriptions.
"""

from ...entities.workflow_artifact import WorkflowArtifact

task = WorkflowArtifact(
  name= 'Task',
  description= '''
    The business task as defined by the customer. It should be realised as a software product or feature.
  ''',
)

modalities = WorkflowArtifact(
  name= 'Modalities',
  description= '''
    The modalities of the task as defined by CEO and CPO. It defines the time for development, the budget,
    human resource costs and similar constraints.
  ''',
)

language = WorkflowArtifact(
  name= 'Language',
  description= '''
    The use cases of the task defined in human language which can be translated between
    business and technical department easily.
  '''
)

code = WorkflowArtifact(
  name= 'Code',
  description= '''
    The code as written by the programmer. It is yet to be designed, reviewed and tested.
  ''',
)

designed_code = WorkflowArtifact(
  name= 'Designed Code',
  description= '''
    The code as enhanced by the designer. It takes into account architecturial decisions
    and things like UX, best practices etc. It is yet to be reviewed and tested.
  ''',
)

reviewed_code = WorkflowArtifact(
  name= 'Reviewed Code',
  description= '''
    The reviewed code containing a list of review items and applied corrections. It is yet to be tested.
  ''',
)

tested_code = WorkflowArtifact(
  name= 'Tested Code',
  description= '''
    The tested code containing the finished code and proper tests. It is ready to be deployed.
  ''',
)

spec = WorkflowArtifact(
  name= 'Specification',
  description= '''
    The technical specification of the implemented code. It declares technical aspects
    for future programmers and can be translated to a manual.
  ''',
)

manual = WorkflowArtifact(
  name= 'Manual',
  description= '''
    A manual written for the customer so that they know how to properly use the changes made
    and can forward integrations to other departments or companies.
  ''',
)
