import os
from markdown_blocks import markdown_to_html_node

def extract_title(markdown):
    blocks = markdown.split("\n")
    for block in blocks:
        if block.startswith("# "):
            return block.strip("# ")
    raise Exception("ERROR: No header found in markdown")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as f:
        markdown = f.read()
    with open(template_path) as f:
        template = f.read()
    template = template.replace("{{ Title }}", extract_title(markdown))
    template = template.replace("{{ Content }}", markdown_to_html_node(markdown).to_html())
    with open(dest_path, "w") as f:
        f.write(template)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for item in os.listdir(dir_path_content):
        item_path = os.path.join(dir_path_content, item)
        dest_path = os.path.join(dest_dir_path, item)
        if os.path.isfile(item_path):
            dest_path = dest_path.replace(".md", ".html")
            generate_page(item_path, template_path, dest_path)
        else:
            if not os.path.isdir(dest_path):
                os.mkdir(dest_path)
            generate_pages_recursive(item_path, template_path, dest_path)
