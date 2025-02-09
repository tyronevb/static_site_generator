from textnode import TextNode, TextType

def main():
    text_node = TextNode(text="This is a text node",
                         text_type=TextType.BOLD_TEXT,
                         url="https://www.boot.dev")
    
    print(text_node)
    
main()
