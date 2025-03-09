import re
from enum import Enum


class BlockType(Enum):
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    ULIST = "unordered_list"
    OLIST = "ordered_list"
    PARAGRAPH = "paragraph"


def markdown_to_blocks(markdown):
    blocks = []

    for block in markdown.split("\n\n"):
        new_str = []

        if block == "":
            continue

        for str in re.split(r"\n\s+", block):
            if str:
                new_str.append(str.strip())

        blocks.append("\n".join(new_str))

    return blocks


def block_to_block_types(md):
    lines = md.split("\n")
    block_type = None
    valid = True
    expected_order = 1
    inside_code_block = False

    for line in lines:
        if inside_code_block:
            if re.match(r"^(`{3})", line):
                block_type = BlockType.CODE
            continue

        if re.match(r"^(`{3})", line):
            inside_code_block = True
            continue

        if re.match(r"^(#{1,6})\s", line):
            if block_type and block_type != BlockType.HEADING:
                valid = False
            block_type = BlockType.HEADING

        elif re.match(r"^(>)\s", line):
            if block_type and block_type != BlockType.QUOTE:
                valid = False
            block_type = BlockType.QUOTE

        elif re.match(r"^(-)\s", line):
            if block_type and block_type != BlockType.ULIST:
                valid = False
            block_type = BlockType.ULIST

        elif re.match(rf"^({expected_order}\.)\s", line):
            if block_type and block_type != BlockType.OLIST:
                valid = False
            block_type = BlockType.OLIST
            expected_order += 1

        else:
            valid = False

    if not valid or not block_type:
        block_type = BlockType.PARAGRAPH

    return block_type
