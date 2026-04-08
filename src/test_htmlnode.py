import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode


props_dict = {}
props_dict= {"href": "https://www.google.com", "target": "_blank"}
props_to_html_expected = ' href="https://www.google.com" target="_blank"'

class TestHTMLNode(unittest.TestCase):

    def test_eq(self):
        node = HTMLNode("p", "bananaphone", None, props_dict)
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "bananaphone")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, props_dict)
        
    def test_repr(self):
        node = HTMLNode("p", "bananamobile", None, props_dict)
        self.assertEqual(node.__repr__(), "HTMLNode(p, bananamobile, None, {'href': 'https://www.google.com', 'target': '_blank'})")
    
    def test_props_to_html(self): ##d4l4 Ver
        node = HTMLNode("p", "bananamobile", None, props_dict)
        self.assertEqual(node.props_to_html(), props_to_html_expected)

    """ ##Lane Ver
    def test_to_html_props(self): 
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://www.boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://www.boot.dev"',
        )
    """
    #Leaf Nodes

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_leafnode_repr(self):
        node = LeafNode("p", "Hello, world!", "https://www.bananachicken.notrealurl")
        self.assertEqual(node.__repr__(), "LeafNode(p, Hello, world!, https://www.bananachicken.notrealurl)")

    #Parent Nodes   

    def test_to_html_with_children(self):
        child_node1 = LeafNode("span", "child")
        child_node2 = LeafNode("b", "rollerblade")
        #child_node3 = LeafNode("p", "Hello, world!", "https://www.bananachicken.notrealurl")
        parent_node = ParentNode("div", [child_node1, child_node2])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span><b>rollerblade</b></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
    )






if __name__ == "__main__":
    unittest.main()