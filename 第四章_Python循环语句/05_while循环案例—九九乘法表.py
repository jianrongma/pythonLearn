# print输出不换行
# print("hello")
# print("world")
#
# print("hello",end='')
# print("world",end='')

# 制表符 \t，实现字符串的对齐
# print("hello world")
# print("itheima best")
#
# print("hello\tworld")
# print("itheima\tbest")

"""
使用while循环打印九九乘法表
外层循环-控制行数，循环条件为 i<=9
内层循环-控制每行的内容，每行的个数与行数对应，循环条件为 j<=i
"""

# 定义外层循环的控制变量
i = 1
while i <= 9:

    # 定义内层循环的控制变量
    j = 1
    while j <= i:
        # 内层循环的print语句，不要换行，通过\t制表符进行对齐
        print(f"{j} * {i} = {j * i}\t",end='')
        j += 1

    i += 1
    print() # print空内容就是输出一个换行

