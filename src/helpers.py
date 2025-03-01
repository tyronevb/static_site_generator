from markdown_to_html import markdown_to_html_node
import os
import shutil

def clear_dir(dest):
    # clear the contents of the dest dir
    shutil.rmtree(dest) # this deletes the entire directory as well
    os.mkdir(dest) # this creates a new dest dir

def copy_from_dir_to_dir(src, dest):
    
    # recursive function to handle nested directories and files
    
    # for loop to copy all files, subdirectories, nested files etc.
    dir_contents = os.listdir(src) # returns a list containing strings representing the names of all dirs and files in the dir from which it is called
    # find files using
    for content in dir_contents:
        path_to_content = os.path.join(src, content)
        is_file = os.path.isfile(path_to_content)
        # print(f"{path_to_content} is file? - {is_file}") # some debug

        if is_file:
          dest_path = os.path.join(dest, content)
          shutil.copy(path_to_content, dest_path)
        else:
            # this is where the recusion must happen
            dest_dir_path = os.path.join(dest, content)
            os.mkdir(dest_dir_path)
            copy_from_dir_to_dir(src=path_to_content, dest=dest_dir_path)

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        line = line.strip()
        if line.startswith("# "):
            return line[2:]
    raise ValueError("No valid title found")

def generate_page(from_path, template_path, dest_path):

    # print a message with the paths
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    # read the md from_path and store in a variable
    with open(from_path, "r") as f:
        raw_md = f.read()

    # read template and store in a variable
    with open(template_path, "r") as f:
        html_template = f.read()

    # convert md to HTML string
    html_node = markdown_to_html_node(raw_md)
    html_string = html_node.to_html()

    # extract title
    page_title = extract_title(raw_md)

    # replace title and content placeholders
    html_template = html_template.replace("{{ Title }}", page_title)
    html_template = html_template.replace("{{ Content }}", html_string)

    # write the new HTML page to dest path (create dirs if they don't exist)
    if not os.path.isdir(os.path.dirname(dest_path)):
        os.makedirs(os.path.dirname(dest_path))
    with open(dest_path, "w") as f:
        f.write(html_template)
        f.close()