import json
from MainController.DataCore.CommandDataClass import CommandDataClass
from collections import OrderedDict

class SuiteFileObject:
    def __init__(self, testID, suiteName, baseURL, overRideURL, description, apiList, hasOverRideURL, commandDataClassList):
        self.testID = testID
        self.suiteName = suiteName
        self.baseURL = baseURL
        self.overRideURL = overRideURL
        self.description = description
        self.apiList = apiList
        self.hasOverRideURL = hasOverRideURL
        self.commandDataClassList = commandDataClassList


    def get_command_data_class_list(self):
        return self.commandDataClassList

    def get_suite_name(self):
        return self.suiteName

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    ##########
    #####
    ## Stuff and Things
    #####
    ##########

    def convert_to_command_data_class_array(self):
        print("hhihihi")
        command_data_class_array = []
        my_dictionary = OrderedDict(self.commandDataClassList)
        for item in self.commandDataClassList:

            print (item)
        return command_data_class_array


