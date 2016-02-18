import json
import SuiteFileObject
from MainController.DataCore.SuiteFileObject import SuiteFileObject

class SuiteFileObjectShell:
    def __init__(self, group, fileName, fileID, description, suiteFileObjectArray):
        self.group = group
        self.fileName = fileName
        self.fileID = fileID
        self.description = description
        self.suiteFileObjectArray = [suiteFileObjectArray]


    def get_suite_file_object_array(self):
        return self.suiteFileObjectArray


    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)


    ##########
    #####
    ##
    #####
    ##########


    def get_suite_file_object_at_index(self, test_number):
        if self.suiteFileObjectArray is not None:
            my_list_data = self.suiteFileObjectArray[0]
            my_array = []
            for my_suite_file_object in my_list_data:
                suite_file_data = SuiteFileObject(**my_suite_file_object)
                my_array.append(suite_file_data)
            if my_array is not None and len(my_array) > test_number:
                return my_array[test_number]
            else:
                print("Could Not Get Data At index")
        else:
            pass
            print("Could Not Get Data")
