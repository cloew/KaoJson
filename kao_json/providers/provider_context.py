from kao_dict import KaoDict

class ProviderContext:
    """ Represents the context for converting using a provider """
    
    def __init__(self, name, obj, args):
        """ Initialize with the attr name, object, and args """
        self.name = name
        self.obj = obj
        self.args = KaoDict(args)