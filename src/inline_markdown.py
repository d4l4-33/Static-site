import re
from textnode import TextType, TextNode

def text_to_textnodes(text):
    nodes = split_nodes_delimiter([TextNode(text, TextType.TEXT)], "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            result.append(node)
            continue
        split_nodes = []
        sections = node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Closing delimiter not found")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else: 
                split_nodes.append(TextNode(sections[i], text_type))
        result.extend(split_nodes)
    return result


def split_nodes_image(old_nodes):
    result = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            result.append(node)
            continue
        original_text = node.text
        images = extract_markdown_images(original_text)
        for image in images:
            image_text, image_url = image[0], image[1]
            text_split = original_text.split(f"![{image_text}]({image_url})", 1)
            if len(text_split) != 2:
                raise ValueError("invalid markdown, image section not closed")
            if text_split[0] != "":
                result.append(TextNode(text_split[0], TextType.TEXT))
            result.append(TextNode(image_text, TextType.IMAGE, image_url))
            original_text = text_split[1]
        if original_text != "":
            result.append(TextNode(original_text, TextType.TEXT))
    return result


def split_nodes_link(old_nodes):
    result = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            result.append(node)
            continue
        original_text = node.text
        links = extract_markdown_links(original_text)
        for link in links:
            link_text, link_url = link[0], link[1]
            text_split = original_text.split(f"[{link_text}]({link_url})", 1)
            if len(text_split) != 2:
                raise ValueError("invalid markdown, link section not closed")
            if text_split[0] != "":
                result.append(TextNode(text_split[0], TextType.TEXT))
            result.append(TextNode(link_text, TextType.LINK, link_url))
            original_text = text_split[1]
        if original_text != "":
            result.append(TextNode(original_text, TextType.TEXT))
    return result


def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)

