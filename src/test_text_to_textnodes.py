import unittest
from textnode import TextNode, TextType
from text_to_textnodes import text_to_textnodes

class TestTextToTextNodes(unittest.TestCase):
    def test_example_from_assignment(self):
        text = (
            "This is **text** with an _italic_ word and a `code block` "
            "and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) "
            "and a [link](https://boot.dev)"
        )
        nodes = text_to_textnodes(text)
        self.assertEqual(
            nodes,
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
        )

    def test_no_markup(self):
        nodes = text_to_textnodes("just plain text")
        self.assertEqual(nodes, [TextNode("just plain text", TextType.TEXT)])

    def test_multiple_delimiters(self):
        text = "**bold** _it_ `code` **b2**"
        nodes = text_to_textnodes(text)
        self.assertEqual(
            nodes,
            [
                TextNode("bold", TextType.BOLD),
                TextNode(" ", TextType.TEXT),
                TextNode("it", TextType.ITALIC),
                TextNode(" ", TextType.TEXT),
                TextNode("code", TextType.CODE),
                TextNode(" ", TextType.TEXT),
                TextNode("b2", TextType.BOLD),
            ],
        )


    def test_multiple_delimiters_skip_empties(self):
        # If your delimiter splitter skips empty chunks, this variant is more appropriate:
        text = "**bold** _it_ `code` **b2**"
        nodes = text_to_textnodes(text)
        # filter out any empty TEXT nodes to make the assertion stable across implementations
        filtered = [n for n in nodes if not (n.text_type is TextType.TEXT and n.text == "")]
        self.assertEqual(
            filtered,
            [
                TextNode("bold", TextType.BOLD),
                TextNode(" ", TextType.TEXT),
                TextNode("it", TextType.ITALIC),
                TextNode(" ", TextType.TEXT),
                TextNode("code", TextType.CODE),
                TextNode(" ", TextType.TEXT),
                TextNode("b2", TextType.BOLD),
            ],
        )

    def test_code_protects_inner_markup(self):
        # underscores and asterisks inside code should remain untouched by our order
        text = "`__not bold__ and _not italic_` outside"
        nodes = text_to_textnodes(text)
        self.assertEqual(
            nodes,
            [
                TextNode("__not bold__ and _not italic_", TextType.CODE),
                TextNode(" outside", TextType.TEXT),
            ],
        )

if __name__ == "__main__":
    unittest.main()
