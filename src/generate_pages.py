import os
from generate_page import generate_page

def generate_pages_recursive(dir_path_content: str, template_path: str, dest_dir_path: str):
    """
    Recursively walk `dir_path_content`, and for each *.md file found,
    generate an HTML file into the parallel path under `dest_dir_path`,
    using `template_path`.

    Examples:
      content/index.md            -> public/index.html
      content/blog/tom/index.md   -> public/blog/tom/index.html
      content/blog/post.md        -> public/blog/post.html
    """
    if not os.path.isdir(dir_path_content):
        raise ValueError(f"Content path does not exist or is not a directory: {dir_path_content}")

    for root, dirs, files in os.walk(dir_path_content):
        for filename in files:
            if not filename.lower().endswith(".md"):
                continue

            src_md_path = os.path.join(root, filename)
            # Rel path from content root
            rel_path = os.path.relpath(src_md_path, dir_path_content)

            # Compute destination path in public with .html extension
            rel_no_ext, _ = os.path.splitext(rel_path)  # remove .md
            dest_html_path = os.path.join(dest_dir_path, rel_no_ext + ".html")

            # Ensure destination directory exists
            os.makedirs(os.path.dirname(dest_html_path), exist_ok=True)

            print(f"[page] {src_md_path} -> {dest_html_path}")
            generate_page(src_md_path, template_path, dest_html_path)
