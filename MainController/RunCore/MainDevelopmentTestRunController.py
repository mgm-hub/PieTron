import json
import time
import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from MainController.Utilities.Log import Log
from MainController.Utilities.Constants import Constants
from MainController.ObserverCore.ObserverService import ObserverService
from MainController.FileCore.FileService import FileService
from MainController.RunCore.DataClassShell import DataClassShell
from MainController.RunCore.DataClass import DataClass
from MainController.DriverCore.SeleniumDriver import SeleniumDriver
from MainController.Utilities.HttpActions import HttpActions
from MainController.DriverCore.GridActions import GridActions
from MainController.DataCore.SharedDataActions import SharedDataActions
from MainController.Utilities.TextActions import TextActions
from MainController.DataCore.CommandDataObject import CommandDataObject
from MainController.DataCore.CommandDataClass import CommandDataClass
from MainController.CommandCore.CommandProcessActionClass import CommandProcessActionClass

from MainController.CommandCore.CommandProcessRun import CommandProcessRun
from MainController.CommandCore.MainProcessContextObject import MainProcessContextObject
from MainController.DataCore.MainProcessSharedDataGroup import MainProcessSharedDataGroup





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
        #self.TEST_read_file_as_string()

        ############
        ## Run Here
        #my_run_service = RunService()
        #my_run_service.main_init()

        ############
        ## Tests
        #self.TEST_directory()
        #self.TEST_read_file_as_object()
        #self.TEST_write_to_new_file()
        #self.TEST_selenium_build()
        #self.TEST_remote_driver()
        #self.TEST_http_actions()
        #self.TEST_codex_object()
        #self.TEST_directory_lists()
        #self.TEST_shared_data_codex_test()
        #self.TEST_suite_directory()
        #self.TEST_suite_data()
        #self.TEST_regex_fix()
        #self.TEST_shared_data()
        #self.TEST_run_suite_by_name()
        #self.TEST_test_run_basic()
        #self.TEST_test_run_advanced()
        #self.TEST_data_converison()
        #self.TEST_data_converison_advanced()
        self.TEST_run_complete_action()


    ##########
    #####
    ## Tests
    #####
    ##########


    def TEST_directory(self):
        Log.log(Constants.CHROME_DRIVER_LOCATION_WIN)


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


    def TEST_selenium_build(self):
        web_driver = webdriver.Firefox() # Get local session of firefox
        web_driver.get("http://www.yahoo.com") # Load page
        #assert "Yahoo!" in browser.title
        elem = web_driver.find_element_by_name("p") # Find the query box
        elem.send_keys("seleniumhq" + Keys.RETURN)
        time.sleep(0.2) # Let the page load, will be added to the API
        web_driver.close()


    def TEST_remote_driver(self):
        #browser = SeleniumDriver.get_firefox_webdriver()
        #browser = SeleniumDriver.get_chrome_webdriver()
        browser = SeleniumDriver.get_remote_webdriver()
        browser.get("http://www.yahoo.com") # Load page


    def TEST_http_actions(self):
        response_code = HttpActions.get_page_response_code('http://localhost:4444/grid/console/test')
        is_grid_running = GridActions.is_grid_running()
        Log.log(is_grid_running)


    def TEST_codex_object(self):
        url_path = "Resources/WebData/Codex/GoogleCodex.json"
        string_data = FileService.get_object_from_path(url_path)
        Log.log(string_data)
        new_codex = FileService.convert_string_to_web_codex_action(string_data)
        new_name = new_codex.get_file_name()
        Log.log(new_name)
        Log.log(new_codex.to_json())


    def TEST_directory_lists(self):
        url_path = "Resources/WebData/Codex"
        directory_info = os.listdir(url_path)
        Log.log(directory_info)


    def TEST_shared_data_codex_test(self):
        SharedDataActions.build_codex_data()


    def TEST_suite_data_directory(self):
        url_path = "Resources/WebData/SuiteFileGroups"
        directory_info_list = FileService.get_files_in_directory(url_path)
        updated_list = TextActions.append_prefix_to_string_list(url_path, directory_info_list)
        Log.log(updated_list)
        combined_list = FileService.get_joined_files_from_combined_directory_list(updated_list)
        Log.log(combined_list)


    def TEST_suite_data(self):
        url_path = "Resources/WebData/SuiteFileGroups/GoogleSuite/Google_Test_Search.json"
        string_data = FileService.get_object_from_path(url_path)
        #Log.log(string_data)
        suite_shell = FileService.convert_string_to_suite_file_content(string_data)
        #Log.log(suite_shell.to_json())
        #file_name = suite_shell.fileName
        #Log.log(file_name)

        suite_data_array = FileService.get_suite_data_array_from_shell(suite_shell)
        my_test_data = suite_data_array[0]
        my_suite_name = my_test_data.get_suite_name()
        print(my_suite_name)
        #Log.log(str(suite_data))


    def TEST_regex_fix(self):
        url_path = "Resources/WebData/SuiteFileGroups/GoogleSuite/Small.json"
        my_file = FileService.read_file_at_location(url_path)
        my_array = TextActions.regex_fixer(my_file)
        my_path = "Resources/WebData/SuiteFileGroups/GoogleSuite/Updated.json"
        FileService.write_file_at_location(my_path, my_array)


    def TEST_shared_data(self):
        pass
        suite_files = SharedDataActions.get_test_suite_directory_files()
        codex_files = SharedDataActions.get_codex_directory_files()
        print(codex_files)
        suite_data = SharedDataActions.get_suite_data()
        first_suite = suite_data[0]
        my_suite_name = first_suite.get_suite_name()
        print(my_suite_name)


    def TEST_run_suite_by_name(self):
        #group_name = "GoogleSuite"
        #file_name = "Google_Test_Search.json"
        group_name = "RedditSuite"
        file_name = "Reddit_Test_Login.json"
        test_number = 0
        suite_shell = SharedDataActions.get_suite_shell_from_group_and_file(group_name, file_name)
        suite_data_array = FileService.get_suite_data_array_from_shell(suite_shell)
        first_suite = suite_data_array[test_number]
        my_suite_name = first_suite.get_suite_name()
        print(my_suite_name)


    def TEST_test_run_basic(self):
        first_class = CommandDataClass("COMMENT", "one")
        second_class = CommandDataClass("CONSOLE", "two")
        third_class = CommandDataClass("clickElement", "element")
        command_data_class_array = [first_class, second_class, third_class]

        my_command_data_object = CommandDataObject(command_data_class_array)
        my_command_data_object.set_current_command_data(third_class)

        web_driver = webdriver.Firefox()
        myCommandProcessActionClass = CommandProcessActionClass(web_driver)
        myCommandProcessActionClass.api_command_consumption(my_command_data_object)


    def TEST_test_run_advanced(self):
        first_class = CommandDataClass("COMMENT", "one")
        second_class = CommandDataClass("CONSOLE", "two")
        third_class = CommandDataClass("clickElement", "element")
        command_data_class_array = [first_class, second_class, third_class]

        my_command_data_object = CommandDataObject(command_data_class_array)
        my_command_data_object.set_current_command_data(third_class)

        web_driver = webdriver.Firefox()
        myCommandProcessActionClass = CommandProcessActionClass(web_driver)
        myCommandProcessActionClass.api_command_consumption(my_command_data_object)


    def TEST_data_converison(self):
        group_name = "RedditSuite"
        file_name = "Reddit_Test_Login.json"
        test_number = 0
        suite_shell = SharedDataActions.get_suite_shell_from_group_and_file(group_name, file_name)
        suite_data_array = FileService.get_suite_data_array_from_shell(suite_shell)
        first_suite = suite_data_array[test_number]
        command_data_class_array = first_suite.convert_to_command_data_class_array()
        #print(command_data_class_array[0].api_name)


    def TEST_data_converison_advanced(self):
        group_name = "RedditSuite"
        file_name = "Reddit_Test_Login.json"
        test_number = 0
        suite_shell = SharedDataActions.get_suite_shell_from_group_and_file(group_name, file_name)
        my_suiteFileObjectArray = suite_shell.get_suite_file_object_at_index(0)
        print(my_suiteFileObjectArray.description)


    def TEST_run_complete_action(self):
        pass
        my_ObserverService = ObserverService()
        my_MainProcessSharedDataGroup = MainProcessSharedDataGroup()
        my_MainProcessContextObject = MainProcessContextObject(my_ObserverService, my_MainProcessSharedDataGroup)

        my_CommandProcessRun = CommandProcessRun(my_MainProcessContextObject)
        my_CommandProcessRun.run_action_init()




