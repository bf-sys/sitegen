import unittest
from htmlnode import *
from textnode import *
from splitter import *

class TestSplitter(unittest.TestCase):
    def test_italics(self):
        node = TextNode("This is a test of finding __italics__.", TextType.TEXT)
        node2 = TextNode("In multiple __italics__ strings.", TextType.TEXT)
        node3 = TextNode("To see if splitting on __italics__ works properly.", TextType.TEXT)
        test = split_nodes_delimiter([node, node2, node3], '__', TextType.ITALIC)
        #print(*test, sep='\n')
        
    def test_multiple_inline(self):
        node = TextNode("This is a __more complicated__ test of __italic words__ in a longer string", TextType.TEXT)
        test = split_nodes_delimiter([node], "__", TextType.ITALIC)
        #print(*test, sep='\n')

    def test_no_close_delimiter(self):
        with self.assertRaises(Exception):
            node = TextNode("This is a test of finding __italics.", TextType.TEXT)
            test = split_nodes_delimiter([node], '__', TextType.ITALIC)
            print(test)
    
    def test_wrong_delimiter(self):
        with self.assertRaises(Exception):
            node = TextNode("This is a test of finding __italics.", TextType.TEXT)
            test = split_nodes_delimiter([node], '**', TextType.ITALIC)
            print(test)
    
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
    
    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        )
        self.assertListEqual([("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], matches)
    
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )