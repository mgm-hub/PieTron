

class SuiteBuildDataProcess:
    def __init__(self, the_SuiteBuildData, the_SuiteFileObjectShell):
        self.the_SuiteBuildData = the_SuiteBuildData
        self.the_SuiteFileObjectShell = the_SuiteFileObjectShell


    ##########
    #####
    ##
    #####
    ##########


    def get_suite_file_object_from_data_process(self, test_number):
        return self.the_SuiteFileObjectShell.get_suite_file_object_at_index(test_number)
        #return self.the_SuiteFileObjectShell.


    ##########
    #####
    ##
    #####
    ##########

    def get_suite_build_data(self):
        return self.the_SuiteBuildData
