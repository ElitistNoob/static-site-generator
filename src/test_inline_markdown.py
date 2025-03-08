import unittest

from textnode import TextType, TextNode
from inline_markdown import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_image,
    split_nodes_link,
    text_to_textnodes,
)


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

    def test_extract_images(self):
        text = "This is a text with an image and an alt text ![Matrix](https://i.imgur.com/aKaOqIh.gif)"
        self.assertListEqual(
            extract_markdown_images(text),
            [("Matrix", "https://i.imgur.com/aKaOqIh.gif")],
        )

    def test_extract_multiple_images(self):
        text = "This is [image #1] - ![alt_text](https://i.imgur.com/aKaOqIh.gif), and this is [image #2] - ![alt_text_2](https://i.imgur.com/fJRm4Vk.jpeg)"
        self.assertListEqual(
            extract_markdown_images(text),
            [
                ("alt_text", "https://i.imgur.com/aKaOqIh.gif"),
                (
                    "alt_text_2",
                    "https://i.imgur.com/fJRm4Vk.jpeg",
                ),
            ],
        )

    def test_extract_link(self):
        text = "This is a text with a link and an anchor text [anchor_text](https://i.imgur.com/aKaOqIh.gif)"
        self.assertListEqual(
            extract_markdown_links(text),
            [("anchor_text", "https://i.imgur.com/aKaOqIh.gif")],
        )

    def test_extract_multiple_links(self):
        text = "This is [link #1] - [anchor_text](https://i.imgur.com/aKaOqIh.gif), and this is [link #2] - [anchor_text_2](https://i.imgur.com/fJRm4Vk.jpeg)"
        self.assertListEqual(
            extract_markdown_links(text),
            [
                (
                    "anchor_text",
                    "https://i.imgur.com/aKaOqIh.gif",
                ),
                (
                    "anchor_text_2",
                    "https://i.imgur.com/fJRm4Vk.jpeg",
                ),
            ],
        )

    def test_split_image_nodes(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode(
                    "image",
                    TextType.IMAGE,
                    "https://i.imgur.com/zjjcJKZ.png",
                ),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image",
                    TextType.IMAGE,
                    "https://i.imgur.com/3elNhQu.png",
                ),
            ],
        )

    def test_split_link_nodes_trailing_text(self):
        node = TextNode(
            "This is text with an [link](https://i.imgur.com/zjjcJKZ.png) and another [second link](https://i.imgur.com/3elNhQu.png) with trailing text",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode(
                    "link",
                    TextType.LINK,
                    "https://i.imgur.com/zjjcJKZ.png",
                ),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second link",
                    TextType.LINK,
                    "https://i.imgur.com/3elNhQu.png",
                ),
                TextNode(" with trailing text", TextType.TEXT),
            ],
        )

    def test_split_image(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode(
                    "image",
                    TextType.IMAGE,
                    "https://i.imgur.com/zjjcJKZ.png",
                ),
            ],
            new_nodes,
        )

    def test_split_image_single(self):
        node = TextNode(
            "![image](https://www.example.COM/IMAGE.PNG)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode(
                    "image",
                    TextType.IMAGE,
                    "https://www.example.COM/IMAGE.PNG",
                ),
            ],
            new_nodes,
        )
