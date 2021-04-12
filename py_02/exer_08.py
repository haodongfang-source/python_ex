# exer8
import random
computer = random.randint(1,3)
#print(computer)
player = int(input('请输入您的拳 石头（1）/剪刀（2）/布（3）：'))
if computer > player:
    print('"computer vs player" ,you lose \n computer is ',computer)
elif computer == player:
    print(' "computer vs player" \n equal',computer, player)
else:
    print('"computer vs player",you win',computer)
