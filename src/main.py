from helpers import clear_dir, copy_from_dir_to_dir, generate_pages_recursive
import os
import sys

def main():

    args = sys.argv
    if len(args) > 1:
        if args[1] != "":
            basepath = args[1]
        else:
            basepath = "/"
    else:
        basepath = "/"

    static_src = "static/"
    content_path = "content/"
    template_path = "template.html"
    dest_path = "docs/"

    clear_dir(dest_path)

    copy_from_dir_to_dir(src=static_src, dest=dest_path)

    generate_pages_recursive(dir_path_content=content_path, template_path=template_path, dest_dir_path=dest_path, basepath=basepath)

main()