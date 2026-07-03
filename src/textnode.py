from enum import Enum
from urllib.parse import urlparse

class TextType(Enum):
	PLAIN_TEXT = "Plain text"
	BOLD_TEXT = "Bold text"
	ITALIC_TEXT = "Italic text"
	CODE_TEXT = "Code text"
	LINK = "Link"
	IMAGE = "Image"

class TextNode():
	def __init__(self, text: str, text_type: TextType, url: str | None):
		self.text = text
		self.text_type = text_type
		if urlparse(url):
			self.url = url
		else:
			url = None
		

	def __eq__(self, other: TextNode) -> bool:
		if self.text == other.text and self.text_type == other.text_type and self.url == other.url:
			return True
		else:
			return False
		
	def __repr__(self):
		return f"TextNode({self.text}, {self.text_type.value}, {self.url})"