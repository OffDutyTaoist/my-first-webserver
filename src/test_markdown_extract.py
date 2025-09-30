import unittest
from markdown_extract import extract_markdown_images, extract_markdown_links

class TestMarkdownExtract(unittest.TestCase):
    def test_extract_markdown_images_single(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual(
            [("image", "https://i.imgur.com/zjjcJKZ.png")],
            matches
        )

    def test_extract_markdown_images_multiple(self):
        text = (
            "Pics: ![rick roll](https://i.imgur.com/aKaOqIh.gif) "
            "and also ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        )
        matches = extract_markdown_images(text)
        self.assertListEqual(
            [
                ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
                ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg"),
            ],
            matches,
        )

    def test_extract_markdown_images_empty_alt(self):
        matches = extract_markdown_images("![ ](https://example.com/x.png) and ![](https://example.com/y.png)")
        self.assertListEqual(
            [(" ", "https://example.com/x.png"), ("", "https://example.com/y.png")],
            matches
        )

    def test_extract_markdown_links_single(self):
        matches = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev)"
        )
        self.assertListEqual(
            [("to boot dev", "https://www.boot.dev")],
            matches
        )

    def test_extract_markdown_links_multiple(self):
        text = (
            "Links: [to boot dev](https://www.boot.dev) and "
            "[to youtube](https://www.youtube.com/@bootdotdev)"
        )
        matches = extract_markdown_links(text)
        self.assertListEqual(
            [
                ("to boot dev", "https://www.boot.dev"),
                ("to youtube", "https://www.youtube.com/@bootdotdev"),
            ],
            matches
        )

    def test_links_do_not_capture_images(self):
        text = "Look ![alt](https://x.png) and [site](https://example.com)"
        links = extract_markdown_links(text)
        images = extract_markdown_images(text)
        self.assertListEqual([("site", "https://example.com")], links)
        self.assertListEqual([("alt", "https://x.png")], images)

    def test_no_matches(self):
        self.assertListEqual([], extract_markdown_images("no markdown here"))
        self.assertListEqual([], extract_markdown_links("no markdown here"))

if __name__ == "__main__":
    unittest.main()
