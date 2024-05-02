
class Message:
  def __init__(self, role: str, content: str):
    self.role = role
    self.content = content

  def dict(self) -> dict:
    return {
      "role": self.role,
      "content": self.content      
    }
