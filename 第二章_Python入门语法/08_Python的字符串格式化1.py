# 1. 字符串格式化 -
name = "黑马程序员"
message = "学IT就来：%s" % name
print(message)

# 2. 数字类型的占位
class_num = 57
avg_salary = 16781
message = "Python大数据学科，北京%s期,毕业平均工资:%s" % (class_num,avg_salary)
# 这里是将数字 转换成了 字符串；也就是数字 57，变成了字符串"57"被放入占位的地方
print(message)

# 3. 完成字符串、整数、浮点数，三种不同类型变量的占位
name = "传智播客"
set_up_year = 2006
stock_price = 19.19
message = "我是：%s,我成立于：%d年,我今天的股价是：%f" %(name,set_up_year,stock_price)
print(message)