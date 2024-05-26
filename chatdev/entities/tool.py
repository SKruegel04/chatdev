from typing import List

class Tool:
  name: str
  description: str
  input_schema: dict

  def __init__(self, name: str, description: str, input_schema: dict):
    self.name = name
    self.description = description
    self.input_schema = input_schema
