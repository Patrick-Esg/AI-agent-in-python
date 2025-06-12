import unittest
# from subdirectory.filename import function_name
#from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content


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

class Test_get_file_content(unittest.TestCase):
    # def test_lorem_text(self):
    #     print("test1")
    #     print(get_file_content("calculator", "lorem.txt"))

    def test_dir_main(self):
        print('test1')
        print(get_file_content("calculator", "main.py"))

    def test_dir_outside(self):
        print('test2')
        print(get_file_content("calculator", "pkg/calculator.py"))

    def test_dir_outside2(self):
        print('test3')
        print(get_file_content("calculator", "/bin/cat"))

if __name__ == "__main__":
    unittest.main()