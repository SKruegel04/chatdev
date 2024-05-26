from ...entities import WorkflowConversation
from .roles import ceo, cpo, cto, programmer, designer, reviewer, tester
from .artifacts import task, modalities, language, code, designed_code, reviewed_code, tested_code, spec, manual

design_modalities = WorkflowConversation(
  name= 'Design (Modalities)',
  description= '''
    The task given by the customer is analyzed and the respective modalities are created.
  ''',
  lead= ceo,
  assistant= cpo,
  input= task,
  output= modalities,
)

design_language = WorkflowConversation(
  name= 'Design (Language)',
  description= '''
    From the task and modalities specific use-cases are created that help the technical
    team to form working code from them.
  ''',
  lead= ceo,
  assistant= cto,
  input= modalities,
  output= language,
)

coding_code = WorkflowConversation(
  name= 'Coding (Code)',
  description= '''
    The initial implementation of the given use-cases realized as code.
    The code is not perfect yet, but it works.
  ''',
  lead= cto,
  assistant= programmer,
  input= language,
  output= code,
)

coding_design = WorkflowConversation(
  name= 'Coding (Design)',
  description= '''
    The given code is analyzed for common architecturial problems and
    improved upon. Best practices are discussed and implemented by the programmer.
    After specifying problems the designer doesn't end the conversation directly, but
    lets the programmer correct the code (switch) and after corrections the programmer
    lets the designer end the conversation.
  ''',
  lead= programmer,
  assistant= designer,
  input= code,
  output= designed_code,
)

testing_review = WorkflowConversation(
  name= 'Testing (Review)',
  description= '''
    The completed code is reviewed for common code problems, errors
    and best practice problems. The programmer resolves problems.
    After specifying problems the reviewer doesn't end the conversation directly, but
    lets the programmer correct the code (switch) and after corrections the programmer
    lets the reviewer end the conversation.
  ''',
  lead= programmer,
  assistant= reviewer,
  input= designed_code,
  output= reviewed_code,
)

testing_test = WorkflowConversation(
  name= 'Testing (Test)',
  description= '''
    The given code is tested if it contains all business cases. Tests are written
    by the programmer by the test concept given by the tester.
  ''',
  lead= programmer,
  assistant= tester,
  input= reviewed_code,
  output= tested_code,
)

documenting_spec = WorkflowConversation(
  name= 'Documenting (Specification)',
  description= '''
    A technical specification is created that covers all aspects of the code
    so that following programmers and technical people can fully understand
    what it is doing.
  ''',
  lead= cto,
  assistant= programmer,
  input= tested_code,
  output= spec,
)

documenting_manual = WorkflowConversation(
  name= 'Documenting (Manual)',
  description= '''
    A business documentation is created for the customer. It explains
    what was implemented on a business level, which use-cases are covered
    and how integration into other systems can be done.
  ''',
  lead= ceo,
  assistant= cpo,
  input= spec,
  output= manual,
)
