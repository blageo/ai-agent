import unittest
import os

import functions.get_files_info as get_files_info
import functions.get_file_content as get_file_content

class TestGetFilesInfo(unittest.TestCase):
    def setUp(self):
        self.working_directory = "/tmp/test_directory"
        self.test_directory = "/tmp/test_directory/subdir"
        self.test_file = "/tmp/test_directory/subdir/test_file.txt"
        
        # Create test directories and files
        os.makedirs(self.test_directory, exist_ok=True)
        with open(self.test_file, 'w') as f:
            f.write("Test content")

    def tearDown(self):
        # Clean up test directories and files
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        if os.path.exists(self.test_directory):
            os.rmdir(self.test_directory)
        if os.path.exists(self.working_directory):
            os.rmdir(self.working_directory)

    def test_get_files_info_valid_directory(self):
        result = get_files_info.get_files_info(self.working_directory, self.test_directory)
        self.assertIn("test_file.txt: file_size=12 bytes, is_dir=False", result)

    def test_get_files_info_invalid_directory(self):
        result = get_files_info.get_files_info(self.working_directory, "/tmp/test_directory/invalid_directory")
        self.assertEqual(result, 'Error: "/tmp/test_directory/invalid_directory" is not a directory.')

    def test_get_files_info_outside_working_directory(self):
        result = get_files_info.get_files_info(self.working_directory, "/tmp")
        self.assertEqual(result, 'Error: Cannot list "/tmp" as it is outside the permitted working directory.')

    def test_get_files_info_calculator_directory(self):
        working_directory = os.path.abspath("calculator")
        result = get_files_info.get_files_info(working_directory, os.path.abspath("calculator/."))
        print(f"Calculator directory result: {result}")

    def test_get_files_info_calculator_pkg_directory(self): 
        working_directory = os.path.abspath("calculator")
        result = get_files_info.get_files_info(working_directory, os.path.abspath("calculator/pkg"))
        print(f"Pkg directory result: {result}")

    def test_get_files_info_calculator_bin_directory(self):
        working_directory = os.path.abspath("calculator")
        result = get_files_info.get_files_info(working_directory, os.path.abspath("calculator/bin"))
        print(f"Bin directory result: {result}")

    def test_get_files_info_calculator_parent_directory(self):
        working_directory = os.path.abspath("calculator")
        result = get_files_info.get_files_info(working_directory, os.path.abspath("../"))
        print(f"Parent Directory result: {result}")

    def test_get_file_content_lorem(self):
        working_directory = os.path.abspath("calculator")
        file_path = os.path.abspath("calculator/lorem.txt")
        result = get_file_content.get_file_content(working_directory, file_path)
        print(f"Lorem file content result: {result}")

    def test_get_file_content_main(self):
        working_directory = os.path.abspath("calculator")
        file_path = os.path.abspath("calculator/main.py")
        result = get_file_content.get_file_content(working_directory, file_path)
        print(f"Main file content result: {result}")

    def test_get_file_content_pkg_calc(self):
        working_directory = os.path.abspath("calculator")
        file_path = os.path.abspath("calculator/pkg/calculator.py")
        result = get_file_content.get_file_content(working_directory, file_path)
        print(f"Pkg calc file content result: {result}")

    def test_get_file_content_bin_cat(self):
        working_directory = os.path.abspath("calculator")
        file_path = os.path.abspath("bin/cat")
        result = get_file_content.get_file_content(working_directory, file_path)
        print(f"Bin cat file content result: {result}")

if __name__ == "__main__":
    unittest.main()