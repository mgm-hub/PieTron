from MainController.Utilities.HttpActions import HttpActions
from MainController.Utilities.Constants import Constants
from MainController.Utilities.Log import Log



class GridActions:
    def __init__(self):
        pass

    @staticmethod
    def is_grid_running():
        response_code = HttpActions.get_page_response_code(Constants.REMOTE_GRID_STATUS_PAGE)
        if response_code is not None and response_code == Constants.OK_RESPONSE_CODE:
            return True
        else:
            return False



