import unittest

from leafnode import LeafNode
from parentnode import ParentNode


class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])

        self.assertEqual(
            parent_node.to_html(), "<div><span>child</span></div>"
        )

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_grandchildren_two(self):
        grandchild_li_one_node = LeafNode("li", "li_one")
        grandchild_li_two_node = LeafNode("li", "li_two")
        grandchild_li_three_node = LeafNode("li", "li_three")
        grandchild_li_four_node = LeafNode("li", "li_four")
        child_node = ParentNode(
            "ul",
            [
                grandchild_li_one_node,
                grandchild_li_two_node,
                grandchild_li_three_node,
                grandchild_li_four_node,
            ],
        )
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><ul><li>li_one</li><li>li_two</li><li>li_three</li><li>li_four</li></ul></div>",
        )

    def test_to_html_with_grandchildren_three(self):
        grandchild_node = LeafNode(
            None, "No. 1 video game website in France"
        )
        grandchild_node_two = LeafNode(
            "a",
            "link",
            {
                "href": "https://www.jeuxvideo.com",
                "target": "_blank",
            },
        )
        child_node = ParentNode(
            "p",
            [grandchild_node, grandchild_node_two],
        )
        parent_node = ParentNode(
            "div", [child_node], {"class": "wrapper"}
        )
        self.assertEqual(
            parent_node.to_html(),
            '<div><p>No. 1 video game website in France<a href="https://www.jeuxvideo.com" target="_blank">link</a></p></div>',
        )

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )
