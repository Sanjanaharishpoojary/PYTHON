n=input("enter one sentence")
l=u=w=d=0
w=len(n.split())
for i in n:
    if i.isdigit():
        d+=1
    if i.islower():
        l+=1
    if i.isupper():
        u+=1
print("lower=",l,"upper=",u,"digits=",d,'words=',w)