import re
def isphonenumber(n):
    if len(n)!=12:
        return False
    for i in range(len(n)):
        if i==3 or i==7:
            if n[i]!='-':
                return False
        else:
            if n[i].isdigit()==False:
                return False
    return True

def check(n):
    pat=re.compile(r'^\d{3}-\d{3}-\d{4}$')
    if pat.match(n):
        return True
    else:
        return False
n=input("enter phone number")
print("without")
if isphonenumber(n):
    print("valid")
else:
    print("invalid")
print("with")
if check(n):
    print("valid")
else:
    print("invalid")