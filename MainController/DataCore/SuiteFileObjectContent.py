import json


class SuiteFileObjectContent:
    def __init__(self, SuiteFileObject):
        self.SuiteFileObject = SuiteFileObject


    def get_suite_file_object(self):
        return self.SuiteFileObject


    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
