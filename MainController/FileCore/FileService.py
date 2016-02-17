import os
import json
import sys
from MainController.Utilities.Log import Log
from MainController.Utilities.Constants import Constants
from MainController.DataCore.DataClassShell import DataClassShell
from MainController.DataCore.DataClass import DataClass
from MainController.DataCore.WebCodex import WebCodex
from MainController.DataCore.WebCodexShell import WebCodexShell
from MainController.DataCore.SuiteFileObjectContent import SuiteFileObjectContent
from MainController.DataCore.SuiteFileObjectShell import SuiteFileObjectShell
from MainController.DataCore.SuiteFileObject import SuiteFileObject


PATH_SLASH = os.sep


class FileService:
    def __init__(self):
        pass


    @staticmethod
    def path_reader(url_path):
        with open(url_path) as json_file:
            return json.load(json_file)

    @staticmethod
    def get_object_from_path(url_path):
        try:
            input_var = FileService.path_reader(url_path)
            return input_var
        except StandardError:
            print("Unexpected error:", sys.exc_info()[0])

    @staticmethod
    def create_file_at_location(directory_name, file_name):
        file_location = directory_name + PATH_SLASH + file_name + Constants.JSON_TAG
        try:
            open_file = open(file_location, 'w')
            print(open_file)
            return open_file
        except StandardError:
            print("Unexpected error:", sys.exc_info()[0])

    @staticmethod
    def write_to_file(my_file, my_string):
        try:
            my_file.write(my_string)
        except StandardError:
            pass


    ##########
    #####
    ## Types
    #####
    ##########

    @staticmethod
    def convert_string_to_data_class_action(string_data):
        try:
            new_data_shell = DataClassShell(**string_data)
            new_data_class = DataClass(**new_data_shell.get_data_class())
            return new_data_class
        except StandardError:
            print("Can not convert string to class", Exception)


    @staticmethod
    def convert_string_to_web_codex_action(string_data):
        try:
            new_codex_shell = WebCodexShell(**string_data)
            new_codex = WebCodex(**new_codex_shell.get_web_codex())
            return new_codex
        except StandardError:
            print("Can not convert string to class", Exception)


    @staticmethod
    def convert_string_to_suite_file_content(string_data):
        try:
            new_suite_file_content = SuiteFileObjectContent(**string_data)
            new_suite_file_shell = SuiteFileObjectShell(**new_suite_file_content.get_suite_file_object())
            return new_suite_file_shell
        except StandardError:
            print("Can not convert string to class", Exception)

    @staticmethod
    def get_suite_data_array_from_shell(suite_file_shell):
        try:
            my_combined_list = suite_file_shell.get_suite_file_object_array()
            ##
            ## Hack Here
            my_list_data = my_combined_list[0]
            ## Hack Here
            ##
            my_array = []
            for my_suite_file_object in my_list_data:
                suite_file_data = SuiteFileObject(**my_suite_file_object)
                my_array.append(suite_file_data)
            return my_array
        except StandardError:
            print("Can not convert string to class", Exception)

    ##########
    #####
    ## Directory
    #####
    ##########

    @staticmethod
    def get_files_in_directory(url_path):
        try:
            return os.listdir(url_path)
        except StandardError:
            return None

    @staticmethod
    def get_files_from_combined_directory_list(my_list):
        new_file_list = []
        for my_directory in my_list:
            directory_info_list = os.listdir(my_directory)
            new_file_list.append(directory_info_list)
        return new_file_list

    @staticmethod
    def get_joined_files_from_combined_directory_list(my_list):
        new_file_list = []
        for my_directory in my_list:
            directory_info_list = os.listdir(my_directory)
            for new_list in directory_info_list:
                new_file_list.append(my_directory + Constants.PATH_SLASH + new_list)

        return new_file_list

    ##########
    #####
    ## Read / Write
    #####
    ##########

    @staticmethod
    def read_file_at_location(url_path):
        try:
            return open(url_path, 'r')
        except StandardError:
            return None

    @staticmethod
    def write_file_at_location(url_path, my_array):
        try:
            my_file = open(url_path, 'w')
            for line in my_array:
                my_file.write(line)
            my_file.close()
        except StandardError:
            return None

    ##########
    #####
    ## Directory
    #####
    ##########

    @staticmethod
    def build_path_for_single_suite(group_name, file_name):
        return Constants.SUITE_DIRECTORY + Constants.PATH_SLASH + group_name + Constants.PATH_SLASH + file_name




