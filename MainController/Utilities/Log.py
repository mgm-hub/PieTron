from Constants import *


class Log:
    def __init__(self):
        pass

    @staticmethod
    def log(my_string):
        if Constants.IS_DEBUG:
            print(my_string)
