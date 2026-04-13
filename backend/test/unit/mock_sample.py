
class A:
    """
    Create a A class
    Returning the value of B.getValue function
    """
    def __init__(self, B):
        self.b = B

    def get_b_value(self):
        return self.b.getValue
    
class B:
    def get_b_value():
        """return then number 5"""
        pass
