import unittest
import os

import functions.get_files_info as get_files_info
import functions.get_file_content as get_file_content
import functions.write_file as write_file

class TestGetFilesInfo(unittest.TestCase):
    def test_write_file_lorem_file(self):
        result = write_file.write_file(
            working_directory="calculator",
            file_path="lorem.txt",
            content="wait, this isn't lorem ipsum"
        )
        self.assertEqual(
            result,
            'Successfully wrote to "lorem.txt" (28 characters written)'
        )
        print(f"Lorem file created: {result}")

    def test_write_file_lorem_subdir(self):
        result = write_file.write_file(
            working_directory="calculator",
            file_path="pkg/morelorem.txt",
            content="lorem ipsum dolor sit amet"
        )
        self.assertEqual(
            result,
            'Successfully wrote to "pkg/morelorem.txt" (26 characters written)'
        )
        print(f"Subdir lorem file created: {result}")

    def test_write_file_lorem_error(self):
        result = write_file.write_file(
            working_directory="calculator",
            file_path="/tmp/temp.txt", 
            content = "this should not be allowed"
        )
        self.assertEqual(
            result,
            'Error: Cannot write "/tmp/temp.txt" as it is outside the permitted working directory'
        )
        print(f"Outside directory result: {result}")

if __name__ == "__main__":
    unittest.main()