from helpers import clear_dir, copy_from_dir_to_dir, generate_page
import os

def main():
    static_src = "static/"
    content_path = "content/index.md"
    template_path = "template.html"
    dest_path = "public/index.html"
    dest_dir = os.path.dirname(dest_path)

    clear_dir(dest_dir)

    copy_from_dir_to_dir(src=static_src, dest=dest_dir)

    generate_page(from_path=content_path, template_path=template_path, dest_path=dest_path)

main()