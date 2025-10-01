import os
import sys
import shutil
from copy_static import copy_static_to_public
from generate_pages import generate_pages_recursive

def normalize_basepath(p: str) -> str:
    # Default and normalization:
    # "" or None -> "/"
    # ensure leading "/" and a trailing "/"
    if not p:
        return "/"
    if not p.startswith("/"):
        p = "/" + p
    if not p.endswith("/"):
        p = p + "/"
    return p

def main():
    # 1) Basepath from CLI arg (default "/")
    basepath = normalize_basepath(sys.argv[1]) if len(sys.argv) >= 2 else "/"

    # 2) Directories for local dev
    output_dir = "docs"         # <— build into docs for GitHub Pages
    content_dir = "content"
    template_path = "template.html"

    # 3) Clean output
    if os.path.exists(output_dir):
        print(f"[wipe] removing {output_dir}")
        shutil.rmtree(output_dir)

    # 4) Copy static -> docs
    copy_static_to_public("static", output_dir)

    # 5) Generate all pages recursively with basepath
    generate_pages_recursive(content_dir, template_path, output_dir, basepath)

if __name__ == "__main__":
    main()
