
class ViaFn:
    """ Provides a value from a fn """
    
    def __init__(self, fn, requires=[]):
        """ Initialize with the fn and the list of required additional arguments """
        self.fn = fn
        self.requiredArgs = requires
        
    def __call__(self, context):
        """ Return the value for the context """
        args = [getattr(context.args, argName) for argName in self.requiredArgs]
        return self.fn(context.obj, *args)