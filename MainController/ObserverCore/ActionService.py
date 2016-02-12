from time import sleep
import multiprocessing
from threading import Thread
from MainController.Utilities.Log import Log
from MainController.Utilities.Constants import Constants
from MainController.FileCore.FileService import *


class ActionService:
    the_observer_service = None

    def __init__(self, the_observer_service):
        if ActionService.the_observer_service is None:
            ActionService.the_observer_service = the_observer_service


    ##########
    #####
    ## Test
    #####
    ##########


    def TEST_action_service(self):
        Log.log(Constants.TEST)
        self.the_observer_service.TEST_observering_service_print()
