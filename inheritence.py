import math
class shapes:
    def calc(self):
        pass

    def disp(self,area):
        print("area=",area)

class circle(shapes):
    def __init__(self):
        self.r=float(input("enter radius"))

    def calc(self):
        self.area=math.pi*self.r*self.r
        return self.area

class triangle(shapes):
    def __init__(self):
        self.a=float(input("enter three sides"))
        self.b=float(input())
        self.c=float(input())

    def calc(self):
        self.s=(self.a+self.b+self.c)/2
        self.area=math.sqrt(self.s*(self.s-self.a)*(self.s-self.b)*(self.s-self.c))
        return self.area

class rectangle(shapes):
    def __init__(self):
        self.l=float(input("enter l and b"))
        self.w=float(input())

    def calc(self):
        self.area=2*(self.l+self.w)
        return self.area

p=circle()
area=p.calc()
p.disp(area)
q=rectangle()
area=q.calc()
q.disp(area)
r=triangle()
area=r.calc()
r.disp(area)
