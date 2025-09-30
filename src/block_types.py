from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def block_to_block_type(block: str) -> BlockType:
    """
    Determine the markdown block type for a single (stripped) block.
    Rules:
      - Heading: 1–6 '#' then space then text (single line)
      - Code: starts with ``` and ends with ```
      - Quote: every line starts with '>'
      - Unordered list: every line starts with '- ' (dash + space)
      - Ordered list: lines '1. ', '2. ', ... incrementing by 1
      - Otherwise: paragraph
    """
    if not block:
        return BlockType.PARAGRAPH

    # CODE block: fenced with triple backticks
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE

    # HEADING: 1-6 hashes then space then text (single line)
    if "\n" not in block:
        # Count leading #
        i = 0
        while i < len(block) and block[i] == "#":
            i += 1
        if 1 <= i <= 6:
            # Must be followed by a space and at least one char
            if i < len(block) and block[i] == " " and (i + 1) <= len(block) - 1:
                return BlockType.HEADING

    lines = block.split("\n")

    # QUOTE: every line starts with '>' (allow optional space after '>')
    if all(line.startswith(">") for line in lines):
        return BlockType.QUOTE

    # UNORDERED LIST: every line starts with "- " (dash + space)
    if all(
        len(line) >= 3 and line[0] == "-" and line[1] == " " and line[2] != " "
        for line in lines
    ):
        return BlockType.UNORDERED_LIST

    # ORDERED LIST: "1. ", "2. ", ... incrementing
    is_ordered = True
    for idx, line in enumerate(lines, start=1):
        expected_prefix = f"{idx}. "
        if not line.startswith(expected_prefix):
            is_ordered = False
            break
    if is_ordered and len(lines) > 0:
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH
