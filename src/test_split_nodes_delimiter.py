import unittest
from split_nodes_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType

class TestSplitNodes(unittest.TestCase):
    def test_single_node_delimeter(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
            ]
        self.assertEqual(new_nodes, expected)

    def test_no_delimiter(self):
        node = TextNode("This is text with just words", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("This is text with just words", TextType.TEXT)
            ]
        self.assertEqual(new_nodes, expected)
    
    def test_multiple_node_types(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        node2 = TextNode("Text describing image","image","location/somwhere/here.jpg")
        new_nodes = split_nodes_delimiter([node,node2], "`", TextType.CODE)
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
            TextNode("Text describing image","image","location/somwhere/here.jpg")
            ]
        self.assertEqual(new_nodes, expected)

    def test_invalid_delimeter(self):
        node = TextNode("This is text with a `half a code block", TextType.TEXT)
        with self.assertRaises(Exception) as context:
            new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual("Invalid Markdown Syntax (odd number of delimiters)", str(context.exception))


if __name__ == "__main__":
    unittest.main()
