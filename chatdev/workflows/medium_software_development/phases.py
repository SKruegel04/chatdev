"""
This module defines the workflow phases for the medium software development workflow.

Modules Imported:
- `WorkflowPhase` from `...entities`: Represents a phase in the workflow.
- Various conversations from `.conversations`: Represents the conversations involved in each phase.

Phases:
- `designing`: Phase where the task provided by the customer is analyzed, and business modalities and use-cases are created.
- `coding`: The phase where the actual code implementation is created.
- `testing`: The phase where the implementation is reviewed and tested properly to ensure it meets all quality standards.
- `documenting`: The phase where the implementation is documented for technical and business people for future extensions, usage, and integrations.

Each phase is defined as a `WorkflowPhase` with appropriate names, descriptions, and conversations.
"""

from ...entities import WorkflowPhase
from .conversations import design_modalities, design_language, coding_code, coding_design, testing_review, testing_test, documenting_spec, documenting_manual

designing = WorkflowPhase(
  name= 'Designing',
  description= '''
    The task is provided by the customer and business modalities
    and use-cases are created for the technical team to implement them properly.

    It's to be decided what kind of software in what languages is written
    and what the system context looks like.

    The outputs are put into documentation files in a folder called docs/.
  ''',
  conversations= [design_modalities, design_language],
)

coding = WorkflowPhase(
  name= 'Coding',
  description= '''
    The coding phase. Here the actual code implementation is created.
    Actual code is output in Markdown code blocks with the file name in bold above the block.

    A code project will be created in the file system that follows the best practices
    of the languages the project is written in.
  ''',
  conversations= [coding_code, coding_design],
)

testing = WorkflowPhase(
  name= 'Testing',
  description= '''
    The testing phase. The implementation is reviewed and tested properly
    so that it checks all quality marks.

    Problems are documented in a docs/testing/ folder.

    Existing code is corrected when tests might fail.
    Tests will be written in the respective languages and frameworks
    so that the code can be tested properly.
  ''',
  conversations= [testing_review, testing_test],
)

documenting = WorkflowPhase(
  name= 'Documenting',
  description= '''
    The implementation is documented for technical and business people
    so that it can be understood for future extensions, business usage and business integrations.

    It includes use cases, diagrams and similar tools to make sure the software can
    be improved upon at a later point.

    The outputs are saved in the docs/ folder.
  ''',
  conversations= [documenting_spec, documenting_manual],
)
