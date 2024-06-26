"""
演示第一种字符串格式化的方式：%d,f,s"
"""
# 占位符拼接 %d %s %f
print("1 * 1 的结果是：%d" % (1 * 1))
name = "传智播客"
set_up_year = 2006
stock_price = 19.990000
# f: format
print("我是 ：%s，我成立于：%d 年，我今天的股价是：%.6f" % (name, set_up_year, stock_price))


"""
演示第二种字符串格式化的方式：f"{占位}"
"""
name = "传智播客"
set_up_year = 2006
stock_price = 19.990000
# f: format
print(f"我是{name}，我成立于：{set_up_year}年，我今天的股价是：{stock_price}")