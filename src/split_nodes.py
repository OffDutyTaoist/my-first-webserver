import re
from textnode import TextNode, TextType

# Reuse-friendly regexes for markdown images/links
_IMAGE_RE = re.compile(r'!\[([^\]]*)\]\(([^)\s]+)\)')
_LINK_RE = re.compile(r'(?<!!)\[([^\]]+)\]\(([^)\s]+)\)')

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    if not delimiter:
        raise ValueError("Delimiter cannot be empty")

    new_nodes = []
    for node in old_nodes:
        if not isinstance(node, TextNode) or node.text_type is not TextType.TEXT:
            new_nodes.append(node)
            continue

        text = node.text
        parts = text.split(delimiter)

        if len(parts) == 1:
            new_nodes.append(node)  # preserve identity when no delimiter exists
            continue

        if len(parts) % 2 == 0:
            raise ValueError(f"Unmatched delimiter: {delimiter}")

        for i, chunk in enumerate(parts):
            if not chunk:
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(chunk, TextType.TEXT))
            else:
                new_nodes.append(TextNode(chunk, text_type))

    return new_nodes

def _split_textnode_by_regex(node: TextNode, pattern: re.Pattern, make_match_node):
    """
    Split a TEXT node by regex matches. Non-TEXT nodes are not expected here.
    Returns a list of TextNodes (TEXT around matches + converted match nodes).
    If no matches are found, returns [node] to preserve identity.
    """
    text = node.text or ""
    out = []
    pos = 0
    any_match = False

    for m in pattern.finditer(text):
        any_match = True
        if m.start() > pos:
            out.append(TextNode(text[pos:m.start()], TextType.TEXT))
        out.append(make_match_node(m))
        pos = m.end()

    if not any_match:
        return [node]  # pass-through if no matches

    if pos < len(text):
        out.append(TextNode(text[pos:], TextType.TEXT))

    return out

def split_nodes_image(old_nodes):
    """
    Scan TEXT nodes for markdown images and split into TEXT/IMAGE nodes.
    Non-TEXT nodes pass through unchanged.
    """
    new_nodes = []
    for node in old_nodes:
        if not isinstance(node, TextNode) or node.text_type is not TextType.TEXT:
            new_nodes.append(node)
            continue

        parts = _split_textnode_by_regex(
            node,
            _IMAGE_RE,
            lambda m: TextNode(m.group(1), TextType.IMAGE, m.group(2)),
        )
        new_nodes.extend(parts)
    return new_nodes

def split_nodes_link(old_nodes):
    """
    Scan TEXT nodes for markdown links and split into TEXT/LINK nodes.
    Non-TEXT nodes pass through unchanged.
    """
    new_nodes = []
    for node in old_nodes:
        if not isinstance(node, TextNode) or node.text_type is not TextType.TEXT:
            new_nodes.append(node)
            continue

        parts = _split_textnode_by_regex(
            node,
            _LINK_RE,
            lambda m: TextNode(m.group(1), TextType.LINK, m.group(2)),
        )
        new_nodes.extend(parts)
    return new_nodes