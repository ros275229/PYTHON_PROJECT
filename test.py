import statistics as st
seq = [13, 15, 16, 16, 19, 20, 20, 21, 22, 22, 25, 25, 25, 25, 30, 33, 33, 35, 35, 35, 35, 36, 40, 45, 46, 52, 70]
x = sum(seq)
y = len(seq)
z = x / y
a = st.median(seq)  # 中位数
b = st.mode(seq)  # 众数
print(b)
print(x, y, z)
print(a)