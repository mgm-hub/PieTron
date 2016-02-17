import ast


class TextActions:
    def __init__(self):
        pass


    @staticmethod
    def print_dictionary(my_dictionary):
        for key, value in my_dictionary.iteritems() :
            print (key, value)


    @staticmethod
    def convert_string_to_dictionary(my_dictionary):
        try:
            return ast.literal_eval(str(my_dictionary))
        except StandardError:
            return None

