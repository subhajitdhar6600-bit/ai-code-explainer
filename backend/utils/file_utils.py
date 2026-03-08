import os

def get_file_extension(file_name: str):
    return os.path.splitext(file_name)[1]