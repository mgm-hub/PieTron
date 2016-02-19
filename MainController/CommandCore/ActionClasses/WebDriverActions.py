from MainController.CommandCore.ActionClasses.AbstractActions import AbstractActions


class WebDriverActions(AbstractActions):


    def __init__(self, the_Reporter, the_MainProcessContextObject):
        AbstractActions.__init__(self, the_Reporter, the_MainProcessContextObject)
        #build selenium actions


    ##########
    #####
    ## API 1-5
    #####
    ##########

    def clickElementAction(self):
        pass

    def elementIsVisibleAction(self):
        pass

    def storeWebElementCSSValueToKeyNamedAction(self):
        pass

    def navigateToURLAction(self):
        pass

    def writeToElementAction(self):
        pass

    def clearTextFieldAction(self):
        pass

    def closeBrowserAction(self):
        pass