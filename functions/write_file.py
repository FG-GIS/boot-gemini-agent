import os

def write_file(working_directory, file_path, content):
    try:
        base_dir = os.path.abspath(working_directory)
    except Exception as e:
        return f'Error validating "working_directory":\n{e}'
    
    target_path = os.path.abspath(os.path.join(base_dir,file_path))
    if not target_path.startswith(base_dir):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(os.path.dirname(target_path)):
        try:
            os.makedirs(os.path.dirname(target_path), exist_ok=True)
        except Exception as e:
            return f"Error creating filepath: {e}"
    
    if os.path.exists(target_path) and os.path.isdir(target_path):
        return f'Error: "{file_path}" is a directory, not a file'
    
    try:
        with open(target_path, "w") as f:
            f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error writing the file: {e}"