#快递计费
while 1:
    init_weight = float(input('请输入您的快递重量（单位/kg）：'))
    place = input('请选择您所在的地区编号（华东01，华南02，华北03）：')
    if place == '01': #执行华东地区计费方案
        if init_weight == 0:
            print('需支付0.0元')
        elif 0 < init_weight <= 2:
            print('\n您的包裹重:', init_weight,'kg')
            print('需支付13元\n')
        elif 2 < init_weight < 99999:
            print('\n包裹超重！')
            total_price = 13 + (init_weight -2) * 3;
            print('您的包裹重:', init_weight, 'kg')
            print('需支付:', total_price, '元\n')
        else :
            print('\n非法数据,请在0～99999内重新输入重量\n')
    elif place == '02': #执行华南地区计费方案
        if init_weight == 0:
            print('需支付0.0元')
        elif 0 < init_weight <= 2:
            print('\n您的包裹重:', init_weight, 'kg')
            print('需支付12元\n')
        elif 2 < init_weight < 99999:
            print('\n包裹超重！')
            total_price = 12 + (init_weight -2) * 2;
            print('您的包裹重:', init_weight, 'kg')
            print('需支付:', total_price, '元\n')
        else :
            print('\n非法数据,请在0～99999内重新输入重量\n')
    elif place == '03':   #执行华北地区计费方案
        if init_weight == 0:
            print('需支付0.0元')
        elif 0 < init_weight <= 2:
            print('\n您的包裹重:',init_weight, 'kg')
            print('需支付14元\n')
        elif 2 < init_weight < 99999:
            print('\n包裹超重！')
            total_price = 14 + (init_weight -2) * 4;
            print('您的包裹重:', init_weight, 'kg')
            print('需支付:', total_price, '元\n')
        else :
            print('\n非法数据,请在0～99999内重新输入重量\n')
    else:
        print('\n其他地区暂未开放\n')
