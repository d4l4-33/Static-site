import os
import shutil
from recursive_file_copy import recursive_file_copy
from generate_page import generate_pages_recursive

def main():
    
    if os.path.exists("./public"):
        shutil.rmtree("./public")

    recursive_file_copy("./static", "./public")
    generate_pages_recursive("./content", "./template.html", "./public")
    
if __name__ == "__main__":
    main()