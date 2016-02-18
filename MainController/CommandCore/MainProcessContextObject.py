from MainController.DriverCore.SeleniumDriver import SeleniumDriver


class MainProcessContextObject:
    the_webDriver = None

    def __init__(self, the_ObserverService, the_MainProcessSharedDataGroup, the_SuiteBuildDataProcess):
        the_WebDriver = None
        the_Reporter = None
        # the_JSONDictionaryData
        #
        #
        self.the_ObserverService = the_ObserverService
        self.the_MainProcessSharedDataGroup = the_MainProcessSharedDataGroup
        self.the_SuiteBuildDataProcess = the_SuiteBuildDataProcess
        #
        #
        #
        self.basic_init()



    ##########
    #####
    ##
    #####
    ##########

    def basic_init(self):
        print("what")
        text = self.the_SuiteBuildDataProcess.the_SuiteBuildData.browserName
        print(text)
        pass
        ##################
        ## Build Reporter
        #reporter here

        ##################
        ## Build Web Driver
        suite_build_data = self.the_SuiteBuildDataProcess.get_suite_build_data()
        browser_name = suite_build_data.get_browser_name()
        self.init_web_driver(browser_name, None)
        print(browser_name)

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


    def get_my_suite_file_object(self, test_number):
        return self.the_SuiteBuildDataProcess.get_suite_file_object_from_data_process(test_number)


    ##########
    #####
    ##
    #####
    ##########


    ##########
    #####
    ##
    #####
    ##########
