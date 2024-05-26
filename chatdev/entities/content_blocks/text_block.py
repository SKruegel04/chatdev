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
