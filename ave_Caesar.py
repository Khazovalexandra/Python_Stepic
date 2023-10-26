first_str = input().split()
str=''

for j in first_str:
    count = 0
    for i in range(len(j)):
        if j[i].isalpha():
            count += 1
        
    for k in j:
        if k.isalpha() and k.islower():
            str += chr((ord(k) - 97 + count) % 26 + 97)
        elif k.isalpha() and k.isupper():
            str += chr((ord(k) - 65 + count) % 26 + 65)
        else:
            str += k
            
    str += ' '

str = str.rstrip(' ')
                 
print(str)