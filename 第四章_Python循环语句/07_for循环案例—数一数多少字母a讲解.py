"""
定义字符串变量name，内容为："itheima is a brand of itcast"
通过for循环，遍历此字符串，统计有多少个英文字母："a"

提示：
1. 计数可以在循环外定义一个整数类型变量用来做累加计数
2. 判断是否为字母"a"，可以通过if语句结合比较运算符来完成
"""

# 1.定义字符串变量
name = "itheima is a brand of itcast"
# 2. 定义一个整数类型变量来做累加计数
count = 0
for x in name:
    # 3.通过if语句结合比较运算符来判断是否为字母”a“
    if x == "a":
        count += 1

# 输出统计所得的共有几个字母
print(f"共有{count}个字母a")

