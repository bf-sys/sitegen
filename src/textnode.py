from enum import Enum
from urllib.parse import urlparse
from htmlnode import *

class TextType(Enum):
	TEXT = "Plain text"
	BOLD = "Bold text"
	ITALIC = "Italic text"
	CODE = "Code text"
	LINK = "Link"
	IMAGE = "Image"

class TextNode():
	def __init__(self, text: str, text_type: TextType, url=None):
		self.text = text
		self.text_type = text_type
		url_test = urlparse(url)
		if url_test.scheme and url_test.netloc:
			self.url = url
		else:
			self.url = None
		
	def __eq__(self, other: TextNode) -> bool:
		if self.text == other.text and self.text_type == other.text_type and self.url == other.url:
			return True
		else:
			return False

	def __repr__(self):
		return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
	

def text_node_to_html_node(text_node: TextNode) -> LeafNode:
	match text_node.text_type:	
		case text_node.text_type.TEXT:
			return LeafNode(tag=None, value=text_node.text)
		case text_node.text_type.BOLD:
			return LeafNode(tag="b", value=text_node.text)
		case text_node.text_type.ITALIC:
			return LeafNode(tag="i", value=text_node.text)
		case text_node.text_type.CODE:
			return LeafNode(tag="code", value=text_node.text)
		case text_node.text_type.LINK:
			return LeafNode(tag="a", value=text_node.text, props={"href": text_node.url})
		case text_node.text_type.IMAGE:
			return LeafNode(tag="img", value="", props={"src": text_node.url, "alt": text_node.text})
		case _:	
			raise Exception(f"{text_node.text_type} is not a valid text type")