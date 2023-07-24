"""
1. 定义一个变量，数字类型，内容随意。
2. 基于input语句输入猜想的数字，通过if和多次elif的组合，判断猜想数字是否和心里数字一致。
输出如下：
"
请输入第一次猜想的数字:1
不对，再猜一次:2
不对，再猜最后一次:3
Sorry，全部猜错啦，我想的是:10
"
"""

# 误解：
# num = 10
# if int(input("请输入第一次猜想的数字：")) != num :
#     print(f"{int(input('不对，再猜一次：'))}")
# elif int(input("不对，再猜一次：")) != num:
#     print(f"{int(input('不对，再猜最后一次：'))}")
# else:
#     print(f"Sorry，全部猜错啦，我想的是:{num}")

# 正解
# 定义一个数字变量
num = 5
# 通过键盘输入获取猜想的数字，通过if和 elif 的组合进行多次猜想比较
if int(input("请猜一个数字：")) == num:
    print("恭喜第一次就猜对了呢")
elif int(input("猜错了，再猜一次：")) == num:
    print("猜对了")
elif int(input("猜错了，再猜最后一次：")) == num:
    print("恭喜，最后一次机会，你猜对了")
else:
    print("Sorry,猜错了！")