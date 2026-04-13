import os
import shutil
from recursive_file_copy import recursive_file_copy
from generate_page import generate_page

def main():
    
    if os.path.exists("./public"):
        shutil.rmtree("./public")

    recursive_file_copy("./static", "./public")
    generate_page("./content/index.md", "./template.html", "./public/index.html")
    
        

if __name__ == "__main__":
    main()