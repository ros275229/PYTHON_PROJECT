import math


def tran(angle):
    # 将角度转化为弧度
    return angle * math.pi / 180.0

D = 70.0
angle_o = 120.0
angle_a = 1.5
a = 1.0 * math.sin(tran(60.0)) / math.sin(tran(28.5))
b = 1.0 * math.sin(tran(60.0)) / math.sin(tran(31.5))

c = a + b
x_list = [0, -800, -600, -400, -200, 0, 200 , 400 , 600 , 800]


def hx(idx):
    return D - (x_list[idx] * math.tan(tran(angle_a)))


def wx(idx):
    return hx(idx) * c * math.cos(tran(angle_a))


def w1(idx):
    return hx(idx) * a


def w2(idx):
    return hx(idx) * b


def print_value(x):
    print("{:.8f}".format(x), end=" ")


if __name__ == "__main__":
    print(" 高度  : ")
    for i in range(1, 10):
        print_value(hx(i))
    print()

    print(" 覆盖宽度  : ")
    for i in range(1, 10):
        print_value(wx(i))
    print()

    print(" 覆盖率 :  ")
    for i in range(2, 10):
        ans = ((w2(i - 1) + w1(i)) * math.cos(tran(angle_a)) - 200.00) / wx(i)
        print_value(ans)

    print()


