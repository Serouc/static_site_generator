import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        print("None URL and __eq__ check OKAY")
        self.assertEqual(node, node2)

    def test_noteqText(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is not the same text node", TextType.BOLD)
        print("Different text check OKAY")
        self.assertNotEqual(node, node2)

    def test_noteqType(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        print("Different texttype check OKAY")
        self.assertNotEqual(node, node2)

    def test_noteqURL(self):
        node = TextNode("This is a text node", TextType.BOLD, "dummy/url/")
        node2 = TextNode("This is a text node", TextType.BOLD, "different/url/")
        print("Different url check OKAY")
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()