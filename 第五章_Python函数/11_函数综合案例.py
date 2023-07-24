"""
综合案例：黑马ATM
1.定义一个全局变量：money，用来记录银行卡余额（默认5000000）
2.定义一个全局变量：name，用来记录客户姓名（启动程序时输入）
3.定义如下的函数：
 * 查询余额函数
 * 存款函数
 * 取款函数
 * 主菜单函数

要求：
程序启动后要求输入客户姓名
查询余额、存款、取款后都会返回主菜单
存款、取款后，都应显示一下当前余额
客户选择退出或输入错误，程序会退出，否则一直运行
"""

# 定义全局变量money、name
money = 5000000
name = None

# 要求客户输入姓名
name = input("请输入您的姓名：")

# 定义查询余额函数
def query(Ture):
    print("---------查询余额---------")
    print(f"{name},您好，您的余额剩余：{money}元")

# 定义存款函数
def saving(num):
    print("---------存款---------")
    global money
    money += num
    print(f"{name},您好，您存款{num}元成功")
    print(f"{name},您好，您的余额剩余{money}元")

    # 调用一下查询余额函数,使用布尔类型控制标头的输出
    query(False)

# 定义取款函数
def get_money(num):
    print("---------取款---------")
    global money
    money -= num
    print(f"{name},您好，您取款{num}成功")
    # 调用查询余额函数
    query(False)

# 定义主菜单函数
def main():
    print("---------主菜单---------")
    print(f"{name}，您好，欢迎来到黑马银行ATM。请选择操作：")
    print("查询余额\t[输入1]") # 使用制表符\t使输出对齐
    print("存款\t\t[输入2]")
    print("取款\t\t[输入3]")
    print("退出\t\t[输入4]")
    return input("请输入您的选择：")

# 设置无限循环，确保程序不退出
while True:
    # 声明变量接收用户的输入
    keyboard_input = main()
    # 判断输入
    if keyboard_input == "1":
        query(True)
        continue #查询余额、存款、取款后都会返回主菜单
    elif keyboard_input == "2":
        num = int(input("您想要存入多少钱？请输入："))
        saving(num)
        continue
    elif keyboard_input == "3":
        num = int(input("您想要取走多少钱？请输入："))
        get_money(num)
        continue
    else:
        print("已退出")
        break # 结束循环






