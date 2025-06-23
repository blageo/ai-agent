import os


def get_file_content(working_directory, file_path):
    try:
        abs_working_dir = os.path.abspath(working_directory)
        abs_file_path = os.path.abspath(file_path)

        if not abs_file_path.startswith(abs_working_dir):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(abs_file_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        MAX_CHARS = 10000
        with open(abs_file_path, 'r') as f:
            file_content_string = f.read(MAX_CHARS)
            return file_content_string
        
    except FileNotFoundError:
        return f'Error: File not found: "{file_path}"'
    except PermissionError:
        return f'Error: Permission denied for file: "{file_path}"'
    except OSError as e:
        return f'Error: An OS error occurred: {e}'
    except Exception as e:
        return f'Error: An unexpected error occurred: {e}'
