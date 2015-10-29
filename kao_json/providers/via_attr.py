
class ViaAttr:
    """ Provides a corresponding attr for the Provider Context """
    
    def __init__(self, name=None):
        """ Initialize with the attr name """
        self.name = name
        
    def __call__(self, context):
        """ Return the value for the context """
        return getattr(context.obj, self.getName(context))
        
    def getName(self, context):
        """ Return the name """
        return self.name if self.name is not None else context.name