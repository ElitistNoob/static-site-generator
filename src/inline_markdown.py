from textnode import TextNode, TextType
import re


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    node_list = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            node_list.append(node)
            continue

        node_text = node.text.split(delimiter)
        if len(node_text) % 2 == 0:
            raise Exception(
                f"Invalid Markdown: expected matching closing {delimiter}"
            )

        for i in range(len(node_text)):
            if node_text[i] == "":
                continue

            if i % 2 == 0:
                node_list.append(
                    TextNode(node_text[i], TextType.TEXT, None)
                )
            else:
                node_list.append(
                    TextNode(node_text[i], text_type, None)
                )

    return node_list


def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches


def extract_markdown_links(text):
    matches = re.findall(
        r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text
    )
    return matches


def split_nodes_image(old_nodes):
    new_nodes = []

    node_text = split_nodes_by_type(
        old_nodes, TextType.IMAGE, extract_markdown_images
    )
    new_nodes.extend(node_text)

    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []

    node_text = split_nodes_by_type(
        old_nodes, TextType.LINK, extract_markdown_links
    )
    new_nodes.extend(node_text)

    return new_nodes


def split_nodes_by_type(old_nodes, node_type, extractor):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        items = extractor(node.text)
        if len(items) == 0:
            new_nodes.append(node)
            continue

        text = node.text
        for item in items:
            delimiter = (
                f"![{item[0]}]({item[1]})"
                if node_type == TextType.IMAGE
                else f"[{item[0]}]({item[1]})"
            )
            section = text.split(delimiter, 1)

            if len(section) != 2:
                raise ValueError("Invalid Markdown")

            if section[0] != "":
                new_nodes.append(
                    TextNode(section[0], TextType.TEXT)
                )
            new_nodes.append(
                TextNode(item[0], node_type, item[1])
            )
            text = section[1]

        if text != "":
            new_nodes.append(TextNode(text, TextType.TEXT))

    return new_nodes


def text_to_textnodes(text):
    text_node = [TextNode(text, TextType.TEXT)]
    text_node = split_nodes_delimiter(
        text_node, "`", TextType.CODE
    )
    text_node = split_nodes_delimiter(
        text_node, "**", TextType.BOLD
    )
    text_node = split_nodes_delimiter(
        text_node, "_", TextType.ITALIC
    )
    text_node = split_nodes_image(text_node)
    text_node = split_nodes_link(text_node)
    return text_node
