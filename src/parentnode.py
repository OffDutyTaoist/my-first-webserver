from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        """
        Parent nodes must have:
        - tag: str (required; cannot be None)
        - children: list[HTMLNode] (required; should not be empty)
        - value: not used for ParentNode
        - props: dict[str, str] | None
        """
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        """
        Render as HTML:
        - If tag is None -> ValueError (distinct message)
        - If children is None or empty -> ValueError (distinct message)
        - Else -> <tag props>children_html</tag>
        """
        if self.tag is None:
            raise ValueError("ParentNode must have a tag")
        if not self.children:
            # Covers None or empty list
            raise ValueError("ParentNode must have at least one child")

        inner = []
        for child in self.children:
            # Each child is responsible for its own rendering
            inner.append(child.to_html())
        inner_html = "".join(inner)

        return f"<{self.tag}{self.props_to_html()}>{inner_html}</{self.tag}>"
