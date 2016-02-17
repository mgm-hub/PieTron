

API_LIST = ["COMMENT",
            "CONSOLE"]


class APIList:
    def __init__(self):
        pass

    @staticmethod
    def has_api(my_string):
        if my_string in API_LIST:
            return True

