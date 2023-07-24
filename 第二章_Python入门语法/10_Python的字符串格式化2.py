""""
字符串格式化 - 快速写法
通过语法：f"内容{变量}" 的格式来快速格式化
"""
name = "传智播客"
set_up_year = 2006
stock_price = 19.19
print(f"我是{name},我成立于{set_up_year},我今天的股价是{stock_price}")
# 这种写法不做精度控制，也不理会类型，适用于快速格式化字符串