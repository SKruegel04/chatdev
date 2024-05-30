"""
This module defines the workflow conversations for the tiny software development workflow.

Modules Imported:
- `WorkflowConversation` from `...entities`: Represents a conversation in the workflow.
- Various roles from `.roles`: Represents the roles of participants in the conversations.
- Various artifacts from `.artifacts`: Represents the input and output artifacts of the conversations.

Conversations:
- `coding_code`: Initial implementation of the given use-cases realized as code.
- `coding_test`: Given code is tested if it contains all business cases, with tests written by the programmer based on the tester's concept.

Each conversation is defined as a `WorkflowConversation` with appropriate names, descriptions, leads, assistants, inputs, and outputs.
"""

from ...entities import WorkflowConversation
from .roles import programmer, tester
from .artifacts import task, code, tested_code

coding_code = WorkflowConversation(
  name= 'Coding (Code)',
  description= '''
    The initial implementation of the given use-cases realized as code.
    The code is not perfect yet, but it works.
  ''',
  lead= programmer,
  assistant= tester,
  input= task,
  output= code,
)

coding_test = WorkflowConversation(
  name= 'Coding (Test)',
  description= '''
    The given code is tested if it contains all business cases. Tests are written
    by the programmer by the test concept given by the tester.
  ''',
  lead= programmer,
  assistant= tester,
  input= code,
  output= tested_code,
)
