from parentnode import ParentNode
from block_markdown import markdown_to_blocks, block_to_block_type
from text_to_textnodes import text_to_textnodes
from textnode import TextNode
from block_markdown import BlockType

def markdown_to_html_node(markdown):
    return ParentNode("div", blocks_to_children(markdown))

def blocks_to_children(markdown):
# Split the markdown into blocks
    blocks = markdown_to_blocks(markdown)
    nodes = []
    # Loop over each block:
    for block in blocks:
        # Determine the type of block
        block_type = block_to_block_type(block)
        nodes.append(block_node_to_html_node(block_type, block))
    return nodes

def block_node_to_html_node(block_type, block):
    if block_type == BlockType.PARAGRAPH.value:
        return ParentNode("p", text_to_children(block))
    elif block_type == BlockType.HEADING.value:
        return convert_heading(block)
    elif block_type == BlockType.CODE.value:
        '''
        return ParentNode("pre", 
                          ParentNode("code", convert_code_block(block))
        )
        '''
        return ParentNode("code", convert_code_block(block))
    elif block_type == BlockType.QUOTE.value:
        return ParentNode("blockquote", text_to_children(block))
    elif block_type == BlockType.LIST_UNORDERED.value:
        return ParentNode("ul", split_list(block))
    elif block_type == BlockType.LIST_ORDERED.value:
        return ParentNode("ol", split_list(block))
    else:
        raise ValueError("Invalid block type")

def convert_code_block(block):
    filtered_lines = []

    for line in block.splitlines():
        if line != "```":
            filtered_lines.append(line)
    text = "\n".join(filtered_lines)

    return text_to_children(text)

def convert_heading(block):
    split_heading = block.split(" ",1)
    tag = f"h{len(split_heading[0])}"
    text = split_heading[1]
    return ParentNode(tag, text_to_children(text))

def split_list(block):
    nodes = []
    for line in block.splitlines():
        text = line.split(" ",1)[1]
        nodes.append(ParentNode("li", text_to_children(text)))
    return nodes

def text_to_children(block):
    text_nodes = text_to_textnodes(block)
    leaf_nodes = []
    for node in text_nodes:
        leaf_nodes.append(node.text_node_to_html_node())
    return leaf_nodes
