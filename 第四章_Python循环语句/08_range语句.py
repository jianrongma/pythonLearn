# range语法1 range(num)
# for x in range(5):
#     print(x)

# range语法2 range(num1,num2)
# for x in range(1,8):
#     print(x)

# range语法3 range(num1,num2,step)
# for x in range(1,5,2):
#     print(x)

"""
练习案例：有几个偶数
定义一个数字变量num，内容随意
并使用range()语句，获取从1到num的序列，使用for循环遍历它。
在遍历的过程中，统计有多少偶数出现

提示：
1. 序列可以使用：range(1, num)得到
2. 偶数通过if来判断，判断数字余2是否为0即可
"""
# 1.定义一个数字变量
num = 100
# 2. 定义一个变量接收统计的偶数的个数
count = 0
# 3.for循环遍历，使用range语句，获取从 1 到 num 的序列
for x in range(1,100):
    # 4.通过if判断是否为偶数
    if x % 2 == 0:
        count += 1
    # 5.输出统计的偶数的个数
print(f"从1到{num}中，一共有{count}个偶数")

for x in range(1,11):
    print(f"送给她的第{x}朵玫瑰花")
