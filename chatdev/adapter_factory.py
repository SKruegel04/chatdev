from openai import OpenAI
from anthropic import Anthropic
from chatdev.adapters import AnthropicAdapter, OpenAIAdapter
from .adapter import Adapter

class AdapterFactory:
  def __init__(self, openai_client: OpenAI, anthropic_client: Anthropic):
    self.openai_client = openai_client
    self.anthropic_client = anthropic_client

  def adapter(self, model: str) -> Adapter:
    if model.startswith("gpt-"):
      return OpenAIAdapter(client= self.openai_client, model= model)
    
    if model.startswith("claude-"):
      return AnthropicAdapter(client= self.anthropic_client, model= model)
    
    raise Exception("Could not resolve model")
