import unittest
from markdown_to_html import markdown_to_html_node

class TestLeafNode(unittest.TestCase):
    def test_basic_text(self):
        markdown = "very simple test"
        input = markdown_to_html_node(markdown).to_html()
        result = "<div><p>very simple test</p></div>"
        self.assertEqual(input, result)

    def test_basic_text_over_lines(self):
        markdown = """
still kind of simple
just with a bonus line"""
        input = markdown_to_html_node(markdown).to_html()
        result = "<div><p>still kind of simple\njust with a bonus line</p></div>"
        self.assertEqual(input, result)
    
    def test_image_and_link(self):
        markdown = "and a line with an ![image](image.jpeg) and a [link to boot.dev](https://www.boot.dev)"
        input = markdown_to_html_node(markdown).to_html()
        result = '<div><p>and a line with an <img src="image.jpeg" alt="image" /> and a <a href="https://www.boot.dev">link to boot.dev</a></p></div>'
        self.assertEqual(input, result)

    def test_headings(self):
        markdown = "### heading\n\n## bonanza"
        input = markdown_to_html_node(markdown).to_html()
        result = '<div><h3>heading</h3><h2>bonanza</h2></div>'
        self.assertEqual(input, result)

    def test_invalid_heading(self):
        markdown = "######## invalid heading"
        input = markdown_to_html_node(markdown).to_html()
        result = "<div><p>######## invalid heading</p></div>"
        self.assertEqual(input, result)

    def test_code_block(self):
        markdown = """```
just a code block
    with 2 lines
```"""
        input = markdown_to_html_node(markdown).to_html()
        result = '<div><code>just a code block\n    with 2 lines</code></div>'
        self.assertEqual(input, result)

    def test_unordered_list(self):
        markdown = """
* an unordered
* list
* to be sure
"""
        input = markdown_to_html_node(markdown).to_html()
        result = "<div><ul><li>an unordered</li><li>list</li><li>to be sure</li></ul></div>"
        self.assertEqual(input, result)

    def test_mixed(self):
        markdown = """
# good old heading

1. ordered
2. list
3. for fun

```
just a code block
```

and a line with an ![image](image.jpeg) and a [link to boot.dev](https://www.boot.dev)

"""
        input = markdown_to_html_node(markdown).to_html()
        result = '<div><h1>good old heading</h1><ol><li>ordered</li><li>list</li><li>for fun</li></ol><code>just a code block</code><p>and a line with an <img src="image.jpeg" alt="image" /> and a <a href="https://www.boot.dev">link to boot.dev</a></p></div>'
        self.assertEqual(input, result)

if __name__ == "__main__":
    unittest.main()