"""
This module defines the workflow conversations for the documentation workflow.

Modules Imported:
- `WorkflowConversation` from `...entities`: Represents a conversation in the workflow.
- `programmer_a`, `programmer_b` from `.roles`: Represents the roles of participants in the conversation.
- `existing_code`, `documented_code` from `.artifacts`: Represents the input and output artifacts of the conversation.

Conversations:
- `documentation`: Represents the conversation where the documentation for existing code is written.

`documentation` Conversation:
Attributes:
- `name`: "Documentation"
- `description`: Describes the tasks involved in the conversation, including reading existing code, writing respective doc blocks, and making important comments. If the code is self-explanatory, it should stick to doc blocks.
- `lead`: `programmer_a`
- `assistant`: `programmer_b`
- `input`: `existing_code`
- `output`: `documented_code`
"""

from ...entities import WorkflowConversation
from .roles import programmer_a, programmer_b
from .artifacts import existing_code, documented_code

documentation = WorkflowConversation(
  name= 'Documentation',
  description= '''
    In this conversation the documentation for existing code is written.
    You read existing code, take a look at it and relate it to
    other code found and write down the respective doc blocks,
    function and variable documentation and very important comments for parts
    that stick out.

    If the code is self-explanatory, don't explain it in detail, only stick
    to doc blocks.
  ''',
  lead= programmer_a,
  assistant= programmer_b,
  input= existing_code,
  output= documented_code,
)
