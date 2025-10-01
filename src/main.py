import os
import shutil
from copy_static import copy_static_to_public
from generate_pages import generate_pages_recursive

def main():
    public_dir = "public"
    content_dir = "content"
    template_path = "template.html"

    # Clean public/ (fresh build)
    if os.path.exists(public_dir):
        print(f"[wipe] removing {public_dir}")
        shutil.rmtree(public_dir)

    # Copy static -> public
    copy_static_to_public("static", public_dir)

    # Generate ALL pages from content recursively
    generate_pages_recursive(content_dir, template_path, public_dir)

if __name__ == "__main__":
    main()
