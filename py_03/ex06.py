user_name = "admin"
password = "123"

num = 3
count = 0

while count <= num: 
    print("请输入您的账号：")
    user_input_name = input()
    #user_input_password = input()
    if user_input_name == user_name :
        print("请输入您的密码：")
        user_input_password = input()
        count += 1
        if user_input_password == password :
            print("登录成功")
            break
        else:
            print("密码错误")
            if count == 3:
                print("输入次数过多，请稍后重试")
                break
    else:
        print("账户名称错误")

'''
if count == 3:
    print("输入次数过多，请稍后重试")'''
