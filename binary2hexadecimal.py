def convert(n,x):
    if n==0 or n==1:
        return n
    else:
        return n%10+x*convert(n//10,x)

def dec2hex(a):
    h=''
    while a>0:
        i=a%16
        if i//16==0:
            h+=str(i)
        else:
            h+=chr(i+87)
        a=a//16
    return h[::-1]
n=int(input("enter one binary no.r"))
print(convert(n,2))
m=int(input("enter one octal"))
print(dec2hex(convert(m,8)))