# 坚持表白100天，每天都送10朵玫瑰花
""""
外层循环 - 100天 - range(1,101)
内层循环 - 每天都送10朵玫瑰花 - range(1,11)
"""
# i = 1
# for i in range(1,101):
#     print(f"今天是向你表白的第{i}天")
#     # 内层循环
#     for j in range(1,11):
#         print(f"这是送给你的第{j}朵玫瑰")
#
#     print("我喜欢你")
#
# print(f"表白到第{i}天，表白成功啦~")

"""
for循环和while循环的相互嵌套
"""
i = 1
while i <= 100:
    print(f"今天是向你表白的第{i}天")
    for j in range(1,11):
        print(f"这是送给你的第{j}朵玫瑰")

    print(f"我喜欢你,第{i}天的表白结束")
    i += 1

print(f"表白到第{i-1}天，表白成功啦~")


