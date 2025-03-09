import re


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
