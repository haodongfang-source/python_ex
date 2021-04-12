# exer06
#BMI = weight / hight

weight_in = float (input('请输入体重(公斤）：'))
hight_in = float (input('请输入身高（公尺）:'))
BMI_in = weight_in / (hight_in * hight_in)
if BMI_in < 18.5:
    print('体重过轻 BMI = ',BMI_in)
elif 18.5 <= BMI_in <= 23.9:
    print('正常 BMI = ', BMI_in)
elif 24 <= BMI_in <= 27:
    print('过重 BMI = ', BMI_in)
elif 28 <= BMI_in <= 32:
    print('肥胖 BMI = ', BMI_in)
else:
    print('非常肥胖 BMI = ', BMI_in)
