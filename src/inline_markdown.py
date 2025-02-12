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

def split_nodes_images(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.NORMAL_TEXT:
            new_nodes.append(old_node)
            continue
        images = extract_markdown_images(old_node.text)
        sections = []
        start_text = old_node.text
        for image in images:
            sec = start_text.split(f"![{image[0]}]({image[1]})", 1)
            sections.append(sec[0])
            start_text = sec[1]
        if sec[-1] != "":
            sections.append(sec[-1])

        offset = 0
        for i in range(len(images)):
            sections.insert(1+i+offset, images[i])
            offset += 1
        
        for i in range(len(sections)):
            if i % 2 == 0:
                # not a link
                if sections[i] != "":
                    new_nodes.append(TextNode(sections[i], TextType.NORMAL_TEXT))
            else:
                new_nodes.append(TextNode(sections[i][0], TextType.IMAGES, sections[i][1]))
    return new_nodes

def split_nodes_links(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.NORMAL_TEXT:
            new_nodes.append(old_node)
            continue
        links = extract_markdown_links(old_node.text)
        sections = []
        start_text = old_node.text
        for link in links:
            sec = start_text.split(f"[{link[0]}]({link[1]})")
            sections.append(sec[0])
            start_text = sec[1]
        if sec[-1] != "":
            sections.append(sec[-1])

        offset = 0
        for i in range(len(links)):
            sections.insert(1+i+offset, links[i])
            offset += 1
        
        for i in range(len(sections)):
            if i % 2 == 0:
                # not a link
                if sections[i] != "":
                    new_nodes.append(TextNode(sections[i], TextType.NORMAL_TEXT))
            else:
                new_nodes.append(TextNode(sections[i][0], TextType.LINKS, sections[i][1]))
    return new_nodes