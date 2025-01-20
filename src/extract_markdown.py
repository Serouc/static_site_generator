import re

def extract_markdown_images(text):
    #return re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    #return re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


print(extract_markdown_links("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"))