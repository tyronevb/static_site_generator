from textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    split_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL_TEXT:
            split_nodes.append(node)
            continue
        splits_for_this_node = []
        segments = node.text.split(delimiter)
        if len(segments) % 2 == 0:
            # unclosed markdown
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(segments)):
            if segments[i] == "":
                continue
            if i % 2 == 0:
                splits_for_this_node.append(TextNode(segments[i], node.text_type))
            else:
                splits_for_this_node.append(TextNode(segments[i], text_type))
        split_nodes.extend(splits_for_this_node)
    return split_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)",text)