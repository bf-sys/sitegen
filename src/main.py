from textnode import TextNode
from textnode import TextType

def main():
    test_text = "This is some anchor text"
    test_type = TextType.LINK
    test_url = "https://boot.dev"
    
    
    testobject = TextNode(test_text, test_type, test_url)
    print(testobject)






if __name__ == "__main__":
    main()

