from Constants import *

__author__ = 'mmoscatello'


class Log:
    def __init__(self):
        pass

    @staticmethod
    def log(my_string):
        pass
        if Constants.IS_DEBUG:
            print(my_string)
