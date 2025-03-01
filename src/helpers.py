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

def generate_page_helper(from_path, template_path, dest_path):

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

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    # crawl every entry in the content directory
    #print(f"\nNew Call of Func:\nPTC: {dir_path_content}, dest:{dest_dir_path}")

    dir_contents = os.listdir(dir_path_content) # returns a list containing strings representing the names of all dirs and files in the dir from which it is called

    for content in dir_contents:
        #print(f"content: {content} dir_contents: {dir_contents}")
        path_to_content = os.path.join(dir_path_content, content)
        
        if os.path.isfile(path_to_content) and content.endswith(".md"):
            # valid markdown, generate html for it
            # call another helper function here
            #print("We have an md file")
            dest_path = os.path.join(dest_dir_path, content)
            # print(path_to_content, template_path, dest_dir_path)

            # rename to html
            html_dest_path = dest_path.split(".")[0] + ".html"

            generate_page_helper(path_to_content, template_path, html_dest_path)
        else:
            # found a directory this is where the recursion must happen
            #print("We have another dir")
            new_dest_dir_path = os.path.join(dest_dir_path, content)
            #print(f"dest_dir_path: {dest_dir_path} path_to_content:{path_to_content}")
            os.mkdir(new_dest_dir_path)
            generate_pages_recursive(path_to_content, template_path, new_dest_dir_path)
    #print("Reached end of function call")
