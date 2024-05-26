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
