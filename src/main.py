from textnode import TextNode, TextType


def main():
    node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    return print(f"{node}")
    



main()
