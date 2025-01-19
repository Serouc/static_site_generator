from textnode import TextNode, TextType
from parentnode import ParentNode
from leafnode import LeafNode
from htmlnode import HTMLNode

def main():
    new_textnode = TextNode("This is a text node", "bold", "https://www.boot.dev")
    print(new_textnode.__repr__())



main()