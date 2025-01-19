import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_noteqText(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is not the same text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_noteqType(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_noteqURL(self):
        node = TextNode("This is a text node", TextType.BOLD, "dummy/url/")
        node2 = TextNode("This is a text node", TextType.BOLD, "different/url/")
        self.assertNotEqual(node, node2)

    def test_text_to_html(self):
        node = TextNode("This is text", "text").text_node_to_html_node()
        node2 = "This is text"
        self.assertEqual(node.to_html(), node2)

    def test_text_to_image(self):
        node = TextNode("Text describing image","image","location/somwhere/here.jpg").text_node_to_html_node()
        node2 = '<img src="location/somwhere/here.jpg" alt="Text describing image" />'
        self.assertEqual(node.to_html(), node2)

    def test_text_to_image_no_alt(self):
        node = TextNode("", "image", "location/somwhere/here.jpg").text_node_to_html_node()
        node2 = '<img src="location/somwhere/here.jpg" alt="" />'
        self.assertEqual(node.to_html(), node2)

if __name__ == "__main__":
    unittest.main()