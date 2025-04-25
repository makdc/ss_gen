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
        prop_list = []
        if self.props is None:
            return ""
        prop_dict = self.props.copy()
        for k in prop_dict:
            v = prop_dict[k]
            prop_list.append(f'{k}="{v}"')
        print(' '.join(prop_list))
        return ' '.join(prop_list)
    
    def __repr__(self):
        
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
            