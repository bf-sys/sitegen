from textnode import *
from htmlnode import *
from splitter import *
from blocks import *
from blocktohtml import *
from filetransfer import *
from generatepage import *
from pathlib import Path



sub_dir = Path.cwd()
public_folder = Path(sub_dir / 'public')
static_folder = Path(sub_dir / 'static')


def main():
    #delete_public(public_folder)
    #copy_static_to_public(static_folder, public_folder)

    md="""
I like dogs
# This is a header
This is not a header
"""
    title = extract_title(md)
    print(title)

if __name__ == "__main__":
    main()

