import unittest
from htmlnode import HTMLNode

#(self, tag=None, value=None, children=None, props=None)

class TestHtmlNode(unittest.TestCase):
    def test_all_none_eq(self):
        node = HTMLNode()
        node2 = HTMLNode()
        self.assertEqual(node, node2)

    def test_props_to_html(self):
        test_props = {
        "href": "https://www.google.com",
        "target": "_blank",
        }
        node = HTMLNode(props=test_props).props_to_html()
        node2 = 'href="https://www.google.com" target="_blank"'
        self.assertEqual(node, node2)

    def test_tag_noteq(self):
        node = HTMLNode(tag = "p")
        node2 = HTMLNode(tag = "a")
        self.assertNotEqual(node, node2)
    
    def test_value_noteq(self):
        node = HTMLNode(value = "the text inside a paragraph")
        node2 = HTMLNode(value = "different text inside a paragraph")
        print(node.__repr__())
        self.assertNotEqual(node, node2)

    def test_children_noteq(self):
        child_node1 = HTMLNode(tag = "p")
        child_node2 = HTMLNode(tag = "a")
        child_node3 = HTMLNode(tag = "h1")
        node = HTMLNode(children = [child_node1, child_node2])
        node2 = HTMLNode(children = [child_node1, child_node3])
        self.assertNotEqual(node, node2)
    
    def test_props_noteq(self):
        test_props1 = {
        "href": "https://www.google.com",
        "target": "_blank",
        }
        test_props2 = {
        "href": "https://www.xtheeverythingapp.com",
        "target": "_blank",
        }
        node = HTMLNode(props = test_props1)
        node2 = HTMLNode(props = test_props2)
        self.assertNotEqual(node, node2)
    
if __name__ == "__main__":
    unittest.main()
