import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a test Node", TextType.BOLD)
        node2 = TextNode("This is a test Node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_iq(self):
        node = TextNode("This is a bold Node", TextType.BOLD)
        node2 = TextNode(
            "This is a link Node",
            TextType.LINK,
            "https://www.pygame.org/news",
        )
        self.assertNotEqual(node, node2)

    def test_link_type_has_url(self):
        node = TextNode(
            "this is a link",
            TextType.LINK,
            "https://www.pygame.org",
        )
        self.assertIs(node.text_type, TextType.LINK)
        self.assertIsNotNone(node.url)

    def test_image_type_has_url(self):
        node = TextNode(
            "this is an image",
            TextType.IMAGE,
            "https://www.pygame.org/news",
        )
        self.assertIs(node.text_type, TextType.IMAGE)
        self.assertIsNotNone(node.url)

    def test_nonlink_type_has_none_url(self):
        node = TextNode("This is not a link", TextType.TEXT)
        self.assertIsNot(node.text_type, TextType.LINK)
        self.assertIsNot(node.text_type, TextType.IMAGE)
        self.assertIsNone(node.url)


class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold node")
        self.assertEqual(
            html_node.to_html(), "<b>This is a bold node</b>"
        )

    def test_italic(self):
        node = TextNode("This is a italic node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is a italic node")
        self.assertEqual(
            html_node.to_html(), "<i>This is a italic node</i>"
        )

    def test_code(self):
        node = TextNode(
            "() => console.log('Hello World!')", TextType.CODE
        )
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(
            html_node.value, "() => console.log('Hello World!')"
        )
        self.assertEqual(
            html_node.to_html(),
            "<code>() => console.log('Hello World!')</code>",
        )

    def test_link(self):
        node = TextNode(
            "This is a link node",
            TextType.LINK,
            "https://www.google.com",
        )
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link node")
        self.assertEqual(
            html_node.props,
            {"href": "https://www.google.com"},
        )
        self.assertEqual(
            html_node.to_html(),
            '<a href="https://www.google.com">This is a link node</a>',
        )

    def text_img(self):
        node = TextNode(
            "This is an image node",
            TextType.IMAGE,
            "https://www.google.com",
        )
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {
                "src": "https://www.google.com",
                "alt": "This is an image node",
            },
        )
        self.assertEqual(
            html_node.to_html(),
            '<img src="https://www.google.com" alt="This is an image node"></img>',
        )


if __name__ == "__main__":
    unittest.main()
