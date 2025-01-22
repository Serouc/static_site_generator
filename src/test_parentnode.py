import unittest
from parentnode import ParentNode
from leafnode import LeafNode
from textnode import TextNode

class TestLeafNode(unittest.TestCase):
    def test_parent_of_leaves(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
            )
        node2 = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(node.to_html(), node2)

    def test_parent_of_parents(self):
        node = ParentNode(
            "p",
            [
                ParentNode(
                    "p",
                    [
                    LeafNode("b", "Bold text"),
                    LeafNode(None, "Normal text"),
                    ],
                ),
                ParentNode(
                    "p",
                    [                
                    LeafNode("i", "italic text"),
                    LeafNode(None, "Normal text"),
                    ],
                )
            ],
        )
        node2 = "<p><p><b>Bold text</b>Normal text</p><p><i>italic text</i>Normal text</p></p>"
        print(node)
        self.assertEqual(node.to_html(), node2)
    
    def test_oddnesting(self):
        parent = ParentNode(
                    "p",
                    [
                    LeafNode("b", "Bold text"),
                    LeafNode(None, "Normal text"),
                    ],
                )
        node = ParentNode(
                    "p",
                    [
                    parent,
                    LeafNode("i", "italic text"),
                    LeafNode(None, "Normal text"),
                    ],
                )
        node2 = "<p><p><b>Bold text</b>Normal text</p><i>italic text</i>Normal text</p>"
        self.assertEqual(node.to_html(), node2)
    
    def test_prop_blankchild(self):
        node = ParentNode(
            "div",
            [LeafNode(None, "Content")],
            props={"id": "main", "class": "container"}
        )
        node2 = '<div id="main" class="container">Content</div>'
        self.assertEqual(node.to_html(), node2)

    def test_no_tag(self):
        node = ParentNode(None,[LeafNode("b", "Bold text"),LeafNode(None, "Normal text")],)
        with self.assertRaises(ValueError) as context:
            node.to_html()
        self.assertEqual("No tag to format as HTML", str(context.exception))

    def test_no_leaves(self):
        node = ParentNode("p",None,)
        with self.assertRaises(ValueError) as context:
            node.to_html()
        self.assertEqual("No children to format as HTML", str(context.exception))

if __name__ == "__main__":
    unittest.main()
