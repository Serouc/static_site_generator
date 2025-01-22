import re

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_title(markdown):
    first_line = markdown.splitlines()[0]
    if first_line.startswith("# "):
        return first_line.lstrip("# ")
    else:
        raise Exception("No h1 header")
    