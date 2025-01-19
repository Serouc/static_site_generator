from enum import Enum
from leafnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = TextType(text_type)
        self.url = url
    
    def __eq__(self, other):
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url
    
    def __repr__(self):
        cls = self.__class__.__name__
        return f"{cls}({self.text}, {self.text_type.value}, {self.url})"
    
    def text_node_to_html_node(self):
        if self.text_type == TextType.TEXT:
            return LeafNode(value=self.text)
        if self.text_type == TextType.BOLD:
            return LeafNode("b",self.text)
        if self.text_type == TextType.ITALIC:
            return LeafNode("i",self.text)
        if self.text_type == TextType.CODE:
            return LeafNode("code",self.text)
        if self.text_type == TextType.LINK:
            return LeafNode("a",self.text,{"href": self.url})
        if self.text_type == TextType.IMAGE:
            return LeafNode("img","",{"src": self.url, "alt": self.text})
    