import json
import time
import os
from MainController.Utilities.Log import Log
from MainController.Utilities.Constants import Constants
from MainController.ObserverCore.ObserverService import ObserverService
from MainController.FileCore.FileService import FileService
from MainController.DataCore.DataClassShell import DataClassShell
from MainController.DataCore.DataClass import DataClass
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from MainController.DriverCore.SeleniumDriver import SeleniumDriver
from MainController.Utilities.HttpActions import HttpActions
from MainController.DriverCore.GridActions import GridActions
from MainController.DataCore.SharedData import SharedData


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
        self.TEST_shared_data()


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


    def TEST_shared_data(self):
        SharedData.build_codex_data()
