"""
This module defines the `Tool` class representing a tool used in the workflow.

Modules Imported:
- `List` from `typing`: Specifies list type.

Classes:
- `Tool`: Represents a tool used in the workflow.

`Tool` Class:
Attributes:
- `name` (str): The name of the tool.
- `description` (str): The description of the tool.
- `input_schema` (dict): The input schema for the tool.

Methods:
- `__init__(self, name: str, description: str, input_schema: dict)`: Initializes a Tool with name, description, and input schema.
"""

from typing import List

class Tool:
  name: str
  description: str
  input_schema: dict

  def __init__(self, name: str, description: str, input_schema: dict):
    self.name = name
    self.description = description
    self.input_schema = input_schema
