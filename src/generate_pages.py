
import os
from generate_page import generate_page

def generate_pages_recursive(dir_path_content: str, template_path: str, dest_dir_path: str, basepath: str = "/"):
    """
    Recursively walk dir_path_content, and for each *.md, render parallel .html under dest_dir_path.
    """
    if not os.path.isdir(dir_path_content):
        raise ValueError(f"Content path does not exist or is not a directory: {dir_path_content}")

    for root, dirs, files in os.walk(dir_path_content):
        for filename in files:
            if not filename.lower().endswith(".md"):
                continue

            src_md_path = os.path.join(root, filename)
            rel_path = os.path.relpath(src_md_path, dir_path_content)
            rel_no_ext, _ = os.path.splitext(rel_path)
            dest_html_path = os.path.join(dest_dir_path, rel_no_ext + ".html")

            os.makedirs(os.path.dirname(dest_html_path), exist_ok=True)
            print(f"[page] {src_md_path} -> {dest_html_path}")
            generate_page(src_md_path, template_path, dest_html_path, basepath)
