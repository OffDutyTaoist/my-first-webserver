import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_basic(self):
        node = HTMLNode(
            tag="a",
            value=None,
            children=[],
            props={"href": "https://www.google.com", "target": "_blank"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' href="https://www.google.com" target="_blank"'
        )

    def test_props_to_html_none_or_empty(self):
        self.assertEqual(HTMLNode(tag="p").props_to_html(), "")
        self.assertEqual(HTMLNode(tag="p", props={}).props_to_html(), "")

    def test_to_html_raises(self):
        node = HTMLNode(tag="p", value="hello")
        with self.assertRaises(NotImplementedError):
            node.to_html()

    def test_constructor_defaults(self):
        node = HTMLNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

    def test_repr_contains_fields(self):
        node = HTMLNode(tag="p", value="hi", children=None, props={"class": "lead"})
        rep = repr(node)
        self.assertIn("tag='p'", rep)
        self.assertIn("value='hi'", rep)
        self.assertIn("props={'class': 'lead'}", rep)

if __name__ == "__main__":
    unittest.main()
