import unittest
from textnode import *

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_noteq(self):
        node = TextNode("Test text", TextType.ITALIC, "https://www.lysol.com")
        node2 = TextNode("Test text", TextType.CODE, "https://www.lysol.com")
        self.assertNotEqual(node, node2)

    def test_url(self):
        node = TextNode("Test text", TextType.ITALIC, "https://www.lysol.com")
        node2 = TextNode("Test text", TextType.CODE, "https://www.espn.com")
        self.assertNotEqual(node, node2)

    def test_url2(self):
        node = TextNode("Test text", TextType.ITALIC, "https://www.lysol.com")
        node2 = TextNode("Test text", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_url_eq(self):
        node = TextNode("Test text", TextType.ITALIC, "pizzaburgers")
        node2 = TextNode("Test text", TextType.ITALIC)
        self.assertEqual(node, node2)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_img(self):
        node = TextNode("This is an image", TextType.IMAGE, url="https://image.com")
        img_node = text_node_to_html_node(node)
        print(img_node.to_html())


if __name__ == "__main__":
    unittest.main()
