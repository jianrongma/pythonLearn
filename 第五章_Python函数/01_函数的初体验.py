# 函数：组织好的，可重复使用的，实现特定功能的代码块
# name = "bsxdcvcu"
# length = len(name)
# print(length)

# 不使用内置函数 len()，完成字符串长度的计算
str1 = "hshcvavc"
str2 ="oiuytr"
str3 = "zxcvbn"

# 定义一个计数的变量
# count = 0
# for i in str1:
#     count += 1
# print(f"字符串{str1}的长度是：{count}")
#
# count = 0
# for i in str2:
#     count += 1
# print(f"字符串{str2}的长度是：{count}")
#
# count = 0
# for i in str3:
#     count += 1
# print(f"字符串{str3}的长度是：{count}")

# 可以使用函数来优化这个过程
def my_len(data):
    count = 0
    for i in data:
        count += 1
    print(f"字符串{data}的长度是：{count}")

my_len(str1)
my_len(str2)
my_len(str3)