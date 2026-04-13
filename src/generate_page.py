import os
from markdown_blocks import markdown_to_html_node, extract_title

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as f:
        markdown = f.read()
    with open(template_path) as f:
        template = f.read()
    template = template.replace("{{ Title }}", extract_title(markdown))
    template = template.replace("{{ Content }}", markdown_to_html_node(markdown).to_html())
    
    #if not os.path.isdir(os.path.dirname(dest_path)) and dest_path:
       #os.makedirs(os.path.dirname(dest_path)) 
    with open(dest_path, "w") as f:
        f.write(template)

#generate_page("./test_markdown", "./template.html", "./public/index.html")