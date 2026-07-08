from textnode import *
from htmlnode import *
from splitter import *
from blocks import *


def main():
    #test_text = "This is some **anchor** text"
    #test_type = TextType.TEXT
    #test_url = "https://boot.dev"
    
    
    #testobject = TextNode(test_text, test_type)
    #print(testobject)
    #split_test = split_nodes_delimiter([testobject], "**", TextType.BOLD)
    #print(split_test)

    # node = TextNode(
    #     "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
    #     TextType.TEXT,
    # )
    # new_nodes = split_nodes_image([node])
    # print(*new_nodes, sep='\n')

    # node = TextNode(
    #     "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
    #     TextType.TEXT,
    # )
    # new_nodes = split_nodes_link([node])
    # print(*new_nodes, sep='\n')
    # string = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)."
    # new_string = text_to_textnode(string)
    # print(*new_string, sep='\n')
#     md = """
# This is **bolded** paragraph

# This is another paragraph with _italic_ text and `code` here
# This is the same paragraph on a new line

# - This is a list
# - with items
# """

#     blocks = markdown_to_blocks(md)
#     print(blocks)
    #print(*blocks, sep='\n')
    md = """
This is a paragraph.

# This is a heading.

## Heading 2.

### Heading 3.

#### Heading 4.

##### Heading 5.

###### Heading 6.

```
This is code
```

> This is a quote
>block that keeps
> going

- Bullet points!
- We love unordered lists!
- because they are awesome

1. Ordered lists are better
2. Because they have numbers
3. And numbers are awesomer


"""
    blocks = markdown_to_blocks(md)
    type_list = []
    for item in blocks:
            type_list.append(block_to_block_type(item))
    print(type_list)



if __name__ == "__main__":
    main()

