import math
for num in range(1,10001):
    x = int (math.sqrt(num + 100))
    y = int (math.sqrt(num + 268))
    if (x ** 2 == num + 100) and (y ** 2 == num + 268):
        print(num)
