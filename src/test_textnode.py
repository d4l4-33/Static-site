import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a link node", TextType.LINK)
        self.assertNotEqual(node, node2)
        
    def test_URL_true(self):
        node = TextNode("This is a link node", TextType.LINK, "http//:www.boot.dev")
        node2= TextNode("This is a link node", TextType.LINK)
        self.assertTrue(node.url)
        self.assertFalse(node2.url)


if __name__ == "__main__":
    unittest.main()