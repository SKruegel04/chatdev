"""
This module defines the workflow phases for the tiny software development workflow.

Modules Imported:
- `WorkflowPhase` from `...entities`: Represents a phase in the workflow.
- Various conversations from `.conversations`: Represents the conversations involved in each phase.

Phases:
- `coding`: The phase where the actual code implementation is created.

Each phase is defined as a `WorkflowPhase` with appropriate names, descriptions, and conversations.
"""

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
