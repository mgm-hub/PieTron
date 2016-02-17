import json


class SuiteFileObject:
    def __init__(self, testID, suiteName, overRideURL, description, apiList, hasOverRideURL, commandDataClassList):
        self.testID = testID
        self.suiteName = suiteName
        self.overRideURL = overRideURL
        self.description = description
        self.apiList = apiList
        self.hasOverRideURL = hasOverRideURL
        self.commandDataClassList = commandDataClassList


    def get_command_data_class_list(self):
        return self.commandDataClassList


    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

