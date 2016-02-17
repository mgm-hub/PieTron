from MainController.Utilities.Log import Log
from MainController.Utilities.Constants import Constants
from MainController.DataCore.CommandDataObject import CommandDataObject


class CommandProcessRun:
    the_command_data_object = None

    def __init__(self):
        pass


    def run_action_init(self):
        Log.log(Constants.STARTING_TEST)

        ############################
        ## Get Context Object with WebDriver

        ############################
        ## Gets Test Data Array Here

        ############################
        ## Navigate To Start Page

        ############################
        ## Run Test Here


    def main_test_run_action(self, my_command_data_class_array):

        the_command_data_object = CommandDataObject(my_command_data_class_array)

        my_count = 0
        for my_command_data in my_command_data_class_array:
            pass

            the_command_data_object.set_current_command_number(my_count)



