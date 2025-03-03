from textnode import TextNode, TextType


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
