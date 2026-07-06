import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)


    def test_noteq(self):
        node = TextNode("Test text", TextType.ITALIC_TEXT, "https://www.lysol.com")
        node2 = TextNode("Test text", TextType.CODE_TEXT, "https://www.lysol.com")
        self.assertNotEqual(node, node2)


    def test_url(self):
        node = TextNode("Test text", TextType.ITALIC_TEXT, "https://www.lysol.com")
        node2 = TextNode("Test text", TextType.CODE_TEXT, "https://www.espn.com")
        self.assertNotEqual(node, node2)

    def test_url2(self):
        node = TextNode("Test text", TextType.ITALIC_TEXT, "https://www.lysol.com")
        node2 = TextNode("Test text", TextType.ITALIC_TEXT)
        self.assertNotEqual(node, node2)

    def test_url_eq(self):
        node = TextNode("Test text", TextType.ITALIC_TEXT, "pizzaburgers")
        node2 = TextNode("Test text", TextType.ITALIC_TEXT)
        self.assertEqual(node, node2)



if __name__ == "__main__":
    unittest.main()
