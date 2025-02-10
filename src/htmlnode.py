class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
      self.tag = tag
      self.value = value
      self.children = children
      self.props = props
    
    def to_html(self):
      # child classes to override this method to render themselves as HTML
        raise NotImplementedError("to_html method not implemented")
   
    def props_to_html(self):
      # returns a sring represents the HTML attributres of the node
        if self.props:
            str = ""
            for key,value in self.props.items():
                str += f' {key}="{value}"'
            return str
        return ""
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
        
    def to_html(self):
        if self.value == None:
            raise ValueError("invalid HTML: must have a value")
        if self.tag == None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("invalid HTML: no tag")
        if not self.children:
            raise ValueError("invalid HTML: no children")
        child_html = ""
        for child in self.children:
            child_html += child.to_html()
        return f"<{self.tag}>{self.props_to_html()}{child_html}</{self.tag}>"
    
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"