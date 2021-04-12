#print "*"
for num1 in range(1,10):
    for num2 in range(1,num1+1):
        print("*",end="")
    print()

#print 9 * 9
for num1 in range(1,10):
    for num2 in range(1,num1+1):
        print(num2, "*", num1, "=", num1 * num2, end="  ")
    print()


