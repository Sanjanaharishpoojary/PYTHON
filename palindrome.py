a=input("enter input")
if a==a[::-1]:
    print("palindrome")
else:
    print("not a palindrome")

for i in range(10):
    if str(a).count(str(i))!=0:
        print(i,"=",str(a).count(str(i)))
