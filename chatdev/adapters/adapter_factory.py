"""
This module defines the `AdapterFactory` class which creates specific adapters for AI models.

Modules Imported:
- `OpenAI` from `openai`: Initializes the OpenAI client.
- `Anthropic` from `anthropic`: Initializes the Anthropic client.
- `AnthropicAdapter` from `.anthropic_adapter`: Represents the adapter for Anthropic AI models.
- `OpenAIAdapter` from `.openai_adapter`: Represents the adapter for OpenAI models.
- `Adapter` from `.adapter`: Represents the generic adapter interface.
- `List` from `typing`: Specifies list type (unused but imported).

Classes:
- `AdapterFactory`: Creates specific adapters for AI models based on the model identifier.

`AdapterFactory` Class:
Attributes:
- `openai_client` (OpenAI): The OpenAI client.
- `anthropic_client` (Anthropic): The Anthropic client.

Methods:
- `__init__(self, openai_client: OpenAI, anthropic_client: Anthropic)`: Initializes the AdapterFactory with OpenAI and Anthropic clients.
- `adapter(self, model: str) -> Adapter`: Creates and returns a specific adapter based on the model identifier.
"""

from openai import OpenAI
from anthropic import Anthropic
from .anthropic_adapter import AnthropicAdapter
from .openai_adapter import OpenAIAdapter
from .adapter import Adapter
from typing import List

class AdapterFactory:
  openai_client: OpenAI
  anthropic_client: Anthropic

  def __init__(self, openai_client: OpenAI, anthropic_client: Anthropic):
    self.openai_client = openai_client
    self.anthropic_client = anthropic_client

  def adapter(self, model: str) -> Adapter:
    if model.startswith("gpt-"):
      return OpenAIAdapter(client= self.openai_client, model= model)
    
    if model.startswith("claude-"):
      return AnthropicAdapter(client= self.anthropic_client, model= model)
    
    raise Exception("Could not resolve model")
