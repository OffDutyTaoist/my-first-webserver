import unittest
from markdown_blocks import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_trims_and_removes_empty(self):
        md = "\n\n  First block  \n\n\n  \nSecond block\n\n\n"
        self.assertEqual(markdown_to_blocks(md), ["First block", "Second block"])

    def test_preserves_single_newlines_inside_block(self):
        md = "Line 1\nLine 2\n\nLine 3"
        self.assertEqual(
            markdown_to_blocks(md),
            ["Line 1\nLine 2", "Line 3"]
        )

    def test_handles_none_and_empty(self):
        self.assertEqual(markdown_to_blocks(None), [])
        self.assertEqual(markdown_to_blocks("   \n \n "), [])

    def test_windows_newlines(self):
        md = "A\r\n\r\nB\r\nC"
        self.assertEqual(markdown_to_blocks(md), ["A", "B\nC"])

if __name__ == "__main__":
    unittest.main()
