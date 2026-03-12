import unittest
from textnode import TextNode, TextType
from texttotextnodes import text_to_text_nodes


class TestTextToTextNodes(unittest.TestCase):
    def test_text_to_text_nodes(self):
        text = 'This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)'
        new_text_nodes = text_to_text_nodes(text)
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
            new_text_nodes
        )
    def test_text_to_text_nodes_bold(self):
        text = "**hola mundo**"
        new_text_node = text_to_text_nodes(text)
        self.assertListEqual([TextNode("hola mundo", TextType.BOLD)], new_text_node)
    def test_text_to_text_nodes_code(self):
        text = "`hola mundo`"
        new_text_node = text_to_text_nodes(text)
        self.assertListEqual([TextNode("hola mundo", TextType.CODE)], new_text_node)
    def test_text_to_text_nodes_italic(self):
        text = "_hola mundo_"
        new_text_node = text_to_text_nodes(text)
        self.assertListEqual([TextNode("hola mundo", TextType.ITALIC)], new_text_node)
    def test_text_to_text_node_image(self):
        text = "![hola mundo](https://holamundo.com/image)"
        new_text_node = text_to_text_nodes(text)
        self.assertListEqual([TextNode("hola mundo", TextType.IMAGE, "https://holamundo.com/image")], new_text_node)
    def test_text_to_text_node_link(self):
        text = "[hola mundo](https://holamundo.com/link)"
        new_text_node = text_to_text_nodes(text)
        self.assertListEqual([TextNode("hola mundo", TextType.LINK, "https://holamundo.com/link")], new_text_node)
        

if __name__ == "__main__":
    unittest.main()