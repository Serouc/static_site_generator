from htmlnode import HTMLNode
from leafnode import LeafNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        self.tag = tag
        self.children = children
        self.props = props
        super().__init__(self.tag, None, self.children, self.props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("No tag to format as HTML")
        if self.children is None:
            raise ValueError("No children to format as HTML")

        return f"<{self.tag}{self.props_to_html()}>{self.construct_child_string()}</{self.tag}>"
        
    def construct_child_string(self):
        child_string = ""
        children_list = self.children
        for entry in children_list:
            if entry.children is None:
                child_string += entry.to_html()
            else:
                child_string += entry.to_html()
        return child_string
    
        
        

    