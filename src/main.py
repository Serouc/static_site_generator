from textnode import TextNode, TextType
from parentnode import ParentNode
from leafnode import LeafNode
from htmlnode import HTMLNode
import os, shutil

def main():
    new_textnode = TextNode("This is a text node", "bold", "https://www.boot.dev")
    print(new_textnode.__repr__())
    static_to_public()


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



    

main()