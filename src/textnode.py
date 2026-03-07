from enum import Enum
from leafnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self, TEXT, TEXT_TYPE: TextType, url = None):
        self.text = TEXT 
        self.text_type = TEXT_TYPE
        self.url = url
    
    def __eq__(self, other):
        if self.text == other.text and self.text_type == other.text_type and self.url == other.url:
            return True
        return False
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"



def text_node_to_html_node(text_node):
    match text_node.text_type.value:
            case "text":
              return LeafNode(None, value=text_node.text)
            case "bold":
              return LeafNode("b", value=text_node.text)
            case "italic":
              return LeafNode("i", value=text_node.text)
            case "code":
              return LeafNode("code", value=text_node.text)
            case "link":
                return LeafNode("a", value=text_node.text, props={"href": text_node.url}) 
            case "image":
                return LeafNode("img", value="", props={"src": text_node.url, "alt": ""})
            case _:
                raise Exception("Invalid text type")
