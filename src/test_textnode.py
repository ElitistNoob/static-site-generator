import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a test Node", TextType.BOLD)
        node2 = TextNode("This is a test Node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_iq(self):
        node = TextNode("This is a bold Node", TextType.BOLD)
        node2 = TextNode("This is a link Node", TextType.LINK, "https://www.pygame.org/news")
        self.assertNotEqual(node, node2)

    def test_link_type_has_url(self):
        node = TextNode("this is a link", TextType.LINK, "https://www.pygame.org/news")
        self.assertIs(node.text_type, TextType.LINK)
        self.assertIsNotNone(node.url)

    def test_image_type_has_url(self):
        node = TextNode("this is an image", TextType.IMAGE, "https://www.pygame.org/news")
        self.assertIs(node.text_type, TextType.IMAGE)
        self.assertIsNotNone(node.url)

    def test_nonlink_type_has_none_url(self):
        node = TextNode("This is not a link", TextType.TEXT)
        self.assertIsNot(node.text_type, TextType.LINK)
        self.assertIsNot(node.text_type, TextType.IMAGE)
        self.assertIsNone(node.url)

if __name__ == "__main__":
    unittest.main()
