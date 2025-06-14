import os
import subprocess
from google.genai import types

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a Python file within the working directory and returns the output from the interpreter.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the Python file to execute, relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(
                    type=types.Type.STRING,
                    description="Optional arguments to pass to the Python file.",
                ),
                description="Optional arguments to pass to the Python file.",
            ),
        },
        required=["file_path"],
    ),
)


def run_python_file(working_directory, file_path):
    try:
        file = os.path.join(working_directory,file_path)
        working_abs = os.path.abspath(working_directory)
        full_path = os.path.abspath(file)

        if not full_path.startswith(working_abs):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.exists(full_path):
            return f'Error: File "{file_path}" not found.'

        if not os.path.basename(full_path).endswith('.py'):
            return f'Error: "{full_path}" is not a Python file.'

        else:
            print('this is a python file')
            target_py_file = os.path.basename(full_path)
            dir_path = os.path.dirname(full_path)
            result = subprocess.run(
                ['python3', file_path], 
                cwd = working_directory, 
                timeout = 30, 
                capture_output=True, 
                text=True )

            #print(result.stdout, result.stderr)
            std_out = f'STDOUT: {result.stdout}'
            std_err = f'STERR: {result.stderr}'
            to_return = f'{std_out} \n{std_err}'

            if result.returncode != 0:
                to_return += f'\n Process exited with code {result.returncode}'
            
            if not result.stdout: 
                to_return += 'No output produced'
            
            return to_return

    except Exception as e:
        return f"Error: executing Python file: {e}"
