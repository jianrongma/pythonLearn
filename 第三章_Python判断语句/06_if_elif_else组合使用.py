# 演示 if elif else 多条件判断语句的使用

# print("欢迎来到黑马动物园。")
# height = int(input("请输入您的身高（cm）："))
# vip_level = int(input("请输入你的VIP等级（1-5）："))
# day = int(input("请输入今天的日期（1~30）："))
# # 通过if判断，使用多条件判断的语法：
# if height < 120:
#     print("您的身高未超出120cm，可以免费游玩。")
# elif vip_level >3:
#     print("vip级别大于3，可以免费游玩。")
# elif day == 1:
#     print("今天是1号，可以免费游玩。")
# else:
#     print("不好意思，条件都不满足，需要买票10元")
#
# print("祝您游玩愉快。")

# 可以在条件判断中，直接写input语句，节省代码量，使代码看起来更简洁
print("欢迎来到黑马动物园。")
# height = int(input("请输入您的身高（cm）："))
# vip_level = int(input("请输入你的VIP等级（1-5）："))
# day = int(input("请输入今天的日期（1~30）："))
# 通过if判断，使用多条件判断的语法：
if int(input("请输入您的身高（cm）：")) < 120:
    print("您的身高未超出120cm，可以免费游玩。")
elif int(input("请输入你的VIP等级（1-5）：")) >3:
    print("vip级别大于3，可以免费游玩。")
elif int(input("请输入今天的日期（1~30）：")) == 1:
    print("今天是1号，可以免费游玩。")
else:
    print("不好意思，条件都不满足，需要买票10元")

print("祝您游玩愉快。")

