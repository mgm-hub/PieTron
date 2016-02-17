from MainController.FileCore.FileService import FileService
from MainController.Utilities.Constants import Constants
from MainController.Utilities.Log import Log
from MainController.Utilities.TextActions import TextActions


class SharedData:
    def __init__(self):
        pass

    @staticmethod
    def get_codex_data():
        complete_file_list = SharedData.get_codex_directory_files()
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
