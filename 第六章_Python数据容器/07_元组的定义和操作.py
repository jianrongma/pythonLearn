# 定义元组
t1 = ("黑马程序员",1,True)
t2 = ()
t3 = tuple()
print(f"t1的类型是：{type(t1)}，内容是：{t1}")
print(f"t2的类型是：{type(t2)}，内容是：{t3}")
print(f"t3的类型是：{type(t2)}，内容是：{t3}")

# 定义单个元素的元组
# t4 = ("hello")
t4 = ("hello",)
print(f"t4的类型是：{type(t4)},内容是：{t4}")

# 元组的嵌套
t5 = ((1,2,3),(4,5,6))
print(f"t5的类型是：{type(t5)},内容是：{t5}")

# 下标索引去取出内容
num = t5[0][2]
print(f"从嵌套元组t5中取出的数据是:{num}")

# 元组的操作：index查找元素的下标索引
t6 = ("船只教育","黑马程序员","Python")
index = t6.index("船只教育")
print(f"在元组t6中查找船只教育的下标是：{index}")

# 元组的操作：count统计某元素的个数
t7 = ("船只教育","黑马程序员","Python","黑马程序员","黑马程序员","Python")
num = t7.count("黑马程序员")
print(f"在元组t7中统计黑马程序员的数量有:{num}")
# 元组的操作：len函数统计元组元素数量
t8 = ("船只教育","黑马程序员","Python","黑马程序员","黑马程序员","Python",True)
count = len(t8)
print(f"元组t8中一共有{count}个元素")
# 元组的遍历：while
index = 0
while index < len(t8):
    print(f"元组的元素有：{t8[index]}")
    # 至关重要
    index += 1

# 元组的遍历：for
for element in t7:
    print(f"元组2中的元素有：{element}")

# 修改元组内list的内容
# t8[0] = "itcast"
# print(t8)

t9 = (1,2,"Heimachengxuyuan",[1,2,3],[True,0,"IT"])
print(f"t9的内容是：{t9}")
t9[3][2] = "我改掉了"
t9[4][0] = "我也改掉了"
print(f"修改后t9的内容是：{t9}")