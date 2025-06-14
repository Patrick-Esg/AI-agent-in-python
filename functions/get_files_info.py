import os
from google.genai import types

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)



def get_files_info(working_directory, directory=None):
    try:
        to_directory = directory if directory is not None else ""

        #order matters below
        joined_path = os.path.join(working_directory, to_directory)
        working_abs = os.path.abspath(working_directory)
        full_path = os.path.abspath(joined_path)
        
        if not full_path.startswith(working_abs):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
        if not os.path.isdir(full_path):
            return f'Error: "{directory}" is not a directory'

        else:
            return "\n".join(map(lambda x: pather(full_path, x)(), os.listdir(full_path)))
    except Exception as e:
        print(f"Error: ", e)

def pather(full_path, dir):#function transofrmation, return
    path = os.path.join(full_path, dir)
    def dir_helper():
        file_size = os.path.getsize(path)
        is_dir = not os.path.isfile(path)
        return f'- {dir}: file_size={file_size}, is_dir={is_dir}'
    return dir_helper


