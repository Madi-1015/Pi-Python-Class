class rectangle:
    
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

r1 = rectangle(10,25) 

print(r1.area())