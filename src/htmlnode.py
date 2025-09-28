class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        """
        tag: str | None
        value: str | None
        children: list[HTMLNode] | None
        props: dict[str, str] | None
        """
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        """Will be implemented by subclasses."""
        raise NotImplementedError

    def props_to_html(self):
        """
        Convert props dict to a leading-space-prefixed string of HTML attributes.
        Example: {'href':'x','target':'_blank'} -> ' href="x" target="_blank"'
        """
        if not self.props:
            return ""
        parts = [f'{k}="{v}"' for k, v in self.props.items()]
        return " " + " ".join(parts)

    def __repr__(self):
        return (
            f"HTMLNode(tag={self.tag!r}, value={self.value!r}, "
            f"children={self.children!r}, props={self.props!r})"
        )
