import json


class DataClass:
    def __init__(self, name, object_id, display_order):
        self.name = name
        self.object_id = object_id
        self.display_order = display_order


    def print_object(self):
        print("name :: " + self.name)
        print("object_id :: " + self.object_id)
        print("display_order :: " + self.display_order)


    def get_name(self):
        return self.name


    def set_id(self, object_id):
        self.object_id = object_id


    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
