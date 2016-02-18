from MainController.DriverCore.SeleniumDriver import SeleniumDriver


class MainProcessContextObject:
    the_webDriver = None

    def __init__(self, the_ObserverService, the_MainProcessSharedDataGroup, the_SuiteBuildDataProcess):
        the_WebDriver = None
        the_Reporter = None
        self.the_ObserverService = the_ObserverService
        self.the_MainProcessSharedDataGroup = the_MainProcessSharedDataGroup
        self.the_SuiteBuildDataProcess = the_SuiteBuildDataProcess
        pass


    ##########
    #####
    ##
    #####
    ##########


    def init_web_driver(self, browser_name, over_ride_url):
        try:
            self.the_WebDriver = SeleniumDriver.get_browser_by_name(browser_name)
        except StandardError:
            None


    ##########
    #####
    ##
    #####
    ##########


    def get_web_driver(self):
        return self.the_WebDriver


    def get_command_data_class_array(self):
        return self.the_SuiteBuildDataProcess