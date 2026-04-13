import os
import shutil

def recursive_file_copy(path, dst):
    if not os.path.exists(dst):
        os.mkdir(dst)
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isfile(file_path):
            shutil.copy(file_path, dst)
            continue
        public_dir_path = os.path.join(dst, file)
        os.mkdir(public_dir_path)
        recursive_file_copy(file_path, public_dir_path)