import os
import shutil
import sys
from recursive_file_copy import recursive_file_copy
from generate_page import generate_pages_recursive



def main():
    basepath = "/"
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    
    if os.path.exists("./docs"):
        shutil.rmtree("./docs")

    recursive_file_copy("./static", "./docs")
    generate_pages_recursive("./content", "./template.html", "./docs", basepath)
    
if __name__ == "__main__":
    main()