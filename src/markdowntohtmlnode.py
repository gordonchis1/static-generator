from markdowntoblocks import markdown_to_blocks
from blocksnode import block_to_block_type, BlockType
from htmlnode import HTMLNode
from parentnode import ParentNode
from textnode import TextNode, TextType,text_node_to_html_node
from leafnode import LeafNode
from texttotextnodes import text_to_text_nodes


def parse_text(text):
    return " ".join(text.split("\n"))



def text_to_children(text):
    text_nodes = text_to_text_nodes(parse_text(text))
    nodes = []
    for text_node in text_nodes:
        nodes.append(text_node_to_html_node(text_node))

    return nodes

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    childs = []

    for block in blocks:
        block_type = block_to_block_type(block)
        match block_type:
            case BlockType.PARAGRAPH:
                block_childs = text_to_children(block)
                childs.append(ParentNode("p", block_childs))
            case BlockType.HEADING:
                line = " ".join(block.split(" ")[1:])
                block_childs = text_to_children(line)
                childs.append(ParentNode(f"h{len(block.split(" ")[0])}", block_childs))
            case BlockType.CODE:
                value = block[4:-3]
                childs.append(ParentNode("pre", [text_node_to_html_node(TextNode(value, TextType.CODE))]))
            case BlockType.OLIST:
                lines = block.split("\n")
                block_childs = []
                for line in lines:
                    block_childs.append(ParentNode("li", text_to_children(line[3:])))
                childs.append(ParentNode("ol", block_childs))
            case BlockType.ULIST:
                lines = block.split("\n")
                block_childs = []
                for line in lines:
                    block_childs.append(ParentNode("li", text_to_children(line[2:])))
                childs.append(ParentNode("ul", block_childs))
            case BlockType.QUOTE:
                lines = block.split("\n")
                text_list = []
                for line in lines:
                    text_list.append(line.lstrip(">").strip())
                block_childs = text_to_children(" ".join(text_list))
                childs.append(ParentNode("blockquote", block_childs))
        
    root = ParentNode("div", childs )
    return root
