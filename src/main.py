from textnode import *
from htmlnode import *
from splitter import *

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
    string = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)."
    new_string = text_to_textnode(string)
    print(*new_string, sep='\n')


if __name__ == "__main__":
    main()

