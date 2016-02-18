from MainController.FileCore.FileService import FileService
from MainController.Utilities.Constants import Constants
from MainController.Utilities.Log import Log
from MainController.Utilities.TextActions import TextActions



class SharedDataActions:
    def __init__(self):
        pass

    @staticmethod
    def get_codex_data():
        complete_file_list = SharedDataActions.get_codex_directory_files()
        complete_dictionary = {}
        for my_file in complete_file_list:
            string_data = FileService.get_object_from_path(my_file)
            new_codex = FileService.convert_string_to_web_codex_action(string_data)
            new_map = new_codex.get_codex_map()
            list_dictionary = TextActions.convert_string_to_dictionary(new_map)
            #Log.log(list_dictionary)
            complete_dictionary.update(list_dictionary)
        #TextActions.print_dictionary(complete_dictionary)
        return complete_dictionary


    @staticmethod
    def get_codex_directory_files():
        url_path = Constants.CODEX_DIRECTORY
        file_list = FileService.get_files_in_directory(url_path)
        complete_file_list = []
        for my_file in file_list:
            complete_path = url_path + Constants.PATH_SLASH + my_file
            complete_file_list.append(complete_path)
        return complete_file_list


    @staticmethod
    def get_test_suite_directory_files():
        url_path = Constants.SUITE_DIRECTORY
        directory_info_list = FileService.get_files_in_directory(url_path)
        updated_list = TextActions.append_prefix_to_string_list(url_path, directory_info_list)
        combined_list = FileService.get_joined_files_from_combined_directory_list(updated_list)
        return combined_list


    @staticmethod
    def get_suite_data():
        file_list = SharedDataActions.get_test_suite_directory_files()
        complete_suite_list = []
        for url_path in file_list:
            string_data = FileService.get_object_from_path(url_path)
            suite_shell = FileService.convert_string_to_suite_file_content(string_data)
            suite_data_array = FileService.get_suite_data_array_from_shell(suite_shell)
            for suite_object in suite_data_array:
                complete_suite_list.append(suite_object)
        return complete_suite_list


    @staticmethod
    def get_suite_shell_from_group_and_file(group_name, file_name):
        complete_path = FileService.build_path_for_single_suite(group_name, file_name)
        string_data = FileService.get_object_from_path(complete_path)
        return FileService.convert_string_to_suite_file_content(string_data)