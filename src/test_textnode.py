import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq_different_text(self):
        a = TextNode("hello", TextType.TEXT)
        b = TextNode("hello!", TextType.TEXT)
        self.assertNotEqual(a, b)

    def test_not_eq_different_type(self):
        a = TextNode("same", TextType.TEXT)
        b = TextNode("same", TextType.BOLD)
        self.assertNotEqual(a, b)

    def test_not_eq_different_url(self):
        a = TextNode("link text", TextType.LINK, "https://a.example")
        b = TextNode("link text", TextType.LINK, "https://b.example")
        self.assertNotEqual(a, b)

    def test_default_url_is_none_and_equal(self):
        a = TextNode("plain", TextType.TEXT)            # url defaults to None
        b = TextNode("plain", TextType.TEXT, None)
        self.assertEqual(a, b)

    def test_repr_format(self):
        node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
        self.assertEqual(
            repr(node),
            "TextNode(This is some anchor text, link, https://www.boot.dev)"
        )

    def test_not_equal_to_non_textnode(self):
        node = TextNode("x", TextType.CODE)
        self.assertNotEqual(node, ("x", "code", None))

if __name__ == "__main__":
    unittest.main()
