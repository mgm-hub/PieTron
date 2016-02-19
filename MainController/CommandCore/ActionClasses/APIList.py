

API_LIST = [
            "clickElement",
            "elementIsVisible",
            "storeWebElementCSSValueToKeyNamed",
            "COMMENT",
            "CONSOLE",

            "finished",
            "wait",
            "navigateToURL",
            "writeToElement",
            "storeKeyAndValue",

            "clearTextField",
            "checkTestCaseWithID",
            "failTest",
            "closeBrowser",
            "breakAndFinishTestNOW"
            ]


class APIList:
    def __init__(self):
        pass

    @staticmethod
    def has_api(my_string):
        if my_string in API_LIST:
            return True

