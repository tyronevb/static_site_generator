import unittest

from textnode import TextType, TextNode, text_node_to_html_node

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", text_type=TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", text_type=TextType.BOLD_TEXT)
        self.assertEqual(node, node2)

    def test_eq_with_url(self):
        node = TextNode("This is a text node", text_type=TextType.BOLD_TEXT, url="https://www.sample.com")
        node2 = TextNode("This is a text node", text_type=TextType.BOLD_TEXT, url="https://www.sample.com")
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = TextNode("This is a text node", TextType.NORMAL_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertNotEqual(node, node2)

    def test_eq_false2(self):
        node = TextNode("This is a text node", TextType.NORMAL_TEXT)
        node2 = TextNode("This is a text node2", TextType.NORMAL_TEXT)
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.NORMAL_TEXT, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)", repr(node)
        )
    
class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        text_node = TextNode(text="This is a normal text node",
                         text_type=TextType.NORMAL_TEXT)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a normal text node")

    def test_bold(self):
        text_node = TextNode(text="This is a bold text node",
                         text_type=TextType.BOLD_TEXT)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold text node")

    def test_image(self):
        text_node = TextNode(text="This is an image node",
                        text_type=TextType.IMAGES,
                        url="www.dreaimages.test")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, 
                         {"src": "www.dreaimages.test", "alt": "This is an image node"})
    
    def test_text_to_html_normal(self):
        text_node = TextNode(text="This is a normal text node",
                         text_type=TextType.NORMAL_TEXT)
        
        html = text_node_to_html_node(text_node)
        self.assertEqual("LeafNode(None, This is a normal text node, None)", repr(html))

    def test_text_to_html_normal_html(self):
        text_node = TextNode(text="This is a normal text node",
                         text_type=TextType.NORMAL_TEXT)
        
        html = text_node_to_html_node(text_node)
        self.assertEqual("This is a normal text node", html.to_html())

    def test_text_to_html_bold_html(self):
        text_node = TextNode(text="This is a bold text node",
                         text_type=TextType.BOLD_TEXT)
        
        html = text_node_to_html_node(text_node)
        self.assertEqual("<b>This is a bold text node</b>", html.to_html())

    def test_text_to_html_italics_html(self):
        text_node = TextNode(text="This is an italics text node",
                         text_type=TextType.ITALIC_TEXT)
        
        html = text_node_to_html_node(text_node)
        self.assertEqual("<i>This is an italics text node</i>", html.to_html())

    def test_text_to_html_code_html(self):
        text_node = TextNode(text="This is a code node",
                         text_type=TextType.CODE_TEXT)
        
        html = text_node_to_html_node(text_node)
        self.assertEqual("<code>This is a code node</code>", html.to_html())
    
    def test_text_to_html_link_html(self):
        text_node = TextNode(text="This is a link node",
                         text_type=TextType.LINKS,
                         url="www.drealinks.test")
        
        html = text_node_to_html_node(text_node)
        self.assertEqual('<a href="www.drealinks.test">This is a link node</a>', html.to_html())

    def test_text_to_html_image_html(self):
        text_node = TextNode(text="This is an image node",
                         text_type=TextType.IMAGES,
                         url="www.dreaimages.test")
        
        html = text_node_to_html_node(text_node)
        self.assertEqual('<img src="www.dreaimages.test" alt="This is an image node"></img>', html.to_html())