#while and for  s = 1 + 3 + 5 + ... + 100 and s2= 0 + 2 + 4 + ... + 100
i = 0
s1 = 0
while i <= 100:
    if (i%2)!= 0:
        s1 += i
        i += 1
    else:
        i+=1
        continue

print(s1)

i = 0
s2 = i
for num in range(0,101):
    if i % 2 == 0:
        s2 += i
        i +=1 
    else:
        i += 1 
        continue
print(s2)

'''s = 0
for i in range(0,101,2):
    s+=i
print(s)'''
