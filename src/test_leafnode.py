import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_to_html_no_value(self):
        node = LeafNode("h1", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_no_tag(self):
        node = LeafNode(None, "LeafNode content without a tag")
        self.assertEqual(
            node.to_html(), "LeafNode content without a tag"
        )

    def test_to_html_a(self):
        node = LeafNode(
            "a",
            "Lorem ipsum dolor si amet",
            {"href": "https://www.google.com"},
        )
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.google.com">Lorem ipsum dolor si amet</a>',
        )

    def test_to_html_p(self):
        node = LeafNode(
            "p",
            "Lorem ipsum dolor si amet",
        )
        self.assertEqual(
            node.to_html(),
            "<p>Lorem ipsum dolor si amet</p>",
        )
