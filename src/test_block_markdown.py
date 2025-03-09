import unittest
from block_markdown import markdown_to_blocks


class test_block_markdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
    This is **bolded** paragraph

    This is another paragraph with _italic_ text and `code` here
    This is the same paragraph on a new line

    - This is a list
    - with items
    """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_markdown_two(self):
        md = """
    # Heading 1
    ## Heading 2
    ### Heading 3

    **Bold Text**  
    _Italic Text_  

    - Unordered list item 1  
    - Unordered list item 2  

    1. Ordered list item 1
    2. Ordered list item 2

    [Link to OpenAI](https://www.openai.com)  
    ![Sample Image](https://via.placeholder.com/150)  
    """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "# Heading 1\n## Heading 2\n### Heading 3",
                "**Bold Text**\n_Italic Text_",
                "- Unordered list item 1\n- Unordered list item 2",
                "1. Ordered list item 1\n2. Ordered list item 2",
                "[Link to OpenAI](https://www.openai.com)\n![Sample Image](https://via.placeholder.com/150)",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
