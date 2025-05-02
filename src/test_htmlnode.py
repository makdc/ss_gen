import unittest

from htmlnode import *


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
            {"class":"greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )
        

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "test paragraph!")
        self.assertEqual(node.to_html(), "<p>test paragraph!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.google.com">Click me!</a>',
        )

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")
        
    
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )  
        
        
        
        
        
        
if __name__ == "__main__":
    unittest.main()