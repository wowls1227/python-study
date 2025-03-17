
import sys
print(sys.path)
sys.path.append("./modules")
sys.path.append("./packages")
print(sys.path)
from mod1 import *
from packages import *


class FourCal:
    def most(self):
        raise NotImplementedError
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

class MyError(Exception):
    pass

def div3(a,b):
    if b == 0:
        raise MyError()  
    else:
        return a / b

class moreFourCal(FourCal):
    def div(self):
        if self.second == 0:
            raise MyError()
        else:
            return self.first / self.second


Object1 = FourCal(5,6)
Object2 = FourCal(4,7)
try:
    div3(6,0)
except MyError:
    print("0입력하지마세요.")

print("Object1.add=",Object1.add())
print("Object2.add=",Object2.add())
print("Object1.div=",Object1.div())
print("Object2.div=",Object2.div())
print("div3=", div3(6,3))

printFirstName("KIM")

print_package1()