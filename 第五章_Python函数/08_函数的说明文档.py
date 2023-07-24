# 定义函数，进行文档说明

# 说明语法
def func(x,y):
    """
    函数体功能的说明
    :param x: 形参x的说明
    :param y: 形参y的说明
    :return: 返回值的说明
    """
    "函数体"
    return "返回值"

def add(x,y):
    """
    add函数可以接收2个参数，进行2数相加的功能
    :param x: 形参x表示相加的其中一个数字
    :param y: 形参y表示相加的另一个数字
    :return: 返回值是2数相加的结果
    """
    result = x + y
    print(f"2数相加的结果是:{result}")
    return result


add(1,5)