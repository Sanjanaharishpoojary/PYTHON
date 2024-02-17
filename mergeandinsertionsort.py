def insert(a):
    for i in range(1,len(a)):
        j=i-1
        x=a[i]
        while j>-1 and a[j]>x:
            a[j+1]=a[j]
            j-=1
        a[j+1]=x

def merge(a):
    if len(a)>1:
        m=len(a)//2
        f=a[:m]
        l=a[m:]
        merge(f)
        merge(l)
        i=j=k=0
        while i<len(f) and j<len(l):
            if f[i]<l[j]:
                a[k]=f[i]
                i+=1
            else:
                a[k]=l[j]
                j+=1
            k+=1
        while i<len(f):
            a[k]=f[i]
            i+=1
            k+=1
        while j<len(l):
            a[k]=l[j]
            j+=1
            k+=1

n=int(input("enter n value"))
list=[]
for i in range(n):
    list.append(int(input()))
merge(list)
print("sorted array: using merge sort",list)
insert(list)
print("using insertion sort",list)
