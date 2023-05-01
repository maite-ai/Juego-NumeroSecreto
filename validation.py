class Validation():
    def __init__(self, value):
        self.value = value
        
    def is_number(self, value):
        return isinstance(value, (int, float, complex))
