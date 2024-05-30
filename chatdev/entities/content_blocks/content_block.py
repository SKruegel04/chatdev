"""
This module defines the `ContentBlock` class which represents a generic content block in a message.

Classes:
- `ContentBlock`: Represents a content block in the workflow messages.

`ContentBlock` Class:
Attributes:
- `type` (str): The type of content block.

Methods:
- `__init__(self, type: str)`: Initializes a ContentBlock with the specified type.
- `dict(self) -> dict`: Placeholder method for returning the dictionary representation of the content block.
"""

class ContentBlock:
  type: str

  def __init__(self, type: str):
    self.type = type

  def dict(self) -> dict:
    pass
