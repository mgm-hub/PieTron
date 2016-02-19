from MainController.CommandCore.ActionClasses.AbstractActions import AbstractActions
from time import sleep


class LifecycleActions(AbstractActions):

    def __init__(self, the_Reporter):
        AbstractActions.__init__(self, the_Reporter)


    ##########
    #####
    ## API
    #####
    ##########


    def comment_action(self):
        pass

    def console_action(self, my_CommandDataObject):
        my_api = my_CommandDataObject.get_current_command_api_value()
        print("   - Console :: " + my_api)

    def finished_action(self, my_CommandDataObject):
        pass

    def wait_action(self, my_CommandDataObject):
        sleep_time = my_CommandDataObject.get_current_command_api_value()
        sleep(sleep_time)

    def check_test_case_with_id_action(self, my_CommandDataObject):
        my_api = my_CommandDataObject.get_current_command_api_value()

    def fail_test_action(self):
        pass

    def break_and_finish_test_namow_action(self):
        pass
