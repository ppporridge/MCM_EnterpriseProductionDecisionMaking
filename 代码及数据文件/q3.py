import openpyxl

# a：零配件 b：半成品 c：成品
a11 = 0.1
a12 = 2
a13 = 1
a21 = 0.1
a22 = 8
a23 = 1
a31 = 0.1
a32 = 12
a33 = 2
a41 = 0.1
a42 = 2
a43 = 1
a51 = 0.1
a52 = 8
a53 = 1
a61 = 0.1
a62 = 12
a63 = 2
a71 = 0.1
a72 = 8
a73 = 1
a81 = 0.1
a82 = 12
a83 = 2
b11 = 0.1
b12 = 8
b13 = 4
b14 = 6
b21 = 0.1
b22 = 8
b23 = 4
b24 = 6
b31 = 0.1
b32 = 8
b33 = 4
b34 = 6
c1 = 0.1
c2 = 8
c3 = 6
c4 = 10
d1 = 200
d2 = 40

x = [0,0,0,0,0,0,0,0,  0,0,0, 0,0,0, 0,0]   # 分别是零件1~8是否检测、半成品1~3是否检测、半成品1~3是否拆解、成品是否检测、成品是否拆解

### 半成品1
# 零件1是否检测
def step11():
    return -a13*x[0]-a23*x[1]-a33*x[2]+((1-a11) if x[0]==1 else 1)*((1-a21) if x[1]==1 else 1)*((1-a31) if x[2]==1 else 1)*step12()

# 半成品是否检测
def step12():
    if x[8]==1: # 如果检测，有装配成本、检测费用，还需要进入是否拆解的判断
        p=((1-a11) if x[0]==0 else 1)*((1-a21) if x[1]==0 else 1)*((1-a31) if x[2]==0 else 1)*(1-b11)
        return -b12-b13+(1-p)*step13()
    else: # 不检测，只有装配成本
        return -b12

# 半成品是否拆解
def step13():
    if x[11]==1:
        return -b14+assumeW1
    else:
        return 0

### 半成品2
# 零件1是否检测
def step21():
    return -a43*x[3]-a53*x[4]-a63*x[5]+((1-a41) if x[3]==1 else 1)*((1-a51) if x[4]==1 else 1)*((1-a61) if x[5]==1 else 1)*step22()

# 半成品是否检测
def step22():
    if x[9]==1: # 如果检测，有装配成本、检测费用，还需要进入是否拆解的判断
        p=((1-a41) if x[3]==0 else 1)*((1-a51) if x[4]==0 else 1)*((1-a61) if x[5]==0 else 1)*(1-b21)
        return -b22-b23+(1-p)*step23()
    else: # 不检测，只有装配成本
        return -b22

# 半成品是否拆解
def step23():
    if x[12]==1:
        return -b24+assumeW2
    else:
        return 0

### 半成品3
def step31():
    return -a73*x[6]-a83*x[7]+((1-a71) if x[6]==1 else 1)*((1-a81) if x[7]==1 else 1)*step32()

# 半成品是否检测
def step32():
    if x[10]==1: # 如果检测，有装配成本、检测费用，还需要进入是否拆解的判断
        p=((1-a71) if x[6]==0 else 1)*((1-a81) if x[7]==0 else 1)*(1-b31)
        #print("p",p)
        return -b32-b33+(1-p)*step33()
    else: # 不检测，只有装配成本
        return -b32

# 半成品是否拆解
def step33():
    if x[13]==1:
        return -b34+assumeW3
    else:
        return 0

#### 成品
# 半成品是否检测
def step1():
    return ((1-half[0][1]) if x[8]==1 else 1)*((1-half[1][1]) if x[9]==1 else 1)*((1-half[2][1]) if x[10]==1 else 1)*step2()

# 成品是否检测
def step2():
    if x[14]==1: # 如果检测，有装配成本、检测费用，还需要进入是否拆解的判断
        p=((1-half[0][1]) if x[8]==0 else 1)*((1-half[1][1]) if x[9]==0 else 1)*((1-half[2][1]) if x[10]==0 else 1)*(1-c1)
        return -c2-c3+p*d1+(1-p)*step3()
    else: # 不检测，只有装配成本
        return -c2 + step4()

# 成品是否拆解
def step3():
    if x[15]==1:
        return -c4+assumeW
    else:
        return 0

# 市场销售阶段
def step4():
    p=((1-half[0][1]) if x[8]==0 else 1)*((1-half[1][1]) if x[9]==0 else 1)*((1-half[2][1]) if x[10]==0 else 1)*(1-c1)
    return p * d1 + (1 - p) * (-d2 + step3())

bestw = -52364
bestx = []
i = 0
for x1 in range(2):
    x[0] = x1
    for x2 in range(2):
        x[1] = x2
        for x3 in range(2):
            x[2] = x3
            for x4 in range(2):
                x[3] = x4
                for x5 in range(2):
                    x[4] = x5
                    for x6 in range(2):
                        x[5] = x6
                        for x7 in range(2):
                            x[6] = x7
                            for x8 in range(2):
                                x[7] = x8
                                for x9 in range(2):
                                    x[8] = x9
                                    for x10 in range(2):
                                        x[9] = x10
                                        for x11 in range(2):
                                            x[10] = x11
                                            for x12 in range(x9+1):
                                                x[11] = x12
                                                for x13 in range(x10+1):
                                                    x[12] = x13
                                                    for x14 in range(x11 + 1):
                                                        x[13] = x14
                                                        for x15 in range(2):
                                                            x[14] = x15
                                                            for x16 in range(x15+1):
                                                                x[15] = x16

                                                                half = []  # 存放成本1~3的成本、次品率

                                                                # 半成品1
                                                                real_res = 40
                                                                assumeW1 = -1100
                                                                while abs(real_res - assumeW1) >= 10e-6:
                                                                    real_res = step11()
                                                                    assumeW1 = (real_res + assumeW1) / 2
                                                                real_res -= (a12 + a22 + a32)

                                                                p = (1 - a11) * (1 - a21) * (1 - a31) * (1 - b11)
                                                                if x[8] == 1:
                                                                    p1 = p
                                                                else:
                                                                    p1 = ((1 - a11) if x[0] == 1 else 1) * (
                                                                    (1 - a21) if x[1] == 1 else 1) * (
                                                                         (1 - a31) if x[2] == 1 else 1)
                                                                half.append([-real_res,1-p/p1])

                                                                real_res = 40
                                                                assumeW2 = 20
                                                                while abs(real_res - assumeW2) >= 10e-6:
                                                                    real_res = step21()
                                                                    assumeW2 = (real_res + assumeW2) / 2
                                                                real_res -= (a42 + a52 + a62)

                                                                p = (1 - a41) * (1 - a51) * (1 - a61) * (1 - b21)
                                                                if x[9] == 1:
                                                                    p1 = p
                                                                else:
                                                                    p1 = ((1 - a41) if x[3] == 1 else 1) * (
                                                                    (1 - a51) if x[4] == 1 else 1) * (
                                                                         (1 - a61) if x[5] == 1 else 1)
                                                                half.append([-real_res, 1-p / p1])

                                                                real_res = 40
                                                                assumeW3 = 20
                                                                while abs(real_res - assumeW3) >= 10e-6:
                                                                    real_res = step31()
                                                                    assumeW3 = (real_res + assumeW3) / 2
                                                                real_res -= (a72 + a82)

                                                                p = (1 - a71) * (1 - a81) * (1 - b31)
                                                                if x[10] == 1:
                                                                    p1 = p
                                                                else:
                                                                    p1 = ((1 - a71) if x[6] == 1 else 1) * (
                                                                    (1 - a81) if x[7] == 1 else 1)
                                                                half.append([-real_res, 1-p / p1])

                                                                real_res = 40
                                                                assumeW = 20
                                                                while abs(real_res - assumeW) >= 10e-6:
                                                                    real_res = step1()
                                                                    assumeW = (real_res + assumeW) / 2

                                                                if bestw<(real_res-half[0][0]-half[1][0]-half[2][0]):
                                                                    bestw = real_res - half[0][0] - half[1][0] - \
                                                                    half[2][0]
                                                                    bestx = [element for element in x]
print(bestx,bestw)




