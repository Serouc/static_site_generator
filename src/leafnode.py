from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    VOID_ELEMENTS = {"img"}
    
    def __init__(self, tag=None, value=None, props=None):
        self.tag = tag
        self.value = value
        self.props = props
        super().__init__(self.tag, self.value, None, self.props)

    def to_html(self):
        if self.value is None:
            raise ValueError("No string to format as HTML")
        if self.tag is None:
            return self.value
        if self.tag in self.VOID_ELEMENTS:
            return f"<{self.tag}{self.props_to_html()} />"
        
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"