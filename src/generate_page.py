import os
from markdown_to_html_node import markdown_to_html_node
from extract_title import extract_title

def _normalize_basepath(basepath: str) -> str:
    if not basepath:
        return "/"
    if not basepath.startswith("/"):
        basepath = "/" + basepath
    if not basepath.endswith("/"):
        basepath += "/"
    return basepath

def generate_page(from_path: str, template_path: str, dest_path: str, basepath: str = "/"):
    basepath = _normalize_basepath(basepath)
    print(f"Generating page from {from_path} to {dest_path} using {template_path} (basepath={basepath})")

    with open(from_path, "r", encoding="utf-8") as f:
        markdown = f.read()

    with open(template_path, "r", encoding="utf-8") as f:
        template = f.read()

    # Convert markdown -> HTML string
    html_node = markdown_to_html_node(markdown)
    html_content = html_node.to_html()

    # Title
    title = extract_title(markdown)

    # Fill template
    full_html = template.replace("{{ Title }}", title).replace("{{ Content }}", html_content)

    # Rebase absolute references to the configured basepath
    # Only rebases links written like href="/..." and src="/..."
    full_html = full_html.replace('href="/', f'href="{basepath}')
    full_html = full_html.replace('src="/',  f'src="{basepath}')

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(full_html)

    print(f"[done] Wrote {dest_path}")
