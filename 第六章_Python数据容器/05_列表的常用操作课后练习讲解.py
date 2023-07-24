"""
练习案例:常用功能练习
有一个列表，内容是：[21, 25, 21, 23, 22, 20]，记录的是一批学生的年龄

请通过列表的功能（方法），对其进行
定义这个列表，并用变量接收它
追加一个数字31，到列表的尾部
追加一个新列表[29, 33, 30]，到列表的尾部
取出第一个元素（应是：21）
取出最后一个元素（应是：30）
查找元素31，在列表中的下标位置
"""
# 定义一个变量来接收 记录学生年龄的列表
age_list = [21, 25, 21, 23, 22, 20]
# 追加一个数字31，到列表的尾部
age_list.append(31)
print(age_list)
# 追加一个新列表[29, 33, 30]，到列表的尾部
age_list.extend([29, 33, 30])
print(age_list)
# 取出第一个元素（应是：21）
print(age_list[0])
# 取出最后一个元素（应是：30）
print(age_list[-1])
# 查找元素31，在列表中的下标位置
index = age_list.index(31)
print(f"元素31，在列表中的下标位置是：{index}")
