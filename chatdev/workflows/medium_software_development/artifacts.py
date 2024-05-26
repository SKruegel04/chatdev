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
