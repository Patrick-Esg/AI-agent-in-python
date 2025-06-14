import os
from functions.config import MAX_CHARS
from google.genai import types

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description=f"Reads and returns the first {MAX_CHARS} characters of the content from a specified file within the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path that leads to the file, relative to the working directory.",
            ),
        },
    ),
)

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
