import unittest
from extract_markdown import extract_markdown_images, extract_markdown_links, extract_title

class TestExtractMarkdown(unittest.TestCase):
    def test_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        input = extract_markdown_images(text)
        result = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(input, result)
    
    def test_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        input = extract_markdown_links(text)
        result = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        self.assertEqual(input, result)

    def test_mix(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and [to youtube](https://www.youtube.com/@bootdotdev)"
        input = [extract_markdown_images(text),extract_markdown_links(text)]
        result = [[("rick roll", "https://i.imgur.com/aKaOqIh.gif")], [("to youtube", "https://www.youtube.com/@bootdotdev")]]
        self.assertEqual(input, result)

    def test_invalid_alt_text(self):
        text = "This is text with a ![rick roll[with nested alt brackets]](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        input = extract_markdown_images(text)
        result = [("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(input, result)

    def test_extract_title_valid(self):
        text = """# heading here

other stuff
"""
        input = extract_title(text)
        result = "heading here"
        self.assertEqual(input, result)

    def test_extract_title_invalid(self):
        text = """no heading

more text
"""
        with self.assertRaises(Exception):
            extract_title(text)


if __name__ == "__main__":
    unittest.main()