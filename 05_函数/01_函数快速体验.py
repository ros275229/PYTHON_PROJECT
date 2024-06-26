"""
演示：快速体验函数的开发及应用
"""
# 需求，统计字符串的长度，不使用内置函数len()

str1 = "y1441206"
# count = 0
# for i in str1:
#     count += 1
# print(count)

def my_len(data):
    count = 0
    for i in data:
        count += 1
    return count

print(my_len(str1))


