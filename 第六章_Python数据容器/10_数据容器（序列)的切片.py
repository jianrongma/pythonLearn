# 对序列进行切片演示

# 对list进行切片 从1开始，到4结束，步长1
my_list = [0,1,2,3,4,5,6]
result1 = my_list[1:4]
print(f"对list进行切片后的结果是:{result1}")
# 对tuple进行切片，从头开始，到最后结束，步长1
my_tuple = (0,1,2,3,4,5,6)
result2 = my_tuple[:] # 起始和结束不写表示从头到尾，步长为1可以省略
print(f"对元组进行切片后的结果是:{result2}")
# 对str进行切片，从头开始，到最后结束，步长2
my_str = "01234567"
result3 = my_str[::2]
print(f"对str进行切片后的结果是:{result3}")
# 对str进行切片，从头开始，到最后结束，步长-1
my_str = "01234567"
result4 = my_str[3:1:-1] # 等同于将序列反转了
print(f"对str进行切片后的结果是:{result4}")
# 对列表进行，从3开始，到1结束，步长-1
my_list = [0,1,2,3,4,5,6]
result5 = my_list[3:1:-1]
print(f"对列表进行切片操作后的结果是:{result5}")
# 对元组进行切片，从头开始，到尾结束，步长-2
my_tuple = (0,1,2,3,4,5,6)
result6 = my_tuple[::-2]
print(f"结果是:{result6}")