import ast
import os
import re
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

    @staticmethod
    def regex_fixer(my_file):
        KEY_TERM = '\"commandDataClassList\"'
        is_initial_key = re.compile(KEY_TERM)

        REGEX_NUMBER = '\"[0-9]+\":'
        has_a_number = re.compile(REGEX_NUMBER)

        EMPTY_LINE = 'S^'
        has_empty_line = re.compile(EMPTY_LINE)

        my_count = 0
        my_array = []
        for line in my_file:
            if re.search(is_initial_key, line):
                my_count = 0
            if re.search(has_empty_line, line):
                pass
            if re.search(has_a_number, line): # is an line to be updated
                my_expected_count = '\"' + str(my_count) + '\":'
                my_expected_count_line = re.compile(my_expected_count)
                if re.search(my_expected_count_line, line): # normal write
                    pass
                    my_array.append(line)
                else: # fix line
                    pass
                    updated_string = re.sub(REGEX_NUMBER, my_expected_count, line)
                    my_array.append(updated_string)
                my_count += 1
            else: # is a normal line
                my_array.append(line)
        my_file.close()
        return my_array

