class pal:
    def pali(self):
        pass

class stg(pal):
    def __init__(self):
        self.s=input("enter string")

    def pali(self):
        if self.s==self.s[::-1]:
            print("yes")
        else:
            print("no")

a=stg()
a.pali()