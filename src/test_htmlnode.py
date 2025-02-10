import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_all_default(self):
        node = HTMLNode()
        self.assertEqual(node.tag, None)
        self.assertEqual(node.value, None)
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)
    
    def test_no_children(self):
        node = HTMLNode(tag="p", value="This is some text", props={"target": "_blank"})
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "This is some text")
        self.assertEqual(node.props, {"target": "_blank"})

    def test_repr(self):
        node = HTMLNode(tag="p", value="This is some text", props={"target": "_blank"})
        self.assertEqual("HTMLNode(p, This is some text, None, {'target': '_blank'})", repr(node))

    def test_props_to_html(self):
        node = HTMLNode(tag="p", value="This is some text", props={"target": "_blank"})
        self.assertEqual(' target="_blank"', node.props_to_html())

    def test_leafnode(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual("<p>This is a paragraph of text.</p>", node.to_html())

    def test_leafnode_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual('<a href="https://www.google.com">Click me!</a>', node.to_html())

    def test_leafnode_no_children(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(None, node.children)

    def test_parentnode(self):
        child_nodes = [ LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ]
        node = ParentNode("p", child_nodes)
        self.assertEqual("<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>", node.to_html())

    def test_parentnode_nested(self):
        child_nodes = [ LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
            ParentNode("a", [LeafNode(None, "Nested text")])
        ]
        node = ParentNode("p", child_nodes)
        self.assertEqual("<p><b>Bold text</b>Normal text<i>italic text</i>Normal text<a>Nested text</a></p>", node.to_html())