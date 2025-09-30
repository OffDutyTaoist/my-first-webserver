import re
from typing import List

def markdown_to_blocks(markdown: str) -> List[str]:
    """
    Split a full markdown document into logical blocks separated by
    one or more blank lines. Trims leading/trailing whitespace per block
    and removes empty blocks.
    """
    if markdown is None:
        return []

    # Normalize newlines and trim overall
    text = (markdown or "").replace("\r\n", "\n").strip()

    if not text:
        return []

    # Split on two or more newlines (i.e., at least one blank line)
    raw_blocks = re.split(r"\n\s*\n+", text)

    # Strip each block and drop empties
    blocks = [blk.strip() for blk in raw_blocks if blk.strip() != ""]
    return blocks
