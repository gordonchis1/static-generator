# from textnode import TextNode, TextType

# def split_nodes_delimiter(old_nodes, delimiter, text_type):
#     result = []
#     stack = []
#     idxs = {}

#     for nodeIdx in range(0, len(old_nodes)):
#         old_node = old_nodes[nodeIdx]
#         if old_node.text_type is not TextType.TEXT:
#             result.append(old_node)
#             continue
#         idxs[nodeIdx] = []
#         for idx in range(0, len(old_node.text)):
#             text = old_node.text
#             if text[idx: idx + len(delimiter)] == delimiter:
#                 if len(stack) == 0:
#                     stack.append(idx)
#                     idxs[nodeIdx].append(idx)
#                     continue
#             if text[idx: idx + len(delimiter)] == delimiter and len(stack) != 0:
#                 idxs[nodeIdx].append(idx + len(delimiter))
#                 stack.pop()
            
#     if len(stack) != 0:
#         raise Exception(f"In line:{stack[-1]} \n That's invalid Markdown syntax")
    
#     for idx in idxs:
#         if len(idxs[idx]) == 0:
#             result.append(TextNode(old_nodes[idx].text, TextType.TEXT))
#             continue

#         current_old_node = old_nodes[idx]
#         current_old_node_text = current_old_node.text
        
#         new_frirst_text_node = current_old_node_text[0: idxs[idx][0]]
#         new_special_node = current_old_node_text[idxs[idx][0] + len(delimiter): idxs[idx][1] - len(delimiter)]
#         new_second_text_node = current_old_node_text[idxs[idx][1]:]

#         result.append(TextNode(new_frirst_text_node, TextType.TEXT))
#         result.append(TextNode(new_special_node, text_type))
#         result.append(TextNode(new_second_text_node, TextType.TEXT))
    
#     return result
from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes
