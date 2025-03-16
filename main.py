
import sys
print(sys.path)
sys.path.append("./modules")
print(sys.path)
from mod1 import *

class FourCal:
    def __init__(self,first,second):
        self.first=first
        self.second=second
    def setData(self,first,second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result
class moreFourCal(FourCal):
    def div(sef):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second


Object1 = FourCal(5,6)
Object2 = FourCal(4,7)



print("Object1.add=",Object1.add())
print("Object2.add=",Object2.add())
print("Object1.div=",Object1.div())
print("Object2.div=",Object2.div())

printFirstName("KIM")