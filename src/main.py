from textnode import TextNode, TextType

print("# hello world")


def main():
    testnode = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(testnode)


main()