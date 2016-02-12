from MainController.Utilities.Log import Log
from MainController.Utilities.Constants import Constants
from MainController.ObserverCore.ActionService import ActionService


class ObserverService:
    the_action_service = None

    def __init__(self):
        if ObserverService.the_action_service is None:
            ObserverService.the_action_service = ActionService(self)


    ##########
    #####
    ## TEST
    #####
    ##########


    def TEST_observer_service_action(self):
        Log.log(Constants.MESSAGE)
        self.the_action_service.TEST_action_service()


    def TEST_observer_service_print(self):
        Log.log(Constants.OBSERVER_SERVICE_INIT_MESSAGE)

