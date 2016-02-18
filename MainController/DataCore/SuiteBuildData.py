from MainController.DataCore.SuiteBuildDataProcess import SuiteBuildDataProcess
from MainController.DataCore.SharedDataActions import SharedDataActions


class SuiteBuildData:

    def __init__(self, testID, testName, testDescription, overRideURL, browserName, serviceName, suiteGroup, suiteFileName, suiteNumberList):
        self.testID = testID
        self.testName = testName
        self.testDescription = testDescription
        self.overRideURL = overRideURL
        self.browserName = browserName
        self.serviceName = serviceName
        self.suiteGroup = suiteGroup
        self.suiteFileName = suiteFileName
        self.suiteNumberList = suiteNumberList


    ##########
    #####
    ## Simple Getters
    #####
    ##########


    def get_browser_name(self):
        return self.browserName


    ##########
    #####
    ## Build SuiteBuildDataProcess from Build Data
    #####
    ##########


    def build_suite_build_data_process(self, my_SuiteBuildData):
        group_name = my_SuiteBuildData.suiteGroup
        file_name = my_SuiteBuildData.suiteFileName
        my_SuiteFileObjectShell = SharedDataActions.get_suite_shell_from_group_and_file(group_name, file_name)
        return SuiteBuildDataProcess(my_SuiteBuildData, my_SuiteFileObjectShell)


