import unittest
from block_markdown import markdown_to_blocks, block_to_block_type

class TestExtractMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        input = markdown_to_blocks("""
# This is a heading with trailing spaces   

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

         * This is the first list item in a list block with leading spaces
* This is a list item
* This is another list item
"""
                                  )
        result = [
            '# This is a heading with trailing spaces', 'This is a paragraph of text. It has some **bold** and *italic* words inside of it.', 
            '* This is the first list item in a list block with leading spaces\n* This is a list item\n* This is another list item'
            ]
        self.assertEqual(input, result)

    def test_blank_lines_with_spaces(self):
        input = markdown_to_blocks("""
The following line has 5 spaces
     
This is a follow up line to confirm
"""
        )
        result = ["The following line has 5 spaces\n     \nThis is a follow up line to confirm"]
        self.assertEqual(input, result)
    
    def test_code_markdown_to_block(self):
        input = markdown_to_blocks("""
```
good old fashioned
code bl```ock
right here
```
""")
        result = ['```\ngood old fashioned\ncode bl```ock\nright here\n```']
        self.assertEqual(input, result)

    def test_block_to_block_type_code(self):
        input = block_to_block_type("""```
good old fashioned
code bl```ock
right here
```""")
        result = "code"
        self.assertEqual(input, result)

    def test_block_to_block_type_ordered_list(self):
        input = block_to_block_type(
"""1. got an ordered list
2. right
3. here""")
        result = "ordered list"
        self.assertEqual(input, result)
    
    def test_block_to_block_type_unordered_list(self):
        input = block_to_block_type("* here is\n* an\n* unordered list")
        result = "unordered list"
        self.assertEqual(input, result)

    def test_block_to_block_type_quote(self):
        input = block_to_block_type(">here is\n>a\n>quote block")
        result = "quote"
        self.assertEqual(input, result)
    
    def test_block_to_block_type_heading(self):
        input = block_to_block_type("#### just a heading")
        result = "heading"
        self.assertEqual(input, result)
    
    def test_block_to_block_type_paragraph(self):
        input = block_to_block_type("finally a paragraph## with random ```nonsense1. ")
        result = "paragraph"
        self.assertEqual(input, result)

if __name__ == "__main__":
    unittest.main()