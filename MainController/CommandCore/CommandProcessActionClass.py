from MainController.Utilities.Log import Log
from MainController.Utilities.Constants import Constants
from MainController.DataCore.CommandDataObject import CommandDataObject
from MainController.CommandCore.APIList import APIList


METHOD_PREFIX = "api_"


class CommandProcessActionClass:
    def __init__(self):
        pass


    def api_command_consumption(self, the_command_data_object):
        api_name = the_command_data_object.get_api_name()
        if APIList.has_api(api_name):
            self.run_method_by_name(api_name)
        else:
            Log.log(Constants.COMMAND_CASE_ERROR)
        the_command_data_object.set_current_command_number(the_command_data_object.get_current_command_number() + 1)
        return the_command_data_object.get_current_command_number()


    def run_method_by_name(self, method_name, *args, **kwargs):
        try:
            getattr(self, method_name)(*args, **kwargs)
        except StandardError:
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
