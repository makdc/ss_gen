class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
    #tag=string of name, value=string of paragraph, children=list of children, props=dict of properties
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    #tag=None, value=None, children=None, props=None
    
    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        if self.props is None:
            return ""
        props_html = ""
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'
        return props_html
    
    #def props_to_html(self):
    #    prop_list = []
    #    if self.props is None:
    #        return ""
    #    prop_dict = self.props.copy()
    #    for k in prop_dict:
    #        v = prop_dict[k]
    #        prop_list.append(f'{k}="{v}"')
    #    print(' '.join(prop_list))
    #    return ' '.join(prop_list)
    
    def __repr__(self):
        
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"


#from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value is None:
            raise  ValueError('All leaf nodes must have a value')
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
    
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.children is None:
            raise  ValueError('All parent nodes must have a child')
        if self.tag is None:
            raise ValueError("Object is missing tag")
        child_str = []
        for child in self.children:
            #print(child.to_html())
            tmp_str = child.to_html()
            child_str.append(tmp_str)
            #child_str.append(str(child).to_html)
        chilren_html = " ".join(child_str)
        return f"<{self.tag}{self.props_to_html()}>{chilren_html}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"