import os,subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args = None):
    try:
        base_path = os.path.abspath(working_directory)
    except Exception as e:
        return f'Error validating "working_directory":\n{e}'
    target_path = os.path.abspath(os.path.join(base_path, file_path))

    if not target_path.startswith(base_path):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(target_path):
        return f'Error: File "{file_path}" not found.'
    if not target_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    try:
        commands = ["python3",target_path]
        if args:
            commands.extend(args)
        result = subprocess.run(commands,capture_output=True, timeout=30, text=True, cwd=base_path)
        if result is None:
            return "No output produced."

        out_string = f'\nSTDOUT: {result.stdout}\nSTDERR: {result.stderr}\n'
        if result.returncode != 0:
            out_string += f'Process exited with code {result.returncode}'
        return out_string
    except Exception as e:
        return f"Error: executing Python file: {e}"

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
                    description="Optional arguments to pass to the Python file",
                ),
                description="Optional arguments to pass to the Python file",
            ),
        },
        required=["file_path"],
    ),
)