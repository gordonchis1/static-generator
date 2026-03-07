import unittest
from htmlnode import HTMLNode

props = {
    "href": "https://www.google.com",
    "target": "_blank",
}

class TestHTMLNode(unittest.TestCase):
    def test_repr_eq(self):
        htmlNode = HTMLNode(tag = "a", value = "hola mundo", props=props, children="")
        self.assertEqual(repr(htmlNode), "HTMLNode(tag: a, value: hola mundo, children:, props: {'href': 'https://www.google.com', 'target': '_blank'})")
    def test_props_to_html(self):
        htmlNode = HTMLNode(tag = "a", value = "hola mundo", props=props, children="")
        self.assertEqual(htmlNode.props_to_html(), ' href="https://www.google.com" target="_blank"')
    def test_no_args(self):
        htmlNode = HTMLNode()
        self.assertEqual(repr(htmlNode), "HTMLNode(tag: None, value: None, children:None, props: None)")
    
if __name__ == "__main__":
    unittest.main()