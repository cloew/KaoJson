from json_attr import JsonAttr

class KeywordAttr(JsonAttr):
    """ Represents an attribute for the JSON that is based on a configured kwarg """
    
    def __init__(self, name, keyword=None):
        """ Initialize the keyword attribute """
        if keyword is None:
            keyword = name
        JsonAttr.__init__(self, name, self.getKeyword, args=[keyword])
        self.keyword = keyword
        
    def getKeyword(self, object, keywordValue):
        """ Return the keyword argument """
        return keywordValue