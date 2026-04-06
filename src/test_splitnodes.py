import unittest

from splitnodes import split_nodes_delimiter
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
    """

    def test_unaltered(self):
        test = split_nodes_delimiter([test_3], "**", TextType.ITALIC)
        expect = TextNode("This will hopfully _**be unaltered**_", TextType.CODE)
        self.assertEqual(test, expect)
    
    def test_error(self):
        test = split_nodes_delimiter([test_4], "**", TextType.TEXT)
        expect = "Closing delimiter not found"
        self.assertRaises(ValueError, test, "Closing delimiter not found")
    """
if __name__ == "__main__":
    unittest.main()