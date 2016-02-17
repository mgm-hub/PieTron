import json


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

