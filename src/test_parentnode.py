import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_mixed_children_including_raw_text(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_parent_with_props(self):
        node = ParentNode(
            "ul",
            [LeafNode("li", "a"), LeafNode("li", "b")],
            props={"class": "list", "data-role": "menu"},
        )
        self.assertEqual(
            node.to_html(),
            '<ul class="list" data-role="menu"><li>a</li><li>b</li></ul>',
        )

    def test_raises_when_no_tag(self):
        child = LeafNode("span", "x")
        parent = ParentNode(None, [child])
        with self.assertRaises(ValueError):
            parent.to_html()

    def test_raises_when_no_children(self):
        parent = ParentNode("div", [])
        with self.assertRaises(ValueError):
            parent.to_html()

    def test_deeply_nested(self):
        # <section><div><p><em>hi</em></p></div></section>
        n = ParentNode(
            "section",
            [
                ParentNode(
                    "div",
                    [ParentNode("p", [LeafNode("em", "hi")])]
                )
            ],
        )
        self.assertEqual(
            n.to_html(),
            "<section><div><p><em>hi</em></p></div></section>",
        )

if __name__ == "__main__":
    unittest.main()
