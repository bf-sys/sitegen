from enum import Enum
import re


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    U_LIST = "unordered list"
    O_LIST = "ordered list"


def block_to_block_type(block: str) -> BlockType:
    if re.match(r"#{1,6}\s.", block):
        return BlockType.HEADING
    elif block.startswith("```\n") and block.endswith("```"):
        return BlockType.CODE
    elif re.match(r"\>", block):
        temp_block = block.split("\n")
        if [s for s in temp_block if re.match(r"\>", s)]:
            return BlockType.QUOTE
    elif re.match(r"\-\s.", block):
        temp_block = block.split("\n")
        if [s for s in temp_block if re.match(r"\-\s.", s)]:
            return BlockType.U_LIST
    elif re.match(r"\d+\.\s.", block):
        temp_block = block.split("\n")
        if [s for s in temp_block if re.match(r"\d+\.\s.", s)]:
            return BlockType.O_LIST
    else:
        return BlockType.PARAGRAPH


def markdown_to_blocks(markdown) -> list[str]:
    block_list = markdown.split("\n\n")
    cleaned_blocks = []
    for item in block_list:
        stripped_item = item.strip()
        if stripped_item != "":
            cleaned_blocks.append(stripped_item)
    return cleaned_blocks      