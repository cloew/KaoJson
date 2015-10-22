
class ListBuilder:
    """ Helper class to build JSON Lists """
    
    def __init__(self, values):
        """ Initialize with the values to build """
        self.values = values
        
    def build(self, context):
        """ Builds a JSON List """
        return [context.newConverter(value).toJson(context) for value in self.values]