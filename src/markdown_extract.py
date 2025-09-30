import re
from typing import List, Tuple

# Matches: ![alt text](https://url)
_IMAGE_RE = re.compile(r'!\[([^\]]*)\]\(([^)\s]+)\)')

# Matches links but NOT images:
# Use negative lookbehind to ensure there's no '!' immediately before '['
# Matches: [anchor text](https://url)
_LINK_RE = re.compile(r'(?<!!)\[([^\]]+)\]\(([^)\s]+)\)')

def extract_markdown_images(text: str) -> List[Tuple[str, str]]:
    """
    Return list of (alt_text, url) tuples for Markdown images.
    Example: "![alt](https://x)" -> [("alt", "https://x")]
    """
    return [(m.group(1), m.group(2)) for m in _IMAGE_RE.finditer(text or "")]

def extract_markdown_links(text: str) -> List[Tuple[str, str]]:
    """
    Return list of (anchor_text, url) tuples for Markdown links (not images).
    Example: "[boot](https://x)" -> [("boot", "https://x")]
    """
    return [(m.group(1), m.group(2)) for m in _LINK_RE.finditer(text or "")]
