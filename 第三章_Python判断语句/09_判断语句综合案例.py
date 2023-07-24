"""
案例需求:
         定义一个数字（1~10，随机产生），通过3次判断来猜出来数字

案例要求：
1.   数字随机产生，范围1-10
2.   有3次机会猜测数字，通过3层嵌套判断实现
3.   每次猜不中，会提示大了或小了

提示，通过如下代码，可以定义一个变量num，变量内存储随机数字。
import random
num = random.randint(1,10)
"""

# 1.构建一个随机的数字变量
import random
num = random.randint(1,10)

guess_num = int(input("输入你要猜测的数字："))

# 2. 通过if判断语句进行数字的猜测验证
if guess_num == num:
    print("恭喜你，猜中了")
else:
    if guess_num > num:
        print("你猜测的数字大了")
    else:
        print("你猜测的数字小了")

    guess_num = int(input("再次输入你要猜测的数字："))
    if guess_num == num:
        print("恭喜你，第二次就猜中了")
    else:
        if guess_num > num:
            print("你猜测的数字大了")
        else:
            print("你猜测的数字小了")

    guess_num = int(input("最后一次输入你要猜测的数字："))
    if guess_num == num:
        print("恭喜你，最后一次终于猜中了")
    else:
        print("很遗憾，三次都没有猜中")




