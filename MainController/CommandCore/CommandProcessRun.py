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


    def run_action_init(self):
        Log.log(Constants.STARTING_TEST)

        ############################
        ## Get Context Object with WebDriver

        ############################
        ## Gets Test Data Array Here
        my_SuiteFileObject = self.the_MainProcessContextObject

        ############################
        ## Navigate To Start Page

        ############################
        ## Run Test Here
        #suiteFileObject.get_command_data_class_list()
        web_driver = self.the_MainProcessContextObject.get_web_driver()
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

        self.the_CommandDataObject = CommandDataObject(my_command_data_class_array)
        my_count = 0

        for my_command_data in my_command_data_class_array:
            pass

            ############################
            ## RUN TEST HERE !!!
            self.the_CommandDataObject.set_current_command_data(my_command_data)
            self.the_CommandDataObject.set_current_command_number(self.run_api_command(self.the_CommandDataObject))
            ## RUN TEST HERE !!!
            ############################

            my_count += 1


    ##########
    #####
    ## Consumption
    #####
    ##########


    def run_api_command(self, my_command_data):
        return self.the_CommandProcessActionClass.api_command_consumption(my_command_data)