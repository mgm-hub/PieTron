from MainController.Utilities.Log import Log
from MainController.Utilities.Constants import Constants
from MainController.DataCore.CommandDataObject import CommandDataObject
from MainController.CommandCore.APIList import APIList


METHOD_PREFIX = "api_"


class CommandProcessActionClass:
    def __init__(self, the_WebDriver):
        self.the_WebDriver = the_WebDriver

    def api_command_consumption(self, the_command_data_object):
        api_name = the_command_data_object.get_current_command_api_name()
        #print("api_name :: " + api_name)
        if APIList.has_api(api_name):
            self.run_method_by_name(METHOD_PREFIX + api_name, the_command_data_object)
        else:
            Log.log(Constants.COMMAND_CASE_ERROR + Constants.SPACE_COLOGNE + str(api_name))
        the_command_data_object.set_current_command_number(the_command_data_object.get_current_command_number() + 1)
        return the_command_data_object.get_current_command_number()


    def run_method_by_name(self, method_name, *args, **kwargs):
        #print ("Running :: " + method_name)
        try:
            getattr(self, method_name)(*args, **kwargs)
        except Exception:
            print ("Invalid Run Method")
            return None


    ##########
    #####
    ## API
    #####
    ##########


    def api_COMMENT(self, my_command_data_object):
        print("comment")


    def api_CONSOLE(self, my_command_data_object):
        print("console")

    def api_clickElement(self, my_command_data_object):
        print(" ")
        print("api_clickElement")
        print(my_command_data_object.get_current_command_api_name())
        print(my_command_data_object.get_current_command_api_value())
