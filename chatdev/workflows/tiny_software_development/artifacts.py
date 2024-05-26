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
