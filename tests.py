import unittest
# from subdirectory.filename import function_name
#from functions.get_files_info import get_files_info
#from functions.get_file_content import get_file_content
#from functions.write_file import write_file
from functions.run_python import run_python_file


# class Test_get_files_info(unittest.TestCase):
#     def test_current_dir(self):
#         print("test1")
#         print(get_files_info("calculator", "."))

#     def test_dir_within(self):
#         print('test2')
#         print(get_files_info("calculator", "pkg"))

#     def test_dir_outside(self):
#         print('test3')
#         print(get_files_info("calculator", "/bin"))

#     def test_dir_outside2(self):
#         print('test4')
#         print(get_files_info("calculator", "../"))

# class Test_get_file_content(unittest.TestCase):
#     # def test_lorem_text(self):
#     #     print("test1")
#     #     print(get_file_content("calculator", "lorem.txt"))

#     def test_dir_main(self):
#         print('test1')
#         print(get_file_content("calculator", "main.py"))

#     def test_dir_outside(self):
#         print('test2')
#         print(get_file_content("calculator", "pkg/calculator.py"))

#     def test_dir_outside2(self):
#         print('test3')
#         print(get_file_content("calculator", "/bin/cat"))

# class test(unittest.TestCase):
#     def test_dir_main(self):
#         print('test1')
#         print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))

#     def test_new_directories(self):
#         print('test2')
#         print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))

#     def test_new_error(self):
#         print('test3')
#         print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))

class test(unittest.TestCase):
    def test_main_py(self):
        print('test1')
        print(run_python_file("calculator", "main.py"))

    def test_test_py(self):
        print('test2')
        print(run_python_file("calculator", "tests.py"))

    def test_error_outside(self):
        print('test3')
        print(run_python_file("calculator", "../main.py"))

    def test_error_dne(self):
        print('test4')
        print(run_python_file("calculator", "nonexistent.py"))

if __name__ == "__main__":
    unittest.main()