from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from MainController.Utilities.Constants import Constants


class SeleniumDriver:
    def __init__(self):
        pass

    @staticmethod
    def get_broswer_by_name(browser_name):
        if browser_name == "firefox":
            return SeleniumDriver.get_firefox_webdriver()
        elif browser_name == "chrome":
            return SeleniumDriver.get_chrome_webdriver()

    @staticmethod
    def get_firefox_webdriver():
        return webdriver.Firefox()

    @staticmethod
    def get_chrome_webdriver():
        return webdriver.Chrome(Constants.CHROME_DRIVER_LOCATION_WIN)

    @staticmethod
    def get_remote_webdriver():
        command_executor = Constants.REMOTE_DRIVER_ADDRESS + ':' + Constants.REMOTE_DRIVER_PORT + '/wd/hub'
        desired_capabilities = {'platform': 'ANY', 'browserName': 'firefox', 'version': '', 'marionette': False, 'javascriptEnabled': True}

        return webdriver.Remote(command_executor=command_executor,
                                desired_capabilities=desired_capabilities)





'''
cd users
cd mmoscatello

Server and the Hub are set
    java -jar selenium-server.jar -role hub -port 4444
    java -jar selenium-server.jar -role node  -hub http://localhost:4444/grid/register

Web page is set to 5555 and not to the hub at 4444
    http://localhost:5555/wd/hub/static/resource/hub.html
    http://localhost:4444/grid/console
    http://localhost:4444/wd/hub
    http://localhost:5555/wd/hub/static/resource/hub.html
'''