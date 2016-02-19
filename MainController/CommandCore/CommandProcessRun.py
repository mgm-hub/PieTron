from time import sleep
from MainController.Utilities.Log import Log
from MainController.Utilities.Constants import Constants
from MainController.DataCore.CommandDataObject import CommandDataObject
from MainController.CommandCore.CommandProcessActionClass import CommandProcessActionClass


class CommandProcessRun:
    the_CommandDataObject = None
    the_CommandProcessActionClass = None
    the_MainProcessContextObject = None

    def __init__(self, the_MainProcessContextObject):
        self.the_MainProcessContextObject = the_MainProcessContextObject
        if self.the_CommandProcessActionClass is None:
            self.the_CommandProcessActionClass = CommandProcessActionClass(the_MainProcessContextObject.get_web_driver)


    ##########
    #####
    ## Builder
    #####
    ##########


    def run_action_init(self, test_number):
        Log.log(Constants.STARTING_TEST)

        ############################
        ## Get Context Object with WebDriver

        ############################
        ## Gets Test Data Array Here
        my_SuiteFileObject = self.the_MainProcessContextObject.get_my_suite_file_object(test_number)

        ############################
        ## Get Web Driver
        web_driver = self.the_MainProcessContextObject.get_web_driver()

        ############################
        ## Navigate To Start Page
        base_url = my_SuiteFileObject.get_base_url()
        #print ("base_url :: " + base_url)
        self.navigate_to_initial_url(web_driver, base_url)

        ############################
        ####convert Data
        my_command_data_class_array = my_SuiteFileObject.convert_to_command_data_class_array()

        ############################
        ## Run Test Here
        self.main_test_run_action(web_driver, my_command_data_class_array)
        ## Run Test Here
        ############################

        # here
        # here
        # here
        # here
        # here
        # here



        #my_command_data_class_array = my_SuiteFileObject.
        #self.main_test_run_action(web_driver, my_command_data_class_array)


    ##########
    #####
    ## Setter
    #####
    ##########


    def main_test_run_action(self, web_driver, my_command_data_class_array):

        ############################
        ## Set Test Data
        self.the_CommandDataObject = CommandDataObject(my_command_data_class_array)
        my_count = 0

        for my_command_data in my_command_data_class_array:
            pass

            ############################
            ## Break

            ############################
            ## Pause

            ############################
            ## Set Current Case number

            ############################
            ## Write Console Output

            ############################
            ## Write time Map

            ############################
            ## Write Command Log

            ############################
            ## RUN TEST HERE !!!
            self.the_CommandDataObject.set_current_command_data(my_command_data)
            self.the_CommandDataObject.set_current_command_number(self.run_api_command(self.the_CommandDataObject))
            ## RUN TEST HERE !!!
            ############################

            ############################
            ## Update Count
            my_count += 1


    ##########
    #####
    ## Consumption
    #####
    ##########


    def run_api_command(self, my_command_data):
        return self.the_CommandProcessActionClass.api_command_consumption(my_command_data)
        #returns an int


    ##########
    #####
    ## Navigate To URL
    #####
    ##########

    @staticmethod
    def navigate_to_initial_url(web_driver, url):
        sleep(1)
        try:
            web_driver.get(url)
        except StandardError:
            pass
        sleep(3)
