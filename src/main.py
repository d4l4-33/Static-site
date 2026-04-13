import os
import shutil


PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))[:-3]                        
SRC_PATH = os.path.join(PROJECT_PATH, "src")
STATIC_PATH = os.path.join(PROJECT_PATH, "static")
PUBLIC_PATH = os.path.join(PROJECT_PATH, "public")


def main():
    
    if os.path.isfile(PUBLIC_PATH):
        os.remove(PUBLIC_PATH)
    if not os.path.exists(PUBLIC_PATH):
        os.mkdir(PUBLIC_PATH)
    else:
        for item in os.listdir(PUBLIC_PATH):
            os.remove(item)

    if not os.path.exists(SRC_PATH):
        raise LookupError("ERROR: src-path not found")
    if not os.path.exists(STATIC_PATH):
        raise LookupError("ERROR: static-path not found")
    file_copy(SRC_PATH, PUBLIC_PATH)
    #file_copy(STATIC_PATH, PULBIC_PATH)
        



def file_copy(path, dst):
    dir_path = os.path.join(PUBLIC_PATH, path)
    for file in os.listdir(dir_path):
        if file == "__pycache__" or file == "test_directory":
            continue
        file_path = os.path.join(dir_path, file)
        print(file_path)
        if os.path.isfile(file_path):
            shutil.copy(file_path, dst)
            continue
        else:
            dir_path = os.path.join(dst, file)
            os.mkdir(dir_path)
            file_copy(file_path, dir_path)
            

if __name__ == "__main__":
    main()