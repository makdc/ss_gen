import unittest

from htmlnode import HTMLNode

#tag=string of name, value=string of paragraph, children=list of children, props=dict of properties
class textHTMLNode(unittest.TestCase):
        
    def test_values(self):
        node1 = HTMLNode(
            "This is a name node", 
            "test paragraph", 
            ['child1','child2','child3'], 
            {"key1":"value1","key2":"value2","key3":"value3"}
            )
        self.assertEqual(node1.tag,"This is a name node")
        self.assertEqual(node1.value,"test paragraph")
        self.assertEqual(node1.children,['child1','child2','child3'])
        self.assertEqual(node1.props,{"key1":"value1","key2":"value2","key3":"value3"})
    
    def test_repr(self):
        node = HTMLNode(
            "t",
            "test paragraph",
            None,
            {"key": "value"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(t, test paragraph, children: None, {'key': 'value'})",
        )   
         
    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            'class="greeting" href="https://boot.dev"',
        )
        
if __name__ == "__main__":
    unittest.main()