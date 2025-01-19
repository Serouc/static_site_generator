from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result = []
    
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            result.append(node)
        elif node.text_type == TextType.TEXT:
            if delimiter not in node.text:
                    result.append(node)
            elif node.text.count(delimiter)%2 != 0:
                raise Exception("Invalid Markdown Syntax (odd number of delimiters)")
            else:
                split_text = node.text.split(delimiter)
                new_nodes = []
                for i, text in enumerate(split_text):
                    if i%2 == 0:
                        new_nodes.append(TextNode(text, TextType.TEXT))
                    if i%2 != 0:
                        new_nodes.append(TextNode(text, text_type))
                result.extend(new_nodes)
    
    return result

def quicktest():
    node = TextNode("This is text with a `code block` word", TextType.TEXT)                     
    split_nodes = split_nodes_delimiter([node,], "`", TextType.CODE)
    return split_nodes

print(quicktest())

        
