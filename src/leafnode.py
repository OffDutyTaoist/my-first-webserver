from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        """
        Leaf nodes cannot have children.
        - tag: str | None (None => render raw text)
        - value: str (required; if None, raise in to_html)
        - props: dict[str, str] | None
        """
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        """
        Render as HTML:
        - If value is None -> ValueError
        - If tag is None -> return raw text (value)
        - Else -> <tag props>value</tag>
        """
        if self.value is None:
            raise ValueError("LeafNode must have a value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
