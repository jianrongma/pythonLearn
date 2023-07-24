# 增
# 1.在指定下标位置插入新元素 列表.insert(下标，元素)
# my_list = ['axycfuvc', 1, 'sucgad']
# my_list.insert(1, 90)
# print(f"列表在插入元素后，结果是：{my_list}")

# 2.追加元素
# 2.1列表.append(元素)
# my_list.append('itheima')
# print(f"列表追加了元素后，结果是：{my_list}")
# 2.2列表.extend(数据容器)
# my_list.extend([1,3,5])
# print(f"列表追加了一批新元素后，结果是：{my_list}")

# 删
# 1.删除列表指定下标元素
# 1.1 del 列表[下标]
my_list = ['axycfuvc', 8, 'sucgad']
del my_list[2]
print(f"通过del取出元素后列表内容为：{my_list}")
# 1.2 列表.pop(下标)
my_list = ['axycfuvc', 8, 'sucgad']
my_list.pop(1)
print(f"通过pop方法取出元素后列表内容为：{my_list}")

# 2.删除某元素在列表中的第一个匹配项
# 列表.remove(元素)
my_list = ['axycfuvc', 8, 'sucgad']
my_list.remove("axycfuvc")
print(f"通过remove方法移除元素后列表内容为：{my_list}")

# 3.清空列表
# 列表.clear()
my_list = ['axycfuvc', 8, 'sucgad']
my_list.clear()
print(f"通过clear方法清空列表后，结果为：{my_list}")

# 改
# 修改指定位置（索引）的元素值
# 列表[下标] = 值
my_list = ['axycfuvc', 8, 'sucgad']
my_list[1] = 23
print(f"修改列表下标为1的元素后列表内容为:{my_list}")

# 查
# 1.查找某元素的下标
# 列表.index(元素)
my_list = ['axycfuvc', 8, 'sucgad',1,'xax']
index = my_list.index("axycfuvc")
print(f"axycfuvc在列表中下标的索引值是：{index}")

# 2.统计指定元素的个数
# 列表.count(元素)
my_list = ['axycfuvc', 8, 'sucgad',1,'xax','xax',8]
count = my_list.count('xax')
print(f"列表中xax的数量是：{count}个")

# 3.统计列表中一共有多少元素
# len(列表)
my_list = ['axycfuvc', 8, 'sucgad',1,'xax','xax',8,True]
count = len(my_list)
print(f"列表中一共有{count}个元素")
