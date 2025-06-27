import os


def write_file(working_directory, file_path, content):
    try:
        abs_working_dir = os.path.abspath(working_directory)
        full_file_path = os.path.join(working_directory, file_path)
        abs_file_path = os.path.abspath(full_file_path)

        if not abs_file_path.startswith(abs_working_dir):
            return f'Error: Cannot write "{file_path}" as it is outside the permitted working directory'
        os.makedirs(os.path.dirname(abs_file_path), exist_ok=True)
        
        with open(abs_file_path, 'w') as f:
            f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        
    except Exception as e:
        return f'Error: Unhandled exception caught when writing to "{file_path}": {e}'
    