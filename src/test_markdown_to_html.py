import unittest
from markdown_to_html import markdown_to_html_node

class TestMarkdownToHTML(unittest.TestCase):
    def test_paragraphs(self):
        md = """
    This is **bolded** paragraph
    text in a p
    tag here

    This is another paragraph with *italic* text and `code` here

    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )
    
    #TODO: why should the inline stuff remain the same for code blocks? I mean, it does make sense
    def test_codeblock(self):
        md = """
```
This is text that *should* remain
the **same** even with inline stuff
```
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that *should* remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_quote(self):
        md = """
>This is a quote
>**Yep** in bold
>Still quoting
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a quote\n<b>Yep</b> in bold\nStill quoting</blockquote></div>",
        )

    def test_orderedlist(self):
        md = """
1. Milk
2. Eggs
3. Write a recursive function
4. Code an LLM

This is a lingering paragraph.
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>Milk</li><li>Eggs</li><li>Write a recursive function</li><li>Code an LLM</li></ol><p>This is a lingering paragraph.</p></div>",
        )

    def test_unorderedlist(self):
        md = """
* Milk
* Eggs
* Write a recursive function
* Code an LLM

This is a lingering paragraph.
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>Milk</li><li>Eggs</li><li>Write a recursive function</li><li>Code an LLM</li></ul><p>This is a lingering paragraph.</p></div>",
        )

    def test_heading(self):
        md = """
# This is a level 1 heading

#### This is a *level* 4 heading with italics

###### This is a `level` 6 heading with codes

This is a lingering paragraph.
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>This is a level 1 heading</h1><h4>This is a <i>level</i> 4 heading with italics</h4><h6>This is a <code>level</code> 6 heading with codes</h6><p>This is a lingering paragraph.</p></div>",
        )