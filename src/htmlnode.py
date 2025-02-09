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