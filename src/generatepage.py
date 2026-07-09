import re
import os
import sys
from pathlib import Path
from blocktohtml import *



def extract_title(markdown: str) -> str:
    text_lines = markdown.splitlines()
    for line in text_lines:
        if re.match(r"\#\s", line):
            return line.strip("# ")
    raise Exception("No H1 header (title) found")


def generate_page(from_path: Path, template_path: Path, dest_path: Path, base_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    for file in from_path.iterdir():
        if file.name.endswith(".md"):
            md_file = open(file, 'r')
            markdown = md_file.read()
    
    
    template_name = Path(template_path / "template.html")
    f_template = open(template_name)
    template = f_template.read()


    html = markdown_to_html_node(markdown)
    title = extract_title(markdown)

    string_html = html.to_html()

    
    page_title = template.replace("{{ Title }}", title)
    page_content = page_title.replace("{{ Content }}", string_html)
    if len(sys.argv) > 1:
        page_body = page_content.replace('href="/', f'href="/{base_path}')
    else:
        page_body = page_content
    
    file_name = Path(dest_path / "index.html")
  
    html_file = open(file_name, 'w')
    html_file.write(page_body)

    return page_body

def generate_page_recursively(dir_path_content: Path, template_path: Path, dest_dir_path: Path, base_path):
    for file in dir_path_content.iterdir():
        if file.name.endswith(".md"):
            print(f"Generating page from {dir_path_content} to {dest_dir_path} using {template_path}")
            md_file = open(file, 'r')
            markdown = md_file.read()

            template_name = Path(template_path / "template.html")
            f_template = open(template_name)
            template = f_template.read()

            html = markdown_to_html_node(markdown)
            title = extract_title(markdown)

            string_html = html.to_html()

    
            page_title = template.replace("{{ Title }}", title)
            page_content = page_title.replace("{{ Content }}", string_html)
            if len(sys.argv) > 1:
                page_body_temp = page_content.replace('href="/', f'href="{base_path}')
                page_body = page_body_temp.replace('src="/', f'href="{base_path}')
            else:
                page_body = page_content

            file_name = Path(dest_dir_path / "index.html")
  
            html_file = open(file_name, 'w')
            html_file.write(page_body)
        elif file.is_dir():
            dir_name = file.name
            current_dest_folder = Path(dest_dir_path / f"{dir_name}")
            current_content_folder = Path(file)
            print(f"Creating directory - {current_dest_folder}")
            os.mkdir(current_dest_folder)
            generate_page_recursively(current_content_folder, template_path, current_dest_folder, base_path)