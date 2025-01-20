from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    LIST_UNORDERED = "unordered list"
    LIST_ORDERED = "ordered list"

def markdown_to_blocks(markdown):
    blocks = markdown.splitlines()
    result = []
    for block in blocks:
        stripped_block = block.strip()
        if stripped_block != "":
            result.append(stripped_block)
    return result

def block_to_block_type(block):
    if block.startswith("#"):
        hash_count = 0
        for char in block:
            if char == "#":
                hash_count += 1
            else:
                break
        if hash_count <= 6 and block[hash_count] == " ":
            return BlockType.HEADING.value
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE.value
    if block.startswith(">"):
        for line in block.splitlines():
            if not line.startswith(">"):
                break
        return BlockType.QUOTE.value
    if block.startswith("* ") or block.startswith("- "):
        lines = block.splitlines()
        for line in lines:
            if not (line.startswith("* ") or line.startswith("- ")):
                break
        else:
            return BlockType.LIST_UNORDERED.value
    if block.startswith("1. "):
        lines = enumerate(block.splitlines(), 1)
        for i, line in lines:
            if not line.startswith(f"{i}. "):
                break
        else:
            return BlockType.LIST_ORDERED.value
    
    return BlockType.PARAGRAPH.value