from enum import Enum
import re

from htmlnode import (
    ParentNode,
)
from textnode import (
    text_node_to_html_node,
    TextType,
    TextNode,
)
from inline_markdown import (
    text_to_textnodes,
)


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    ULIST = "unorderded_list"
    OLIST = "ordered_list"

def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        if block.startswith("##"):
            continue
        if block.startswith("#"):
            return block.strip("# ")
    raise Exception("ERROR: No header found in markdown")

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div", children, None)

def markdown_to_blocks(markdown):
    nodes = []
    blocks = markdown.split("\n\n")
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        nodes.append(block.strip())
    return nodes

def block_to_html_node(block):
    block_type = block_to_block_type(block)
    match block_type:
        case BlockType.PARAGRAPH:
            return paragraph_to_html_node(block)
        case BlockType.QUOTE:
            return quote_to_html_node(block)
        case BlockType.HEADING: 
            return heading_to_html_node(block)
        case BlockType.CODE:
            return code_to_html_node(block)
        case BlockType.OLIST: 
            return olist_to_html_node(block)
        case BlockType.ULIST: 
            return ulist_to_html_node(block)
        case _:
            raise ValueError("invalid block type")

def block_to_block_type(markdown_block):
    if re.match(r"#{1,6} ", markdown_block):
        return BlockType.HEADING
    if re.match(r"(```\n)", markdown_block):
        return BlockType.CODE
    if re.match(r">", markdown_block):
        return BlockType.QUOTE
    if re.match(r"-", markdown_block):
        return BlockType.ULIST
    if re.match(r"(\d. )", markdown_block):
        return BlockType.OLIST
    else: return BlockType.PARAGRAPH

def text_to_children(text):
    textnodes = text_to_textnodes(text)
    children = []
    for textnode in textnodes:
        children.append(text_node_to_html_node(textnode))
    return children

def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)

def heading_to_html_node(block):
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    if level + 1 >= len(block):
        raise ValueError(f"invalid heading level: {level}")
    text = block[level + 1 :]
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)

def code_to_html_node(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("invalid code block")
    text = block[4: -3]
    raw_text_node = TextNode(text, TextType.TEXT)
    child = text_node_to_html_node(raw_text_node)
    code = ParentNode("code", [child])
    return ParentNode("pre", [code])

def olist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        parts = item.split(". ", 1)
        text = parts[1]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)

def ulist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)

def quote_to_html_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)



