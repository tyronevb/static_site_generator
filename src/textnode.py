from enum import Enum
from htmlnode import LeafNode
class TextType(Enum):
    NORMAL_TEXT = "text"
    BOLD_TEXT = "bold"
    ITALIC_TEXT = "italic"
    CODE_TEXT = "code"
    LINKS = "links"
    IMAGES = "images"

class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, otherTextNode):
        if self.text == otherTextNode.text and \
                self.text_type == otherTextNode.text_type and \
                self.url == otherTextNode.url:
            return True
        else:
            return False
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.NORMAL_TEXT:
            return LeafNode(tag=None, value=text_node.text, props=None)
        case TextType.BOLD_TEXT:
            return LeafNode(tag="b", value=text_node.text, props=None)
        case TextType.ITALIC_TEXT:
            return LeafNode(tag="i", value=text_node.text, props=None)
        case TextType.CODE_TEXT:
            return LeafNode(tag="code", value=text_node.text, props=None)
        case TextType.LINKS:
            return LeafNode(tag="a", value=text_node.text, props={"href": text_node.url})
        case TextType.IMAGES:
            return LeafNode(tag="img", value="", props={"src": text_node.url, "alt": text_node.text,})
        
        case _: 
            raise ValueError (f"Invalid Text Type: {text_node.text_type}")