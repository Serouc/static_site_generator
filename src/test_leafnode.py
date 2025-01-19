import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_to_html_no_prop(self):
        node = LeafNode("p", "This is a paragraph of text.").to_html()
        node2 = "<p>This is a paragraph of text.</p>"
        self.assertEqual(node, node2)
    
    def test_to_html_with_prop(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"}).to_html()
        node2 = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
