from MainController.CommandCore.ActionClasses.AbstractActions import AbstractActions
from time import sleep


class LifeCycleActions(AbstractActions):

    def __init__(self, the_Reporter, the_observer_service):
        AbstractActions.__init__(self, the_Reporter)
        self.the_observer_service = the_observer_service


    ##########
    #####
    ## API
    #####
    ##########


    def commentAction(self):
        pass

    def consoleAction(self, my_CommandDataObject):
        my_api = my_CommandDataObject.get_current_command_api_value()
        print("   - Console :: " + my_api)

    def finishedAction(self, my_CommandDataObject):
        pass

    def waitAction(self, my_CommandDataObject):
        sleep_time = my_CommandDataObject.get_current_command_api_value()
        sleep(sleep_time)

    def checkTestCaseWithIDAction(self, my_CommandDataObject):
        my_api = my_CommandDataObject.get_current_command_api_value()

    def failTestAction(self):
        pass

    def breakAndFinishTestNowAction(self):
        pass
