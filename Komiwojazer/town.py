import math
class Town:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def __repr__(self):
        return(self.name + " "+ str(self.x)+" " + str(self.y))
        
    def distance(self,other):
        return math.sqrt(math.pow(int(self.x)-int(other.x),2)+math.pow(int(self.y)-int(other.y),2))


