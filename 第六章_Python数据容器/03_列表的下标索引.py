# 通过下标索引取出对应位置的元素
my_list = ['Ton','hixabxa',1]
# 列表[下标索引]，从前往后从0开始，从后往前从-1递减
print(my_list[0])
print(my_list[1])
print(my_list[2])
# 下标索引取值超过范围，就会报错
# print(my_list[3])

# 通过下标索引取出数据（倒序取出）
print(my_list[-1])
print(my_list[-2])
print(my_list[-3])

# 取出嵌套列表的元素
my_list1 = [[1,5,2],[0,9,8],1,'jsua']
print(my_list1[1][0])