__author__ = 'mmoscatello'


class RunProcess:
    def __init__(self):
        pass

    ##########
    #####
    ## Main
    #####
    ##########


    def main_init(self):
        print("RunProcess")
        pass
        self.run_list(["process_one"])


    ##########
    ####
    ##Run From List
    #####
    ##########


    def append_run_list(self, method_list):
        my_append_list = []
        for method_name in method_list:
            method_to_call = getattr(self, method_name)
            my_append_list.append(method_to_call())
        return my_append_list

    def run_list(self, method_list):
        for method_name in method_list:
            method_to_call = getattr(self, method_name)
            method_to_call()


    ##########
    ####
    ##Run From List
    #####
    ##########

    def process_one(self):
        print("one")

    def process_two(self):
        print("two")
