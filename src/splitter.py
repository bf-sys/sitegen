from htmlnode import *
from textnode import *
import re

def verify_markdown_tags(text, opening_tag, closing_tag):
    pattern = re.escape(opening_tag) + r'.*?' + re.escape(closing_tag)
    return bool(re.search(pattern, text))


def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes = []
    for item in old_nodes:
        if item.text_type != TextType.TEXT:
            new_nodes.append(item)
        elif delimiter not in item.text:
            raise Exception(f"Delimiter: {delimiter} does not exist in the string")
        elif not verify_markdown_tags(item.text, delimiter, delimiter):
            raise Exception(f"Invalid Markdown syntax: {delimiter} needs to open and close")
        else:
            temp_nodes = item.text.split(delimiter)
            for index, value in enumerate(temp_nodes):
                if index % 2 == 0:
                    new_nodes.append(TextNode(value, TextType.TEXT))
                else:
                    new_nodes.append(TextNode(value, text_type))
    return new_nodes


def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for old_node in old_nodes:
        if not old_node.text_type.TEXT:
            new_nodes.append(old_node)
            continue
            
        images = extract_markdown_images(old_node.text)
        if not images:
            new_nodes.append(old_node)
            continue
            
        remaining_text = old_node.text
        for alt_text, url in images:
            # Reconstruct the image syntax to split exactly by the image
            section = f"![{alt_text}]({url})"
            parts = remaining_text.split(section, 1)
            
            if parts[0]:
                new_nodes.append(TextNode(parts[0], TextType.TEXT))
                
            new_nodes.append(TextNode(alt_text, TextType.IMAGE, url))
            remaining_text = parts[1]
            
        if remaining_text:
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))
            
    return new_nodes




def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
            
        links = extract_markdown_links(old_node.text)
        if not links:
            new_nodes.append(old_node)
            continue
            
        remaining_text = old_node.text
        for anchor_text, url in links:
            # Reconstruct the exact markdown link syntax to split by
            section = f"[{anchor_text}]({url})"
            parts = remaining_text.split(section, 1)
            
            # Append the text before the link if it's not empty
            if parts[0] != "":
                new_nodes.append(TextNode(parts[0], TextType.TEXT))
                
            # Append the link node using the anchor text as the node's text
            new_nodes.append(TextNode(anchor_text, TextType.LINK, url))
            remaining_text = parts[1]
            
        # Append any remaining text after the final link
        if remaining_text != "":
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))
    print(f"New Nodes = {new_nodes}")            
    return new_nodes

def text_to_textnode(text: str) -> list[TextNode]:
    if not text:
        raise Exception("Text string required")  # Added quotes

    new_list: list[TextNode] = []
    append_text = TextNode(text, TextType.TEXT)
    new_list.append(append_text)
    working_list = []

    #for bold
    working_list.extend(split_nodes_delimiter(new_list, "**", TextType.BOLD))
    temp = TextNode(working_list.pop().text, TextType.TEXT)
    new_list = [temp]
    
    #for italic
    working_list.extend(split_nodes_delimiter(new_list, "_", TextType.ITALIC))
    temp = TextNode(working_list.pop().text, TextType.TEXT)
    new_list = [temp]
    
    # for code
    working_list.extend(split_nodes_delimiter(new_list, "`", TextType.CODE))
    temp = TextNode(working_list.pop().text, TextType.TEXT)
    new_list = [temp]
    
    # # for image
    working_list.extend(split_nodes_image(new_list))
    temp = TextNode(working_list.pop().text, TextType.TEXT)
    new_list = [temp]
    
    # for link:
    working_list.extend(split_nodes_link(new_list))
    if working_list[-1].text_type != TextType.LINK:
        temp = TextNode(working_list.pop().text, TextType.TEXT)
        new_list = [temp]
        
        if new_list:
            working_list.extend(new_list)
            
    return working_list
        
        