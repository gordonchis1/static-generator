import unittest
from textnode import TextNode, TextType
from splitnodesdelimiter import split_nodes_delimiter


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_code_block(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual(new_nodes[0].text_type.value, "text")
        self.assertEqual(new_nodes[1].text_type.value, "code")
        self.assertEqual(new_nodes[2].text_type.value, "text")
        self.assertEqual(new_nodes[0].text + new_nodes[1].text + new_nodes[2].text, "This is text with a code block word")
        
    def test_bold(self):
        node = TextNode("This is text with a **bold text** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes[0].text_type.value, "text")
        self.assertEqual(new_nodes[1].text_type.value, "bold")
        self.assertEqual(new_nodes[2].text_type.value, "text")
        self.assertEqual(new_nodes[0].text + new_nodes[1].text + new_nodes[2].text, "This is text with a bold text word")
    def test_italic(self):
        node = TextNode("This is text with a _italic text_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(new_nodes[0].text_type.value, "text")
        self.assertEqual(new_nodes[1].text_type.value, "italic")
        self.assertEqual(new_nodes[2].text_type.value, "text")
        self.assertEqual(new_nodes[0].text + new_nodes[1].text + new_nodes[2].text, "This is text with a italic text word")
    def test_without(self):
        node = TextNode("This is text with a normal word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes[0].text_type.value, "text")
        self.assertEqual(new_nodes[0].text, "This is text with a normal word")
 
 
 

if __name__ == "__main__":
    unittest.main()