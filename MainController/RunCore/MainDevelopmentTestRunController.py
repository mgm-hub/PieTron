from MainController.Utilities.Log import Log
from MainController.Utilities.Constants import Constants
from MainController.ObserverCore.ObserverService import ObserverService
from MainController.FileCore.FileService import FileService
from MainController.DataCore.DataClassShell import DataClassShell
from MainController.DataCore.DataClass import DataClass
import json
from MainController.ActionCore.RunProcess import RunProcess



class MainDevelopmentTestRunController:
    the_observer_service = None

    def __init__(self):
        if MainDevelopmentTestRunController.the_observer_service is None:
            MainDevelopmentTestRunController.the_observer_service = ObserverService()


    ##########
    #####
    ## Run
    #####
    ##########


    def main_init(self):
        Log.log(Constants.MAIN_INIT_MESSAGE)
        # self.the_observer_service.TEST_obsererer_service_action()
        #self.TEST_read_file_as_string()
        #self.TEST_read_file_as_object()
        #self.TEST_write_to_new_file()
        my_run_process = RunProcess()
        my_run_process.main_init()



    ##########
    #####
    ## Tests
    #####
    ##########


    def TEST_read_file_as_string(self):
        url_path = "Resources/test.json"
        string_data = FileService.get_object_from_path(url_path)
        new_data = FileService.convert_string_to_data_class_action(string_data)
        new_name = new_data.get_name()
        Log.log(new_name)


    def TEST_read_file_as_object(self):
        url_path = "Resources/test.json"
        with open(url_path) as json_file:
            input_object = json.load(json_file)
            new_data_shell = DataClassShell(**input_object)
            new_data = DataClass(**new_data_shell.get_data_class())
            new_name = new_data.get_name()
            Log.log(new_name)


    def TEST_write_to_new_file(self):
        my_file = FileService.create_file_at_location("Resources", "tomato")
        url_path = "Resources/test.json"
        string_data = FileService.get_object_from_path(url_path)
        new_data = FileService.convert_string_to_data_class_action(string_data)
        new_shell = DataClassShell(new_data)
        FileService.write_to_file(my_file, new_shell.to_json())