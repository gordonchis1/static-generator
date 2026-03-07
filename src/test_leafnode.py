import unittest
from leafnode import LeafNode

props = {
    "href": "https://www.google.com",
    "target": "_blank",
}

class TestHTMLNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    def test_tag(self):
        node = LeafNode("p", "Hola mundo")
        node2 = LeafNode("p", "Hola mundo")
        self.assertEqual(node.tag, node2.tag )
    def test_value(self):
        node = LeafNode("p", "Hola mundo")
        node2 = LeafNode("p", "Hola mundo")
        self.assertEqual(node.value, node2.value)
    def test_repr(self):
        node = LeafNode("p", "Hola mundo")
        self.assertEqual(node.__repr__(), "HTMLNode(tag: p, value: Hola mundo, props: None)")

if __name__ == "__main__":
    unittest.main()