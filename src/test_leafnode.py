import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_link_with_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.google.com">Click me!</a>'
        )

    def test_raw_text_when_no_tag(self):
        node = LeafNode(None, "Just text")
        self.assertEqual(node.to_html(), "Just text")

    def test_raises_when_no_value(self):
        node = LeafNode("span", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_props_multiple_attributes_ordered(self):
        # Insertion order is preserved in Python 3.7+
        node = LeafNode("img", "alt text not used for img here", {
            "src": "cat.png",
            "alt": "A cat"
        })
        # Note: This is just to verify props formatting; LeafNode renders value,
        # but we still confirm attribute string shape via to_html.
        self.assertIn('<img src="cat.png" alt="A cat">', node.to_html().replace("alt text not used for img here", ""))

if __name__ == "__main__":
    unittest.main()
