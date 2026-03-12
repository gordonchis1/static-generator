import re
from textnode import TextNode, TextType

def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def split_nodes_link(old_nodes):
    result = []

    for old_node in old_nodes:
        split_nodes = []
        matches = extract_markdown_links(old_node.text)
        if len(matches) == 0 or old_node.text_type != TextType.TEXT:
            result.append(old_node)
            continue
        current_old_text = old_node.text
        sections = []
        for match in matches:
            delimiter = f"[{match[0]}]({match[1]})"
            sections = current_old_text.split(delimiter, 1)
            current_old_text = sections[1]
            if len(sections[0]) != 0:
                split_nodes.append(TextNode(sections[0], old_node.text_type))
            split_nodes.append(TextNode(match[0], TextType.LINK, match[1]))
        
        if len(current_old_text) != 0:
            split_nodes.append(TextNode(current_old_text, TextType.TEXT))
            
        result.extend(split_nodes)
   
    return result
     
    
def split_nodes_image(old_nodes):
    result = []


    for old_node in old_nodes:
        split_nodes = []
        matches = extract_markdown_images(old_node.text)
        if len(matches) == 0 or old_node.text_type != TextType.TEXT:
            result.append(old_node)
            continue
        current_old_text = old_node.text
        sections = []
        for match in matches:
            delimiter = f"![{match[0]}]({match[1]})"
            sections = current_old_text.split(delimiter, 1)
            current_old_text = sections[1]
            if len(sections[0]) != 0:
                split_nodes.append(TextNode(sections[0], old_node.text_type))
            split_nodes.append(TextNode(match[0], TextType.IMAGE, match[1]))
        
        if len(current_old_text) != 0:
            split_nodes.append(TextNode(current_old_text, TextType.TEXT))
            
        result.extend(split_nodes)


   
    return result