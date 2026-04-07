import unittest

from inline_markdown import split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link
from textnode import TextNode, TextType


test_1 = TextNode("Why is _Alakazam_ magic?", TextType.TEXT)
test_2 = TextNode("Alakazam is a **BIG** Word", TextType.TEXT)
test_3 = TextNode("This will hopfully _**be unaltered**_", TextType.CODE)
test_4 = TextNode("This should _**be error", TextType.TEXT)
test_5 = TextNode("Why is Alakazam magic?", TextType.TEXT)

class testSplitNodes(unittest.TestCase):
    
    def test_bold(self):
        test = split_nodes_delimiter([test_2], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("Alakazam is a ", TextType.TEXT),
                TextNode("BIG", TextType.BOLD),
                TextNode(" Word", TextType.TEXT)
            ],
            test,
        )
    
    def test_italic(self):
        test = split_nodes_delimiter([test_1, test_5], "_", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("Why is ", TextType.TEXT),
                TextNode("Alakazam", TextType.ITALIC),
                TextNode(" magic?", TextType.TEXT),
                TextNode("Why is Alakazam magic?", TextType.TEXT)
            ],
            test,
        )

    def test_unaltered(self):
        test = split_nodes_delimiter([test_3], "**", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("This will hopfully _**be unaltered**_", TextType.CODE)
            
            ],
            test,
        )
    """
    def test_error(self):
        self.assertRaises(ValueError, split_nodes_delimiter([test_4], "**", TextType.TEXT))
    """
    #Extract Markdown

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
            )
        self.assertListEqual([("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], matches)

    def test_split_image(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            ],
            new_nodes,
        )

    def test_split_image_single(self):
        node = TextNode(
            "![image](https://www.example.COM/IMAGE.PNG)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://www.example.COM/IMAGE.PNG"),
            ],
            new_nodes,
        )

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://boot.dev) and [another link](https://wikipedia.org) with text that follows",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode("another link", TextType.LINK, "https://wikipedia.org"),
                TextNode(" with text that follows", TextType.TEXT),
            ],
            new_nodes,
        )

    
if __name__ == "__main__":
    unittest.main()