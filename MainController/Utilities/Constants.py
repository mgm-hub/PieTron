import os


class Constants:
    def __init__(self):
        pass


    CLASS_NAME = "CONSTANTS"
    IS_DEBUG = True
    MAIN_INIT_MESSAGE = "Main Process Started"
    ACTION_SERVICE_INIT_MESSAGE = "Action Service Started"
    OBSERVER_SERVICE_INIT_MESSAGE = "Action Service Started"
    MESSAGE = "MESSAGE"
    TEST = "TEST"
    JSON_TAG = ".json"
    RUN_ERROR = "Method Could Not Be Found"
    SPACE_EMPTY = " "
    SPACE_COLOGNE = " :: "

    FULL_PATH = os.path.realpath(__file__)
    DIRECTORY = (os.path.dirname(FULL_PATH))
    RESOURCE_LOCATION_NAME = "\Resources\\"
    RESOURCE_DIRECTORY = os.getcwd() + RESOURCE_LOCATION_NAME
    CHROME_WIN_FILE_NAME = "chromedriver.exe"
    CHROME_DRIVER_LOCATION_WIN = RESOURCE_DIRECTORY + CHROME_WIN_FILE_NAME
