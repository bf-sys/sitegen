import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
   #def test_eq(self):
        #node = HTMLNode("<p>", "Test text", {"href": "www.nike.com"})
        #node2 = HTMLNode("<p>", "Test text", {"href": "www.nike.com"})
        #self.assertEqual(node, node2)

    def test_props(self):
        node2 = HTMLNode(tag="<p>", value="Test text", props={"href": "www.nike.com", "target": "_blank"})
        node3 = HTMLNode()
        node = HTMLNode(tag="<p>", value="Test text", children=[node2, node3])
        print(node.props_to_html())
        print(node2.props_to_html())


    def test_repr(self):
        testnode1 = HTMLNode()
        testnode2 = HTMLNode()
        node = HTMLNode(tag="<p>", value="Test text", children=[testnode1, testnode2], props={"href": "www.nike.com"})
        print(node)




if __name__ == "__main__":
    unittest.main()