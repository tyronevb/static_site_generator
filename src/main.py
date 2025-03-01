from textnode import TextNode, TextType
import os
import shutil

def main():
    src = "static/"
    dest = "public/"

    copy_from_dir_to_dir(src=src, dest=dest, root_dest=True)

def copy_from_dir_to_dir(src, dest, root_dest=True):
    # recursive function to handle nested directories and files
    
    # clear the contents of the dest dir
    shutil.rmtree(dest) # this deletes the entire directory as well
    os.mkdir(dest) # this creates a new dest dir

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
    
main()
