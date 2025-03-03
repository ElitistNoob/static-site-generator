import unittest

from textnode import TextType, TextNode
from inline_markdown import split_nodes_delimiter


class TestUtils(unittest.TestCase):
    def test_split_nodes_delimiter_code(self):
        node = TextNode(
            "This is a `code block` node", TextType.TEXT
        )
        self.assertEqual(
            split_nodes_delimiter([node], "`", TextType.CODE),
            [
                TextNode("This is a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" node", TextType.TEXT),
            ],
        )

    def test_split_nodes_delimiter_italic(self):
        node = TextNode(
            "This is a _italic block_ node", TextType.TEXT
        )
        self.assertEqual(
            split_nodes_delimiter([node], "_", TextType.ITALIC),
            [
                TextNode("This is a ", TextType.TEXT),
                TextNode("italic block", TextType.ITALIC),
                TextNode(" node", TextType.TEXT),
            ],
        )

    def test_split_nodes_delimiter_bold(self):
        node = TextNode(
            "This is a **bold** block node", TextType.TEXT
        )
        self.assertEqual(
            split_nodes_delimiter([node], "**", TextType.BOLD),
            [
                TextNode("This is a ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" block node", TextType.TEXT),
            ],
        )

    def test_delim_invalid(self):
        node = TextNode(
            "This is a **bold block node", TextType.TEXT
        )
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "**", TextType.BOLD)

    def test_delim_multi_tags(self):
        node = TextNode(
            "This is a **bold** and _italic_ block node",
            TextType.TEXT,
        )
        new_nodes = split_nodes_delimiter(
            [node], "**", TextType.BOLD
        )
        new_nodes = split_nodes_delimiter(
            new_nodes, "_", TextType.ITALIC
        )
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is a ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" block node", TextType.TEXT),
            ],
        )
