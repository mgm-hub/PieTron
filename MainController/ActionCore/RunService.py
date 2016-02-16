from MainController.Utilities.Log import Log
from MainController.Utilities.Constants import Constants
from time import sleep
import multiprocessing
from threading import Thread

class RunService:
    def __init__(self):
        pass


    ##########
    #####
    ## Main Init
    #####
    ##########


    def main_init(self):
        print("RunProcess")
        pass
        self.run_list(["TEST_thread_completed", "process_two"])


    ##########
    ####
    ## Run From List
    #####
    ##########


    def run_list(self, method_list):
        for method_name in method_list:
            try:
                method_to_call = getattr(self, method_name)
                method_to_call()
            except Exception:
                Log.log(Constants.RUN_ERROR + Constants.SPACE_COLOGNE + method_name)


    ##########
    ####
    ## Run Methods
    #####
    ##########

    def TEST_thread_completed(self):
        myThread = Thread(target=self.TEST_end_of_thread, args=())
        myThread.start()

    def TEST_end_of_thread(self):
        sleep(5)
        print("End of Thread")

    def process_one(self):
        print("one")

    def process_two(self):
        print("two")
