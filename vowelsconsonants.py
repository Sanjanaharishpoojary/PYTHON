a = input("Enter string: ")
a = a.upper()
v = 0
c = 0

for i in range(0, len(a)):
    if a[i] in ['A', 'E', 'I', 'O', 'U']:
        v = v + 1
    else:
        c = c + 1

print("The number of vowels =", v, "The number of consonants =", c)
