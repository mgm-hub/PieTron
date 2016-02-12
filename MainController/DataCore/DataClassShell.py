import json


class DataClassShell():
    def __init__(self, dataClass):
        self.dataClass = dataClass


    def get_data_class(self):
        return self.dataClass


    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)