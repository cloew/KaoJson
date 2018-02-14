
def IterWrapper(value):
    """ Return an iterable for the value """
    if type(value) is tuple:
        return value
    else:
        return (value,)