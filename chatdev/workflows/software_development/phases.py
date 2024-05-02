from ...entities import WorkflowPhase
from .conversations import design_modalities, design_language, coding_code, coding_design, testing_review, testing_test, documenting_spec, documenting_manual

designing = WorkflowPhase(
  name= 'Designing',
  description= '''
    The task is provided by the customer and business modalities
    and use-cases are created for the technical team to implement them properly.
  ''',
  conversations= [design_modalities, design_language],
)

coding = WorkflowPhase(
  name= 'Coding',
  description= '''
    The coding phase. Here the actual code implementation is created.
    Actual code is output in Markdown code blocks with the file name in bold above the block.
  ''',
  conversations= [coding_code, coding_design],
)

testing = WorkflowPhase(
  name= 'Testing',
  description= '''
    The testing phase. The implementation is reviewed and tested properly
    so that it checks all quality marks.
  ''',
  conversations= [testing_review, testing_test],
)

documenting = WorkflowPhase(
  name= 'Documenting',
  description= '''
    The implementation is documented for technical and business people
    so that it can be understood for future extensions, business usage and business integrations.
  ''',
  conversations= [documenting_spec, documenting_manual],
)
