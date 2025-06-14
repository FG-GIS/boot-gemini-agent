import os
from google.genai import types
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    """
    Reads the content of a file located at the specified path within the given working directory.
    
    :param working_directory: The directory where the file is located.
    :param file_path: The relative path to the file from the working directory.
    :return: The content of the file as a string, or None if the file does not exist.
    """
    try:
        base_dir = os.path.abspath(working_directory)
    except Exception as e:
        return f'Error validating "working_directory":\n{e}'
    
    target_path = os.path.abspath(os.path.join(base_dir,file_path))
    if not target_path.startswith(base_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(target_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    try:
        with open(target_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)    
            if len(file_content_string) == MAX_CHARS:
                return file_content_string +  f'[...File "{file_path}" truncated at 10000 characters]'
            return file_content_string
    except Exception as e:
        return f"Error reading file contents: {e}"

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description=f"Reads and returns the first {MAX_CHARS} characters of the content from a specified file within the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file whose content should be read, relative to the working directory.",
            ),
        },
        required=["file_path"]
    ),
)