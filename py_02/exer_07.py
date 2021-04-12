ticket = input('有车票请输入 y or Y，否则输入n or N：')
if ticket == 'y' or ticket == 'Y':
    print('\n有车票，可以进站')
    danger_package = input('有危险品输入1，没有着输入0：')
    if danger_package == '0':
        print('\n通过安检，可以乘车')
    else:
        print('\n没有通过安检，不能乘车')
else:
    print('\n没有车票，不能进站')
