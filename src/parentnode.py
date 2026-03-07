from htmlnode import HTMLNode
from leafnode import LeafNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children,  props=None):
        super().__init__(tag=tag, children=children, props=props)
    def to_html(self):
        if not self.tag:
            raise ValueError("Parent node should have a tag")
        
        if not self.children:
            raise ValueError("Parent node without a children")
        

        child_html= ""

        for child in self.children:
            child_html += child.to_html()

        return f"<{self.tag}{self.props_to_html()}>{child_html}</{self.tag}>"



