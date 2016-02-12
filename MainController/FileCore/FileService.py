import os
import json
import sys
from MainController.Utilities.Log import Log
from MainController.Utilities.Constants import Constants
from MainController.DataCore.DataClassShell import DataClassShell
from MainController.DataCore.DataClass import DataClass

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
        except Exception:
            print("Unexpected error:", sys.exc_info()[0])

    @staticmethod
    def create_file_at_location(directory_name, file_name):
        file_name = directory_name + PATH_SLASH + file_name + Constants.JSON_TAG
        try:
            open_file = open(file_name, 'w')
            print(open_file)
            return open_file
        except Exception:
            print("Unexpected error:", sys.exc_info()[0])

    @staticmethod
    def write_to_file(my_file, my_string):
        try:
            my_file.write(my_string)
        except Exception:
            pass

    @staticmethod
    def convert_string_to_data_class_action(string_data):
        try:
            new_data_shell = DataClassShell(**string_data)
            new_data_class = DataClass(**new_data_shell.get_data_class())
            return new_data_class
        except Exception:
            print("Can not convert string to class", Exception)