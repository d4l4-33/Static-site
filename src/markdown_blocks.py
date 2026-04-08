from enum import Enum
import re

from htmlnode import (
    HTMLNode,
    LeafNode,
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


def block_to_block_type(markdown_block):
    if re.match(r"#{1,6} ", markdown_block):
        return BlockType.HEADING
    if re.match(r"```\n", markdown_block):
        return BlockType.CODE
    if re.match(r">", markdown_block):
        return BlockType.QUOTE
    if re.match(r"-", markdown_block):
        return BlockType.ULIST
    if re.match(r"(\d. )", markdown_block):
        return BlockType.OLIST
    else: return BlockType.PARAGRAPH

    
def markdown_to_blocks(markdown):
    nodes = []
    blocks = markdown.split("\n\n")
    for block in blocks:
        if block == "":
            continue
        nodes.append(block.strip())
    return nodes


def markdown_to_html_node(markdown):
    block_nodes= []
    blocks = markdown_to_blocks(markdown)
    html_block = None
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.CODE:
            block_nodes.append(text_node_to_html_node(TextNode(block, TextType.CODE)))
            continue
        html_block = ParentNode(block_type, text_to_children(block))
        block_nodes.append(html_block)
    parent_node = ParentNode("div", block_nodes)
    return parent_node


def text_to_children(text):
    leafnodes = []
    textnodes = text_to_textnodes(text)
    for textnode in textnodes:
        leafnodes.append(text_node_to_html_node(textnode))
    return leafnodes
 

def blocktype_to_tag(block_type):
    match block_type:
        case BlockType.PARAGRAPH:
            return "<p>"
        case BlockType.QUOTE:
            return "<blockquote>"
        case BlockType.HEADING: 
            pass
            #return f"<h{count}>" ####h1 - h6
        case BlockType.CODE:
            return "<code>"
        

#splitta i blocks
#varje block blir en Parent Node med rätt tag, ingen value
    # varje leaf node får rätt html-tag baserat på parent node blocktype-tag

md = """
## Heading

This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here

```
Fantastic code
```

"""

print(markdown_to_html_node(md).to_html)