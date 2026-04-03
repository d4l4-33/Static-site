import unittest
from htmlnode import HTMLNode


props_dict = {}
props_dict= {"href": "https://www.google.com", "target": "_blank"}
props_to_html_expected = ' href="https://www.google.com" target="_blank"'

class TestHTMLNode(unittest.TestCase):

    def test_eq(self):
        node1 = HTMLNode("p", "bananaphone", None, props_dict)
        self.assertEqual(node1.tag, "p")
        self.assertEqual(node1.value, "bananaphone")
        self.assertEqual(node1.children, None)
        self.assertEqual(node1.props, props_dict)
        
    def test_repr(self):
        node3 = HTMLNode("p", "bananamobile", None, props_dict)
        self.assertEqual(node3.__repr__(), "p, bananamobile, None, {'href': 'https://www.google.com', 'target': '_blank'}")
    

    def test_props_to_html(self): ##d4l4 Ver
        node4 = HTMLNode("p", "bananamobile", None, props_dict)
        self.assertEqual(node4.props_to_html(), props_to_html_expected)

    """ ##Lane Ver
    def test_to_html_props(self): 
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )
    """

if __name__ == "__main__":
    unittest.main()