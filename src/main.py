import os
import shutil
from recursive_file_copy import recursive_file_copy

STATIC_PATH = "./static"
PUBLIC_PATH = "./public"

def main():
    
    if os.path.exists(PUBLIC_PATH):
        shutil.rmtree(PUBLIC_PATH)

    recursive_file_copy(STATIC_PATH, PUBLIC_PATH)
        

if __name__ == "__main__":
    main()