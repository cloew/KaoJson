
class ViaAttr:
    """ Provides a corresponding attr for the Provider Context """
    
    def __init__(self, attr=None):
        """ Initialize with the attr name """
        self.attr = attr
        
    def __call__(self, context):
        """ Return the value for the context """
        return getattr(context.obj, self.getAttrName(context))
        
    def getAttrName(self, context):
        """ Return the attr name """
        return self.attr if self.attr is not None else context.attr