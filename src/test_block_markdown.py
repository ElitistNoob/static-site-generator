import unittest
from block_markdown import (
    BlockType,
    block_to_block_types,
    markdown_to_blocks,
)


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

    def test_block_to_block_types_headings(self):
        block = "### heading3"
        self.assertEqual(
            block_to_block_types(block), BlockType.HEADING
        )

    def test_block_to_block_types_code(self):
        block = (
            "```\nThis is a code block\n with multiple lines\n```"
        )
        self.assertEqual(
            block_to_block_types(block), BlockType.CODE
        )

    def test_block_to_block_types_quote(self):
        block = "> Quote1\n> Quote2\n> Quote3"
        self.assertEqual(
            block_to_block_types(block), BlockType.QUOTE
        )

    def test_block_to_block_types_unordered_list(self):
        block = "- item1\n- item2\n- item3"
        self.assertEqual(
            block_to_block_types(block), BlockType.ULIST
        )

    def test_block_to_block_types_ordered_list(self):
        block = "1. item1\n2. item2\n3. item3"
        self.assertEqual(
            block_to_block_types(block), BlockType.OLIST
        )

    def test_block_to_block_types_paragraph(self):
        block = "This is a paragraph\n with multiple lines"
        self.assertEqual(
            block_to_block_types(block), BlockType.PARAGRAPH
        )
