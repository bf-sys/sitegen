from enum import Enum
from htmlnode import *
from splitter import *
from blocks import *
from textnode import *

def markdown_to_html_node(markdown) -> HTMLNode:
    block_list = markdown_to_blocks(markdown)
    html_parents_list = []
    for item in block_list:
        match block_to_block_type(item):
            case BlockType.PARAGRAPH:
               #children = text_to_children(item)
               lines = [line.strip() for line in item.split("\n")]
               paragraph = " ".join(lines)
               children = text_to_children(paragraph)
               node = ParentNode(tag="p", children=children)
               html_parents_list.append(node)
            case BlockType.HEADING1:
               children = text_to_children(item)
               node = ParentNode(tag="h1", children=children)
               html_parents_list.append(node)
            case BlockType.HEADING2:
               children = text_to_children(item)
               node = ParentNode(tag="h2", children=children)
               html_parents_list.append(node)
            case BlockType.HEADING3:
               children = text_to_children(item)
               node = ParentNode(tag="h3", children=children)
               html_parents_list.append(node)
            case BlockType.HEADING4:
               children = text_to_children(item)
               node = ParentNode(tag="h4", children=children)
               html_parents_list.append(node)
            case BlockType.HEADING5:
               children = text_to_children(item)
               node = ParentNode(tag="h5", children=children)
               html_parents_list.append(node)
            case BlockType.HEADING6:
               children = text_to_children(item)
               node = ParentNode(tag="h6", children=children)
               html_parents_list.append(node)
            case BlockType.CODE:
                lines = [line.strip("```\n ") for line in item.split("\n")]
                paragraph = "\n".join(lines)
                node = TextNode(paragraph, TextType.CODE)
                node.text = node.text.lstrip("\n")
                code_node = text_node_to_html_node(node)
                code_parent = ParentNode(tag="pre", children=[code_node])
                html_parents_list.append(code_parent)
            case BlockType.QUOTE:
                children = text_to_children(item)
                node = ParentNode(tag="blockquote", children=children)
                html_parents_list.append(node)
            case BlockType.U_LIST:
                list_temp = [line.strip() for line in item.split("\n")]
                new_list = [string[2:] for string in list_temp]
                children = []
                for str in new_list:
                    children.append(ParentNode(tag="li", children=text_to_children(str)))
                node = ParentNode(tag="ul", children=children)
                html_parents_list.append(node)
            case BlockType.O_LIST:
                list_temp = [line.strip() for line in item.split("\n")]
                new_list = [string.split(". ",1)[1] for string in list_temp]
                children = []
                for str in new_list:
                    children.append(ParentNode(tag="li", children=text_to_children(str)))
                node = ParentNode(tag="ol", children=children)
                html_parents_list.append(node)
            case _:
                raise Exception("Invalid BlockType")
        
    grand_parent_node = ParentNode(tag="div", children=html_parents_list)
        
    return grand_parent_node
           
        # Determine the type of block [use Enum match/case] create a new HTMLNode with proper data [as part of each case]
        
        # Assign the proper child HTMLNode objects to the block node. 
       
       # The "code" block is a bit of a special case: it should not do any inline markdown parsing of its children. 
        # I didn't use my text_to_children function for this block type, I manually made a TextNode and used text_node_to_html_node.   

        #Male all the block nodes children under a single parent HTML node (which should just be a div) and return it.


def text_to_children(text) -> list[HTMLNode]:
    textnode_list = text_to_textnode(text)
    htmlnode_list = []
    for item in textnode_list:
        htmlnode_list.append(text_node_to_html_node(item))
    return htmlnode_list

       
      
        # I created a shared text_to_children(text) function that works for all block types. 
        # It takes a string of text and returns a list of HTMLNodes that represent the inline 
        #   markdown using previously created functions (think TextNode -> HTMLNode).
        
        