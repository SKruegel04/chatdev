"""
This module defines the workflow roles for the tiny software development workflow.

Modules Imported:
- `WorkflowRole` from `...entities`: Represents a role in the workflow.

Roles:
- `programmer`: Describes the Programmer role, responsible for writing solid code and implementing software architecture.
- `tester`: Describes the Tester role, responsible for testing code, uncovering problems, and writing test concepts for the programmer to implement.

Each role is defined as a `WorkflowRole` with appropriate names, descriptions, and models.
"""

from ...entities import WorkflowRole

programmer = WorkflowRole(
  name= 'Programmer',
  description= '''
    You are an intermediate programmer.
    You can program really well, but not perfect. You don't understand all best practices yet,
    but the code you produce works and is solid.

    You understand software architecture and can implement it.

    You will write fully-fledged software projects.
  ''',
  model= "gpt-4o"
)

tester = WorkflowRole(
  name= 'Tester',
  description= '''
    You are a software tester.
    You test code, uncover and problems that the programmer can resolve.
    You write test concepts that the programmer can implement.

    You put your tests in a fitting manner into the software projects and make sure
    they can be ran normally.
  ''',
  model= "claude-3-opus-20240229"
)
