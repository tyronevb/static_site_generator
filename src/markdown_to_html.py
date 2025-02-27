from block_markdown import markdown_to_blocks, block_to_block_type, BlockType
from htmlnode import HTMLNode, ParentNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node, TextNode, TextType

def markdown_to_html_node(markdown):
    # split markdown into blocks
    blocks = markdown_to_blocks(markdown)
    block_nodes = []
    for block in blocks:
        block_node = block_to_html_node(block)
        block_nodes.append(block_node)
    return ParentNode("div", block_nodes, None)

def block_to_html_node(block):
    # get block type
    block_type = block_to_block_type(block)
    if block_type == BlockType.PARAGRAPH:
        return paragraph_to_html_node(block)
    if block_type == BlockType.CODE:
        return code_to_html_node(block)
    if block_type == BlockType.QUOTE:
        return quote_to_html_node(block)
    if block_type == BlockType.HEADING:
        return heading_to_html_node(block)
    if block_type == BlockType.OLIST:
        return ordered_list_to_html_node(block)
    if block_type == BlockType.ULIST:
        return unordered_list_to_html_node(block)
    
def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children_html_nodes = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children_html_nodes.append(html_node)
    return children_html_nodes

def paragraph_to_html_node(block):
    lines = block.split("\n")
    lines = [line.strip() for line in lines]
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)

def code_to_html_node(block):
    text = block[4:-3]
    text_node = TextNode(text, TextType.NORMAL_TEXT)
    child = text_node_to_html_node(text_node)
    code = ParentNode("code", [child])
    return ParentNode("pre", [code])

def quote_to_html_node(block):
    lines = block.split("\n")
    lines = [line.strip()[1:] for line in lines]
    paragraph = "\n".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("blockquote", children)

def heading_to_html_node(block):
    level = block.split(" ")[0].count("#")
    heading = " ".join(block.split(" ")[1:])
    children = text_to_children(heading)
    return ParentNode(f"h{level}", children)

def ordered_list_to_html_node(block):
    list_items = []
    items_on_list = block.split("\n")
    items_on_list = [item[3:] for item in items_on_list]
    for item in items_on_list:
        children = text_to_children(item)
        list_items.append(ParentNode("li", children))
    return ParentNode("ol", list_items)

def unordered_list_to_html_node(block):
    list_items = []
    items_on_list = block.split("\n")
    items_on_list = [item[2:] for item in items_on_list]
    for item in items_on_list:
        children = text_to_children(item)
        list_items.append(ParentNode("li", children))
    return ParentNode("ul", list_items)