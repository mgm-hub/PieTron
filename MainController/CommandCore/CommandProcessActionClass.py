from MainController.Utilities.Log import Log
from MainController.Utilities.Constants import Constants
from MainController.CommandCore.ActionClasses.APIList import APIList
from MainController.CommandCore.ActionClasses.LifeCycleActions import LifeCycleActions
from MainController.CommandCore.ActionClasses.WebDriverActions import WebDriverActions
from MainController.CommandCore.ActionClasses.StorageActions import StorageActions


METHOD_PREFIX = "api_"


class CommandProcessActionClass:
    the_LifeCycleActions = None
    the_WebDriverActions = None
    the_StorageActions = None

    def __init__(self, the_WebDriver, the_MainProcessContextObject):
        self.the_WebDriver = the_WebDriver
        self.the_MainProcessContextObject = the_MainProcessContextObject
        ##
        ##
        ##
        self.basic_init()


    ##########
    #####
    ## Init
    #####
    ##########

    def basic_init(self):
        the_reporter = self.the_MainProcessContextObject.get_the_reporter()
        the_observer_service = self.the_MainProcessContextObject.get_the_observer_service()
        self.the_LifeCycleActions = LifeCycleActions(the_reporter, the_observer_service)
        self.the_WebDriverActions = WebDriverActions(the_reporter, self.the_MainProcessContextObject)
        self.the_StorageActions = StorageActions(the_reporter)


    ##########
    #####
    ## Consumption
    #####
    ##########

    def api_command_consumption(self, the_command_data_object):
        api_name = the_command_data_object.get_current_command_api_name()
        #print("api_name :: " + api_name)
        if APIList.has_api(api_name):
            self.run_method_by_name(METHOD_PREFIX + api_name, the_command_data_object)
        else:
            Log.log(Constants.COMMAND_CASE_ERROR + Constants.SPACE_COLOGNE + str(api_name))
        the_command_data_object.set_current_command_number(the_command_data_object.get_current_command_number() + 1)
        return the_command_data_object.get_current_command_number()


    def run_method_by_name(self, method_name, *args, **kwargs):
        #print ("Running :: " + method_name)
        try:
            getattr(self, method_name)(*args, **kwargs)
        except Exception:
            print ("Invalid Run Method")
            return None


    ##########
    #####
    ## API 1-5
    #####
    ##########

    def api_clickElement(self, my_command_data_object):
        print(my_command_data_object.get_current_command_api_name())
        print(my_command_data_object.get_current_command_api_value())
        self.the_WebDriverActions.clickElementAction()

    def api_elementIsVisible(self, my_command_data_object):
        pass

    def api_storeWebElementCSSValueToKeyNamed(self, my_command_data_object):
        pass

    def api_COMMENT(self, my_command_data_object):
        print("comment")

    def api_CONSOLE(self, my_command_data_object):
        print("console")

    ##########
    #####
    ## API 6-10
    #####
    ##########

    def api_finished(self, my_command_data_object):
        pass

    def api_wait(self, my_command_data_object):
        pass

    def api_navigateToURL(self, my_command_data_object):
        pass

    def api_writeToElement(self, my_command_data_object):
        pass

    def api_storeKeyAndValue(self, my_command_data_object):
        pass


    ##########
    #####
    ## API 11-15
    #####
    ##########

    def api_clearTextField(self, my_command_data_object):
        pass

    def api_checkTestCaseWithID(self, my_command_data_object):
        pass

    def api_failTest(self, my_command_data_object):
        pass

    def api_writeTapi_closeBrowseroElement(self, my_command_data_object):
        pass

    def api_breakAndFinishTestNOW(self, my_command_data_object):
        pass