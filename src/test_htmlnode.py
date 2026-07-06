import unittest
from htmlnode import HTMLNode
from htmlnode import LeafNode
from htmlnode import ParentNode

class TestHTMLNode(unittest.TestCase):
   #def test_eq(self):
        #node = HTMLNode("<p>", "Test text", {"href": "www.nike.com"})
        #node2 = HTMLNode("<p>", "Test text", {"href": "www.nike.com"})
        #self.assertEqual(node, node2)

    def test_props(self):
        node2 = HTMLNode(tag="p", value="Test text", props={"href": "www.nike.com", "target": "_blank"})
        node3 = HTMLNode()
        node = HTMLNode(tag="p", value="Test text", children=[node2, node3])
        print(node.props_to_html())
        print(node2.props_to_html())


    def test_repr(self):
        testnode1 = HTMLNode()
        testnode2 = HTMLNode()
        node = HTMLNode("<p>", "Test text", [testnode1, testnode2], {"href": "www.nike.com"})
        print(node)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click here", {"href": "www.hopethisworks.com"})
        self.assertEqual(node.to_html(), '<a href="www.hopethisworks.com">Click here</a>')
        
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
        
if __name__ == "__main__":
    unittest.main()