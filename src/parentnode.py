from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("Invalid HTML: Tag Needed")

        if self.children == None:
            raise ValueError(
                "Invalid Parent Node: children needed"
            )

        return f"<{self.tag}>{"".join([node.to_html() for node in self.children])}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
