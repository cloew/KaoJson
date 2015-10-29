from kao_dict import KaoDict

class ProviderContext:
    """ Represents the context for converting using a provider """
    
    def __init__(self, attr, obj, args):
        """ Initialize with the attr name, object, and args """
        self.attr = attr
        self.obj = obj
        self.args = KaoDict(args)