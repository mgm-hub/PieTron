from MainController.CommandCore.ActionClasses.AbstractActions import AbstractActions


class StorageActions(AbstractActions):

    def __init__(self, the_Reporter):
        AbstractActions.__init__(self, the_Reporter)


    ##########
    #####
    ## API
    #####
    ##########


    def storeKeyAndValueAction(self):
        pass