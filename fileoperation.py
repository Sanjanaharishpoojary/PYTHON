import os.path,sys
file=input("enter file name")
if not os.path.isfile(file):
    print("file not found")
    sys.exit(0)
f=open(file,'r')
l=f.readlines()
for i in l:
    print(i)

word=input("enter the word")
cnt=0
for i in l:
    cnt+=i.count(word)

print(word,"appears",cnt,"times")