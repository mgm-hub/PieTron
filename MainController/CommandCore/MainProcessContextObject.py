from MainController.DriverCore.SeleniumDriver import SeleniumDriver


class MainProcessContextObject:
    the_webDriver = None

    def __init__(self, the_Observer_service, the_SharedData):
        self.the_Observer_service = the_Observer_service
        self.the_SharedData = the_SharedData

        pass


    def init_web_driver(self, browser_name, over_ride_url):
        try:
            self.the_webDriver = SeleniumDriver.get_browser_by_name(browser_name)
        except StandardError:
            None
