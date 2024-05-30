"""
This module defines the `TextBlock` class which represents a block of text content in a message.

Modules Imported:
- `ContentBlock` from `.content_block`: Represents a generic content block in a message.

Classes:
- `TextBlock`: Represents a block of text content in the workflow messages.

`TextBlock` Class:
Attributes:
- `text` (str): The text content of the block.

Methods:
- `__init__(self, text: str)`: Initializes a TextBlock with the specified text.
- `__str__(self)`: Returns a string representation of the text block.
- `dict(self) -> dict`: Returns the dictionary representation of the text block.
"""

from .content_block import ContentBlock

class TextBlock(ContentBlock):
  text: str

  def __init__(self, text: str):
    super().__init__(type= "text")

    self.text = text

  def __str__(self):
    return f"TextBlock(text= {self.text})"
  
  def dict(self) -> dict:
    return {
      "text": self.text
    }
