from textnode import TextNode, TextType

def main():
    italic_link = TextNode("Dummy Text", TextType.ITALIC, "https://www.jeuxvideo.com")
    print(italic_link)

if __name__ == "__main__":
    main()
