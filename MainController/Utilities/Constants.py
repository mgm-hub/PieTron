import os


class Constants:
    def __init__(self):
        pass

    ##########
    #####
    ##
    #####
    ##########

    CLASS_NAME = "CONSTANTS"
    IS_DEBUG = True
    MAIN_INIT_MESSAGE = "Main Process Started"
    ACTION_SERVICE_INIT_MESSAGE = "Action Service Started"
    OBSERVER_SERVICE_INIT_MESSAGE = "Action Service Started"
    MESSAGE = "MESSAGE"
    TEST = "TEST"
    RUN_ERROR = "Method Could Not Be Found"
    SPACE_EMPTY = " "
    SPACE_COLOGNE = " :: "

    ##########
    #####
    ##
    #####
    ##########

    FULL_PATH = os.path.realpath(__file__)
    DIRECTORY = (os.path.dirname(FULL_PATH))
    PROJECT_DIRECTORY = os.getcwd()
    PATH_SLASH = "/"
    JSON_TAG = ".json"

    ##########
    #####
    ##
    #####
    ##########

    RESOURCE_NAME = "Resources"
    RESOURCE_DIRECTORY = PROJECT_DIRECTORY + PATH_SLASH + RESOURCE_NAME + PATH_SLASH
    CHROME_WIN_FILE_NAME = "chromedriver.exe"
    CHROME_DRIVER_LOCATION_WIN = RESOURCE_DIRECTORY + CHROME_WIN_FILE_NAME

    ##########
    #####
    ## Codex
    #####
    ##########

    WEB_DATA_NAME = "WebData"
    CODEX_NAME = "Codex"
    CODEX_DIRECTORY = RESOURCE_NAME + PATH_SLASH + WEB_DATA_NAME + PATH_SLASH + CODEX_NAME

    SUITE_NAME = "SuiteFileGroups"
    SUITE_DIRECTORY = RESOURCE_NAME + PATH_SLASH + WEB_DATA_NAME + PATH_SLASH + SUITE_NAME

    ##########
    #####
    ##
    #####
    ##########

    REMOTE_DRIVER_ADDRESS = "http://127.0.0.1"
    REMOTE_DRIVER_PORT = "4444"
    REMOTE_GRID_STATUS_PAGE = 'http://localhost:4444/grid/console/test'
    OK_RESPONSE_CODE = "200"
