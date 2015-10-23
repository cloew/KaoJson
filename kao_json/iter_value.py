
def IterValue(value):
    """ Return an iterable for the value """
    if hasattr(value, '__iter__'):
        return value
    else:
        return (value,)