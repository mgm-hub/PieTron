

class CommandDataClass:
    def __init__(self, api_name, api_value):
        self.api_name = api_name
        self.api_value = api_value


    def get_api_name(self):
        # print("CommandDataClass.api_name :: " + self.api_name)
        return self.api_name


    def get_api_value(self):
        # print("CommandDataClass.api_value " + self.api_value)
        return self.api_value


    def has_value(self):
        if self.api_name is not None and len(self.api_name) > 0 and self.api_value is not None and len(self.api_value) > 0:
            return True
        else:
            return False
