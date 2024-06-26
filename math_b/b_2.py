import math

N = 9
xh = [0.0, 0.0, 0.3, 0.6, 0.9, 1.2, 1.5, 1.8, 2.1]
angle = [0.0, 0.0, 45.0, 90.0, 135.0, 180.0, 225.0, 270.0, 315.0]
ans = [[0.0] * N for _ in range(N)]


def tran(angle):  # 将角度转化为弧度
    return math.radians(angle)


def print_value(x):
    print(f"{x:.8f}", end=" ")


h0 = 120
af = 1.5
st = 60.00

for i in range(1, N):
    for j in range(1, N):
        x = xh[j]
        bt = angle[i]

        taf = tran(af)
        tst = tran(st)
        tbt = tran(bt)

        z = -x * 1852 * math.tan(taf) * math.cos(tbt)
        y = h0 - z

        l1 = y * math.tan(tst) / math.cos(taf) - math.sin(taf) * math.tan(tst)
        l2 = y * math.tan(tst) / math.cos(taf) + math.sin(taf) * math.tan(tst)

        ans[i][j] = l1 + l2

for i in range(1, N):
    for j in range(1, N):
        print_value(ans[i][j])
    print()
