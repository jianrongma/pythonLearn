""""
通过for循环，输出九九乘法表内容
提示：
2层循环，外层控制行，内层控制列
可使用range语句来得到数字序列进行for循环
内层for循环的range最大范围，取决于当前外层循环的数字
"""
for i in range(1,10):
    for j in range(1,i+1):
        print(f"{j} * {i} = {j * i}\t",end='')

    print()