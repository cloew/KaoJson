
class A:
    def __init__(self, value):
        self.value = value
        
class AChild(A):
    pass
    
class AGrandchild(AChild):
    pass