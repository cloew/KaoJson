
class ObjectBuilder:
    """ Helper class to build JSON Objects """
    
    def __init__(self, values):
        """ Initialize with the values to build """
        self.values = values
        
    def build(self, context):
        """ Builds a JSON Object """
        return {key:context.newConverter(value).toJson(context) for key, value in self.values.items()}