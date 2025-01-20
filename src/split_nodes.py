from textnode import TextNode, TextType
from extract_markdown import extract_markdown_images, extract_markdown_links

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

def split_nodes_image(old_nodes):
    result = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            result.append(node)
        elif extract_markdown_images(node.text) == []:
            result.append(node)
        else:
            text = node.text
            image_dict = extract_markdown_images(text)
            for image in image_dict:
                image_alt = image[0]
                image_link = image[1]
                sections = text.split(f"![{image_alt}]({image_link})", 1)
                result.append(TextNode(sections[0], TextType.TEXT))
                result.append(TextNode(image_alt, TextType.IMAGE, image_link))
                text = sections[1]

    return result

def split_nodes_link(old_nodes):
    result = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            result.append(node)
        elif extract_markdown_links(node.text) == []:
            result.append(node)
        else:
            text = node.text
            link_dict = extract_markdown_links(text)
            for link in link_dict:
                link_text = link[0]
                link_url = link[1]
                sections = text.split(f"[{link_text}]({link_url})", 1)
                result.append(TextNode(sections[0], TextType.TEXT))
                result.append(TextNode(link_text, TextType.LINK, link_url))
                text = sections[1]

    return result
