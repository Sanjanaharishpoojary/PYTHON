import re
phn=re.compile(r'\+\d{12}')
email=re.compile(r'[A-Za-z0-9._]+@[A-Za-z0-9]+\.[A-Za-z]')
with open('meee','r') as f:
    for i in f:
        m=phn.findall(i)
        for n in m:
            print(n)
        m =email.findall(i)
        for n in m:
            print(n)
