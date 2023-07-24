# 无return语句的函数返回值
# def say_Hi():
#     print("你好")

# 定义变量接收say_Hi函数的返回值
# result = say_Hi()
# 打印返回值
# print(f"无返回值函数，返回的内容是：{result}")
# 打印返回值的类型
# print(f"无返回值函数，返回的内容类型是：{type(result)}")

# 主动返回None的函数
# def say_Hi2():
#     print("你好")
#     return None
#
# result = say_Hi2()
# print(f"无返回值函数，返回的内容是{result}")
# print(f"无返回值函数，返回的内容类型是：{type(result)}")

# None用于if的判断
def check_age(age):
    if age > 18:
        return "SUCCESS"
    else:
        return  None

result = check_age(13)
# print(result)
if not None:
    # 进入if表示result是None值，也就是False
    print("未成年人，不可以进入")


# 暂不赋予变量具体值
name = None
