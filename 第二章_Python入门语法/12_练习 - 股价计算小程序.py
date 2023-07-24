"""
定义如下变量
name， 公司名
stock_price， 当前股价
stock_code， 股票代码
stock_price_daily_growth_factor， 股票每日增长系数，浮点数类型，比如1.2
growth_day， 增长天数
计算，经过growth_day天的增长后，股价达到了多少钱
使用字符串格式进行输出，如果是浮点数，要求小数点精度2位数
示例输出：
公司:传智播客，股票代码:003032，当前股价:19.99  --- 本行要求使用 f"{变量}" 的方式输出
每日增长系数是:1.2，经过7天的增长后，股价达到了:71.63 --- 本行要求使用 %占位符 的方式输出
"""
name = "传智播客"
stock_price = 19.99
stock_code = "003032"
stock_price_daily_growth_factor = 1.2
growth_days = 7
finally_stock_price = stock_price * stock_price_daily_growth_factor ** growth_days
print(f"公司：{name},股票代码：{stock_code},当前股价：{stock_price}")
print("每日增长系数：%.1f,经过%d天的增长后，股价达到了：%.2f" % (stock_price_daily_growth_factor,growth_days,finally_stock_price))