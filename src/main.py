from textnode import TextNode, TextType
from parentnode import ParentNode
from leafnode import LeafNode
from htmlnode import HTMLNode
from markdown_to_html import markdown_to_html_node
from extract_markdown import extract_title
import os, shutil

def main():
    static_to_public()

    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root =  os.path.dirname(script_dir)
    public_dir = os.path.join(project_root, "public")
    content_dir = os.path.join(project_root, "content")

    generate_pages_recursive(content_dir, os.path.join(project_root, "template.html"), public_dir)


def static_to_public():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root =  os.path.dirname(script_dir)
    public_dir = os.path.join(project_root, "public")
    static_dir = os.path.join(project_root, "static")
    if os.path.exists(public_dir):
        shutil.rmtree(public_dir)
    
    os.mkdir(public_dir)
    copy_static_to_public(static_dir, public_dir)

def copy_static_to_public(working_dir, public_dir):
    static_dir_contents = os.listdir(working_dir)
    for object in static_dir_contents:
        if os.path.isfile(os.path.join(working_dir, object)):
            print(f"Copying: {os.path.join(working_dir, object)}\nTo: {os.path.join(public_dir, object)}")
            shutil.copyfile(os.path.join(working_dir, object),os.path.join(public_dir, object))
        elif os.path.isdir(os.path.join(working_dir, object)):
            print(f"Creating new folder:{os.path.join(public_dir, object)}")
            os.mkdir(os.path.join(public_dir, object))
            copy_static_to_public(os.path.join(working_dir, object), os.path.join(public_dir, object))

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    content_dir_contents = os.listdir(dir_path_content)
    for object in content_dir_contents:
        if os.path.isfile(os.path.join(dir_path_content, object)):
            file = os.path.splitext(os.path.basename(object))

            file_name = file[0]
            file_ext = file[1]
            print(file_ext)
            if file_ext == ".md":
                generate_page(os.path.join(dir_path_content, object), template_path, os.path.join(dest_dir_path, f"{file_name}.html"))
        elif os.path.isdir(os.path.join(dir_path_content, object)):
            os.mkdir(os.path.join(dest_dir_path, object))
            generate_pages_recursive(os.path.join(dir_path_content, object), template_path, os.path.join(dest_dir_path, object))


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as f:
        markdown = f.read()
    with open(template_path) as t:
        html_string = t.read()

    title = extract_title(markdown)
    content = markdown_to_html_node(markdown).to_html()
    html_string = html_string.replace("{{ Title }}", title).replace("{{ Content }}", content)

    with open(dest_path, "w") as d:
        d.write(html_string)



main()