import openpyxl

# 情况1
a1 = 0.1
a2 = 4
a3 = 2
b1 = 0.1
b2 = 18
b3 = 3
c1 = 0.1
c2 = 6
c3 = 3
c4 = 56
d1 = 6
d2 = 5

# 零件1、2是否检测
def step1():
    global x1
    global x2
    if(x1==1 and x2==1):
        return -a3-b3+(1-a1)*(1-b1)*step3()  # 检测成本，同时有(1-a1)的概率能够进入后续
    elif(x1==1 and x2==0):
        return -a3 + (1 - a1) * step3()
    elif(x1==0 and x2==1):
        return -b3+(1-b1)*step3()
    else:
        return step3()  # 直接进入下一步

# 成品的装配和是否检测
def step3():
    global x1
    global x2
    global x3
    if(x3==1):
        p = ((1-a1) if x1==0 else 1)*((1-b1) if x2==0 else 1)*(1-c1) # 正品率
        return -c2-c3+p*c4+(1-p)*step4()
    else:
        return step5()

# 是否拆解不合格品
def step4():
    global assumeW
    if(x4==1):
        return -d2+assumeW  # 拆解出两个零件，相当于又是一件成品的利润
    else:
        return 0

# 进入市场（当未检测成品时才能到达这一步）
def step5():
    global x1
    global x2
    p = ((1 - a1) if x1==0 else 1) * ((1 - b1) if x2==0 else 1) * (1 - c1)
    return p*c4+(1-p)*(-d1+step4())  # 同时损失了一件

# 对不同情形枚举各种决策
for x1 in range(2):
    for x2 in range(2):
        for x3 in range(2):
            for x4 in range(x3+1):  # 如果不检测，也拆解不了
                real_res = 40
                assumeW = 20
                while abs(real_res-assumeW)>=10e-6:
                    real_res = step1()
                    assumeW = (real_res+assumeW)/2
                print(bool(x1),bool(x2),bool(x3),bool(x4),real_res - a2 - b2)  # 真正的利润要减去两个零件的成本

