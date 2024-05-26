from ...entities import WorkflowPhase
from .conversations import coding_code, coding_test

coding = WorkflowPhase(
  name= 'Coding',
  description= '''
    The coding phase. Here the actual code implementation is created.
    Actual code is output in Markdown code blocks with the file name in bold above the block.

    A code project will be created in the file system that follows the best practices
    of the languages the project is written in.
  ''',
  conversations= [coding_code, coding_test],
)
