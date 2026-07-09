import sys
from textnode import *
from htmlnode import *
from splitter import *
from blocks import *
from blocktohtml import *
from filetransfer import *
from generatepage import *
from pathlib import Path



def main():
    if len(sys.argv) > 1:
        sub_dir = Path(sys.argv[1])
        base_path = Path(sys.argv[1])

    else:
        sub_dir = Path.cwd()
        base_path = Path.cwd()
        
    
    public_folder = Path(sub_dir / 'docs')
    static_folder = Path(sub_dir / 'static')
    from_path = Path(sub_dir / 'content')
    template_path = Path(sub_dir)

    delete_public(public_folder)
    copy_static_to_public(static_folder, public_folder)
    #generate_page(from_path, template_path, public_folder, base_path)
    
    generate_page_recursively(from_path, template_path, public_folder, base_path)
    
    # md = "![Image of Glorfindel](/home/bryan/workspace/sitegen/static/images/glorfindel.png)"
    # node = text_to_textnode(md)
    
    # print(f"Text = {md}\nNode = {node}")
    


if __name__ == "__main__":
    main()

