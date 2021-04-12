#input three numbers and print them.

i = 1
for num in range(3):
    print("请输入第",i,"个数:",end="")
    num = input()
    print("第",i,"个数是：",num)
    i+=1
