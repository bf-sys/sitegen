from textnode import *
from htmlnode import *
from splitter import *
from blocks import *
from blocktohtml import *


def main():
    md = """
    1. here is an ordered list
    2. because I want to
    3. watch this break too
    """
    node1 = markdown_to_blocks(md)
    node = markdown_to_html_node(md)
    html = node.to_html()
    print(f"Node = {node}\n")
    print(f"html = {html}\n")
    print(f"blocks = {node1}")


if __name__ == "__main__":
    main()

