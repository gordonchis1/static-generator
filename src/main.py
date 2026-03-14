from textnode import TextNode, TextType
from copyfiles import copy_static_to_public
from generatepage import generate_page, generate_pages_recursive

def main():
    copy_static_to_public()
    generate_pages_recursive("content/", "template.html", "public/")

    

main()