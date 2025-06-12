import os
from functions.config import MAX_CHARS

def get_file_content(working_directory, file_path):
    try:
        #order matters below
        file = os.path.join(working_directory,file_path)
        working_abs = os.path.abspath(working_directory)
        full_path = os.path.abspath(file)
        
        if not full_path.startswith(working_abs):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
        if not os.path.isfile(full_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        else:
            return reader(file)
    except Exception as e:
        print("Error: ", e)

def reader(file_path):
    file_content_string = ''

    with open(file_path, "r") as f:
        file_content_string = f.read(MAX_CHARS)
    
    if len(file_content_string) == MAX_CHARS:
        file_content_string += f'[...File "{file_path}" truncated at 10000 characters]'
    
    return file_content_string
