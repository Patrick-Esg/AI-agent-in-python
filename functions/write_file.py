import os

def write_file(working_directory, file_path, content):
    try:
        #order matters below
        file = os.path.join(working_directory,file_path)
        working_abs = os.path.abspath(working_directory)
        full_path = os.path.abspath(file)
        
        if not full_path.startswith(working_abs):
            return f'Error: Cannot write to "{full_path}" as it is outside the permitted working directory'
        
        if not os.path.exists(full_path):
            #create directory and file
            print('new directory being made')
            dir_path = os.path.dirname(full_path) #the directories before the base
            #file_name = os.path.basename(full_path) #the base
            
            os.makedirs(dir_path, exist_ok=True)
    
        with open(full_path, "w") as f:
            f.write(content)

        return f'Successfully wrote to "{full_path}" ({len(content)} characters written)'

    except Exception as e:
        print("Error: ", e)