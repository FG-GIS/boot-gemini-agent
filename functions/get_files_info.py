import os

def get_files_info(working_directory, directory=None):
    try:
        base_dir = os.path.abspath(working_directory)
    except Exception as e:
        return f'Error validating "working_directory":\n{e}'
    
    if directory.startswith(".."):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    try:
        target_dir = os.path.abspath(os.path.join(base_dir,directory))
    except Exception as e:
        return f'Error validating "directory":\n{e}'

    if not target_dir.startswith(base_dir):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(target_dir):
        return f'Error: "{directory}" is not a directory'
    try:
        info = []

        for obj in os.listdir(target_dir):
            obj_path = os.path.join(target_dir,obj)
            info.append(f"- {obj}: file size={os.path.getsize(obj_path)} bytes, is_dir={os.path.isdir(obj_path)}")
        
        return "\n".join(info)
    except Exception as e:
        return f"Error listing files: {e}"