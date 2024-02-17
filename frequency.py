a=int(input("entwr multidigit number"))
for i in range(10):
    if str(a).count(str(i))!=0:
        print(i,"=",str(a).count(str(i)))