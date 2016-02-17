from MainController.DataCore.CommandDataClass import CommandDataClass


class CommandDataObject:
    current_command_data = None
    current_command_number = None

    def __init__(self, command_data_class_array):
        self.command_data_class_array = [command_data_class_array]
        self.current_command_number = 0

    ##########
    #####
    ## Get
    #####
    ##########


    def get_current_command_api_name(self):
        if self.current_command_data is not None:
            return self.current_command_data.get_api_name()


    def get_current_command_api_value(self):
        if self.current_command_data is not None:
            return self.current_command_data.get_api_value()


    def get_current_command_number(self):
        return self.current_command_number


    ##########
    #####
    ## Set
    #####
    ##########


    def set_current_command_data(self, current_command_data):
        self.current_command_data = current_command_data


    def set_current_command_number(self, current_command_number):
        self.current_command_number = current_command_number

