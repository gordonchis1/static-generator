import unittest
from parentnode import ParentNode
from leafnode import LeafNode

props = {
    "href": "https://www.google.com",
    "target": "_blank",
}

class TestParentNode(unittest.TestCase):
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
    def test_nested_parent_node(self):
        child_parent_node = ParentNode("div", [LeafNode("p", "try nested nodes")])
        parent_node = ParentNode("div", [child_parent_node])

        self.assertEqual(parent_node.to_html(), "<div><div><p>try nested nodes</p></div></div>")
    def test_parent_props(self):
        parent_node = ParentNode("div", [LeafNode("p", "try nested nodes")], props={"href": "http://holamundo.com"})
        self.assertEqual(parent_node.to_html(), '<div href="http://holamundo.com"><p>try nested nodes</p></div>')

    
if __name__ == "__main__":
    unittest.main()