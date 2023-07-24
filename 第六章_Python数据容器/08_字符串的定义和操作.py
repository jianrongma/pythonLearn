my_str = "itheima and itcast"
# 通过下标索引取值
value = my_str[4]
value1 = my_str[-14]
print(f"从字符串{my_str}取下标为4的元素，值是：{value},从字符串{my_str}取下标为-14的元素，值是：{value1}")
print(value1)

# 不能修改字符串的内容
# my_str[9] = "我该改了"
# print(my_str)
# index方法
value = my_str.index("and")
print(f"在字符串{my_str}中查找and，其起始下标为：{value}")
# replace方法
new_my_str = my_str.replace("and","我替换了一下")
print(f"将字符串{my_str}，进行替换后得到了新的字符串是:{new_my_str}")
# split方法
my_str = "hello python itheima and itcast"
my_str_list = my_str.split(" ")
print(f"将字符串{my_str}通过分隔符 ''切割后得到了：{my_str_list},其类型是:{type(my_str_list)}")
# strip方法
my_str = "  hello python  "
new_my_str = my_str.strip() # 不传入参数，去掉首位空格
print(f"将字符串{my_str}被strip后，结果是:{new_my_str}")

my_str = "12hello 12python21"
new_my_str = my_str.strip("12") # 只能去除掉首尾指定字符
print(f"将字符串{my_str}被strip('12')后，结果是:{new_my_str}")
# 统计字符串中某字符串的出现次数
my_str = "hello python itheima and itcast"
count = my_str.count("it")
print(f"字符串{my_str}中，字符it出现的次数是：{count}")
# 统计字符串的长度
my_str = "hello python itheima and itcast"
num = len(my_str)
print(f"字符串{my_str}的长度是:{num}")

# 字符串的while遍历
# my_str = "hello python itheima and itcast"
# index = 0
# while index < len(my_str):
#     print(f"字符串{my_str}的元素有：{my_str[index]}")
#     index += 1

# 字符串的for循环遍历
# my_str = "hello python itheima and itcast"
# for element in my_str:
#     print(f"字符串{my_str}的元素有:{element}")