# def list_while_func():
    # my_list = ["智能工厂","黑马程序员","订单优先级"]
    # 循环控制变量通过下标索引来控制，默认为0
    # 每一次循环将下标索引变量+1
    # 循环条件：下标索引量 < 列表的元素数量

    # 定义一个变量标记列表的下标
    # index = 0
    # while index < len(my_list):
    #     # 通过index变量取出对应下标的元素
    #     element = my_list[index]
    #     print(f"列表的元素：{element}")

        # 至关重要 将循环变量（index）每次循环都+1
        # index += 1


# def list_for_func():
    # my_list = [1,2,3,4,5]
    # for element in my_list:
    #     print(f"列表的元素有：{element}")


# list_while_func()
# list_for_func()

"""
练习案例：取出列表内的偶数
定义一个列表，内容是：[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
遍历列表，取出列表内的偶数，并存入一个新的列表对象中
使用while循环和for循环各操作一次

提示：
通过if判断来确认偶数
通过列表的append方法，来增加元素
"""
# while循环
def list_while_func():
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    my_list1 = []
    index = 0
    while index < len(my_list):
        element = my_list[index]
        if element % 2 == 0:
            my_list1.append(element)
        index += 1

    print(f"通过while循环，从列表{my_list}中取出偶数，组成新的列表：{my_list1}")

# list_while_func()

# for循环
def list_for_func():
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    my_list1 = []
    for element in my_list:
        if element % 2 == 0:
            my_list1.append(element)

    print(f"通过for循环，从列表{my_list}中取出偶数，组成新的列表：{my_list1}")

list_for_func()