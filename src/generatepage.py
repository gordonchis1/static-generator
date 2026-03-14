import os
import pathlib
from markdowntohtmlnode import markdown_to_html_node
from extracttitle import extract_title

def generate_page(from_path, template_path, dest_path):
    print(f"> Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as file:
        markdown_content = file.read()
    
    with open(template_path, "r") as template_file:
        html_template = template_file.read()
    
    title = extract_title(markdown_content)
    html = markdown_to_html_node(markdown_content).to_html()
    
    result = html_template.replace("{{ Title }}", title).replace("{{ Content }}", html)

    if not os.path.exists(os.path.dirname(dest_path)):
        os.makedirs(os.path.dirname(dest_path))
    
    with open(dest_path, "w") as dest_file:
        dest_file.write(result)
        

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    dir_content_list = os.listdir(dir_path_content)
    for file in dir_content_list:
        content_path = pathlib.Path(os.path.join(dir_path_content, file ))
        if os.path.isdir(content_path.absolute()):
            generate_pages_recursive(content_path.absolute(), template_path, os.path.join(dest_dir_path, file))
            
        else:
            if content_path.suffix == ".md":
                dest_path = pathlib.Path(os.path.join(dest_dir_path, file)).with_suffix(".html")
                generate_page(content_path.absolute(), template_path, dest_path)
            
            

    


    