from textnode import TextNode, TextType
from htmlnode import LeafNode

print("# hello world")


def main():
    testnode = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(testnode)

def text_node_to_html_node(text_node):
    pass

main()