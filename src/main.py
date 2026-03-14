from copyfiles import copy_static_to_public
from generatepage import generate_page, generate_pages_recursive
import sys

def main():
    args = sys.argv
    base_path = "/"

    if len(args) > 1:
        base_path = args[1]

    copy_static_to_public("./static", "./docs")
    generate_pages_recursive("content/", "template.html", "docs/", base_path)

    

main()
