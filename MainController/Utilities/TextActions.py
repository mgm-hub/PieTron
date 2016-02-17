import ast
import os
from MainController.Utilities.Constants import Constants


class TextActions:
    def __init__(self):
        pass


    @staticmethod
    def print_dictionary(my_dictionary):
        for key, value in my_dictionary.iteritems() :
            print (key, value)


    @staticmethod
    def convert_string_to_dictionary(my_dictionary):
        try:
            return ast.literal_eval(str(my_dictionary))
        except StandardError:
            return None

    @staticmethod
    def convert_string_to_array(my_array):
        try:
            return str(my_array).split(',')
        except StandardError:
            return None

    @staticmethod
    def append_prefix_to_string_list(my_string, my_list):
        new_string_list = []
        for my_string_part in my_list:
            new_string_list.append(my_string + Constants.PATH_SLASH + my_string_part)
        return new_string_list

    @staticmethod
    def combine_directories_from_list(my_list):
        new_file_list = []
        for my_directory in my_list:
            directory_info_list = os.listdir(my_directory)
            new_file_list.append(directory_info_list)
        return new_file_list

