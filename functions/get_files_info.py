import os

def get_files_info(working_directory, directory=None):
	abs_working_dir = os.path.abspath(working_directory)
	target_dir = os.path.abspath(directory) if directory else abs_working_dir

	if not os.path.commonpath([abs_working_dir]) == os.path.commonpath([abs_working_dir, target_dir]):
		return f'Error: Cannot list "{directory}" as it is outside the permitted working directory.'

	if not os.path.isdir(target_dir):
		return f'Error: "{directory}" is not a directory.'

	files_info = []
	try:
		for entry in os.listdir(target_dir):
			entry_path = os.path.join(target_dir, entry)
			try:
				size = os.path.getsize(entry_path)
				is_dir = os.path.isdir(entry_path)
				files_info.append(f"{entry}: file_size={size} bytes, is_dir={is_dir}")
			except Exception as e:
				files_info.append(f"{entry}: Error retrieving file info: {e}")
		return "\n".join(files_info) if files_info else "No files found in the directory."
	except Exception as e:
		return f"Error: {e}"
