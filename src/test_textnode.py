import unittest

from textnode import TextNode, TextType, text_node_to_html_node


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

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_link(self):
        node = TextNode("This is a link", TextType.LINK, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link")
        self.assertEqual(html_node.props, "href")
        self.assertEqual(html_node.__repr__(), "a, This is a link, href")

if __name__ == "__main__":
    unittest.main()