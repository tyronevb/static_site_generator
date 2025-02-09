import unittest

from htmlnode import HTMLNode

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