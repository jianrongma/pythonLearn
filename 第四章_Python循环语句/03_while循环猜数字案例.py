"""
设置一个范围1-100的随机整数变量，通过while循环，配合input语句，判断输入的数字是否等于随机数

无限次机会，直到猜中为止
每一次猜不中，会提示大了或小了
猜完数字后，提示猜了几次

提示：
无限次机会，终止条件不适合用数字累加来判断
可以考虑布尔类型本身（True or False）
需要提示几次猜中，就需要提供数字累加功能
随机数可以使用：
import random
num = random.randint(1,100)
"""
# 1.获取1~100的随机数
import random
num = random.randint(1,100)

# 2.定义一个变量，记录总共猜测了多少次
count = 0

# 3.由于有无限次猜测机会，所以通过一个布尔类型的变量，做循环是否继续的标记
flag = True
while flag:
    guess_num = int(input("输入你猜测的数字："))
    count += 1
    if guess_num == num:
        print("猜中了")
        flag = False
    else:
        if guess_num > num:
            print("猜大了")
        else:
            print("猜小了")

print(f"你总共猜测了{count}次")
