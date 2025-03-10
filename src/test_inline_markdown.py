import unittest

from textnode import TextType, TextNode
from inline_markdown import split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_images, split_nodes_links, text_to_textnodes

class TestInlineMarkdown(unittest.TestCase):
    def test_split_basic(self):
        node = TextNode("This is text with a `code block` word", TextType.NORMAL_TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE_TEXT)
        self.assertEqual(new_nodes,
                         [TextNode("This is text with a ", TextType.NORMAL_TEXT),
                          TextNode("code block", TextType.CODE_TEXT),
                          TextNode(" word", TextType.NORMAL_TEXT),])
        
    def test_split_basic_bold(self):
        node = TextNode("This is text with a **bold** word", TextType.NORMAL_TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD_TEXT)
        self.assertEqual(new_nodes,
                         [TextNode("This is text with a ", TextType.NORMAL_TEXT),
                          TextNode("bold", TextType.BOLD_TEXT),
                          TextNode(" word", TextType.NORMAL_TEXT),])
        
    def test_split_basic_italics(self):
        node = TextNode("This is text with an *italics* word", TextType.NORMAL_TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC_TEXT)
        self.assertEqual(new_nodes,
                         [TextNode("This is text with an ", TextType.NORMAL_TEXT),
                          TextNode("italics", TextType.ITALIC_TEXT),
                          TextNode(" word", TextType.NORMAL_TEXT),])
        
    def test_split_multiple_nodes(self):
        node = TextNode("This is text with an *italics* word", TextType.NORMAL_TEXT)
        node_2 = TextNode("This is text with *another italics* word", TextType.NORMAL_TEXT)
        new_nodes = split_nodes_delimiter([node, node_2], "*", TextType.ITALIC_TEXT)
        self.assertEqual(new_nodes,
                         [TextNode("This is text with an ", TextType.NORMAL_TEXT),
                          TextNode("italics", TextType.ITALIC_TEXT),
                          TextNode(" word", TextType.NORMAL_TEXT),
                          TextNode("This is text with ", TextType.NORMAL_TEXT),
                          TextNode("another italics", TextType.ITALIC_TEXT),
                          TextNode(" word", TextType.NORMAL_TEXT)])
        
    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", TextType.NORMAL_TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD_TEXT)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.NORMAL_TEXT),
                TextNode("bolded", TextType.BOLD_TEXT),
                TextNode(" word and ", TextType.NORMAL_TEXT),
                TextNode("another", TextType.BOLD_TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", TextType.NORMAL_TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD_TEXT)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.NORMAL_TEXT),
                TextNode("bolded word", TextType.BOLD_TEXT),
                TextNode(" and ", TextType.NORMAL_TEXT),
                TextNode("another", TextType.BOLD_TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and *italic*", TextType.NORMAL_TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD_TEXT)
        new_nodes = split_nodes_delimiter(new_nodes, "*", TextType.ITALIC_TEXT)
        self.assertListEqual(
            [
                TextNode("bold", TextType.BOLD_TEXT),
                TextNode(" and ", TextType.NORMAL_TEXT),
                TextNode("italic", TextType.ITALIC_TEXT),
            ],
            new_nodes,
        )

    def test_extract_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        output = extract_markdown_images(text)
        self.assertEqual([("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")], 
                         output)
        
    def test_extract_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        output = extract_markdown_links(text)
        self.assertEqual([("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")],
                          output)
        
    def test_split_nodes_images(self):
        node = TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)", TextType.NORMAL_TEXT)
        output = split_nodes_images([node])
        self.assertListEqual([
            TextNode("This is text with a ", TextType.NORMAL_TEXT),
            TextNode("rick roll", TextType.IMAGES, "https://i.imgur.com/aKaOqIh.gif"),
            TextNode(" and ", TextType.NORMAL_TEXT),
            TextNode("obi wan", TextType.IMAGES, "https://i.imgur.com/fJRm4Vk.jpeg"),
        ], output)

    def test_split_nodes_links(self):
        node = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", TextType.NORMAL_TEXT)
        output = split_nodes_links([node])
        self.assertListEqual([
                            TextNode("This is text with a link ", TextType.NORMAL_TEXT),
                            TextNode("to boot dev", TextType.LINKS, "https://www.boot.dev"),
                            TextNode(" and ", TextType.NORMAL_TEXT),
                            TextNode(
                                "to youtube", TextType.LINKS, "https://www.youtube.com/@bootdotdev"
                            ),
                        ], output)
        
    def test_split_image_single(self):
        node = TextNode(
            "![image](https://www.example.COM/IMAGE.PNG)",
            TextType.NORMAL_TEXT,
        )
        new_nodes = split_nodes_images([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGES, "https://www.example.COM/IMAGE.PNG"),
            ],
            new_nodes,
        )
    
    def test_text_to_textnodes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(text)
        self.assertListEqual([
            TextNode("This is ", TextType.NORMAL_TEXT),
            TextNode("text", TextType.BOLD_TEXT),
            TextNode(" with an ", TextType.NORMAL_TEXT),
            TextNode("italic", TextType.ITALIC_TEXT),
            TextNode(" word and a ", TextType.NORMAL_TEXT),
            TextNode("code block", TextType.CODE_TEXT),
            TextNode(" and an ", TextType.NORMAL_TEXT),
            TextNode("obi wan image", TextType.IMAGES, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.NORMAL_TEXT),
            TextNode("link", TextType.LINKS, "https://boot.dev"),
        ], nodes)