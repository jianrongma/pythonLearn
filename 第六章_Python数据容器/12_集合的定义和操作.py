# 定义集合
my_set = {"传智教育","黑马程序员","uwigdeucv","传智教育","黑马程序员","uwigdeucv"}
my_set_empty = set() # 定义空集合
print(f"my_set的内容是:{my_set},类型是{type(my_set)}")
print(f"my_set_empty的内容是:{my_set_empty},类型是{type(my_set_empty)}")
# 添加新元素 集合.add(元素)
my_set.add("Python")
my_set.add("传智教育")
print(f"my_set添加元素后的结果是:{my_set}")
# 移除元素  集合.remove(元素)
my_set.remove("传智教育")
print(f"my_set移除元素'传智教育'后的结果是:{my_set}")
# 随机取出一个元素 集合.pop()
my_set = {"传智教育","黑马程序员","uwigdeucv"}
element = my_set.pop()
print(f"随机从集合my_set中取出一个元素,取出的元素是:{element},取出后集合是:{my_set}")
# 清空集合 集合.clear()
my_set = {"传智教育","黑马程序员","uwigdeucv"}
my_set.clear()
print(f"集合被清空后的结果是：{my_set}")
# 取2个集合的差集 集合1.difference(集合2) 取出集合1有而集合2没有的
set_1 = {1,2,3}
set_2 = {1,5,6}
set_3 = set_1.difference(set_2)
print(f"取出差集后的结果是:{set_3}")
print(f"取差集后，原有set1的内容是:{set_1}")
print(f"取差集后，原有set2的内容是:{set_2}")
# 消除2个集合的差集 集合1.difference_update(集合2) 对比集合1和集合2，删除和集合2相同的元素
set_1 = {1,2,3}
set_2 = {1,5,6}
# set_4 = set_1.difference_update(set_2)
# print(f"消除2个集合的差集后的结果是:{set_4}")
print(f"消除2个集合的差集后，原有set1的内容是:{set_1}")
print(f"消除2个集合的差集后，原有set2的内容是:{set_2}")
# 2个集合 合并为1个 集合1.union(集合2) 将集合1和集合2组合为新的集合 得到新的集合 集合1和集合2不变
set_1 = {1,2,3}
set_2 = {1,5,6}
set_5 = set_1.union(set_2)
print(f"合并2个集合后的结果是:{set_5}")
print(f"合并2个集合后，原有set1的内容是:{set_1}")
print(f"合并2个集合后，原有set2的内容是:{set_2}")
# 统计集合元素的数量 len(集合)
set = {"hiehsax","黑马程序员",1,3,1,2,3,"黑马程序员",True}
num = len(set)
print(f"集合set内的元素数量有:{num}")

set1 = {3,8,True,True,False} # True和False 代表 0 1
num1 = len(set1)
print(f"集合set1内的元素数量有:{num1}")

# 集合的遍历
# 集合不支持下标索引，不能用while循环
# 可以使用for循环
set1 = {1,2,3,4,5}
for element in set1:
    print(f"集合set的元素有:{element}")