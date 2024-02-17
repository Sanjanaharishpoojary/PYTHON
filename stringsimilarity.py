a=input("enter twο strings")
b=input()
if len(a)>len(b):
    l=len(a)
    s=len(b)
else:
    l=len(b)
    s=len(a)
c=0
for i in range(s):
    if a[i]==b[i]:
        c+=1

print("string similarity=",c/l)