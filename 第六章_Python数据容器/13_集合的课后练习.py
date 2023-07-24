"""
信息去重
有如下列表对象：
my_list = ['黑马程序员', '传智播客', '黑马程序员', '传智播客', 'itheima', 'itcast', 'itheima', 'itcast', 'best']

请：
定义一个空集合
通过for循环遍历列表
在for循环中将列表的元素添加至集合
最终得到元素去重后的集合对象，并打印输出
"""
my_list = ['黑马程序员', '传智播客', '黑马程序员', '传智播客', 'itheima', 'itcast', 'itheima', 'itcast', 'best']
# 定义一个空集合
my_set_empty = set()
# 通过for循环遍历列表
for element in my_list:
    print(f"列表my_list中的元素有:{element}")
    # 在for循环中将列表的元素添加至集合
    my_set_empty.add(element)

# 打印输出去重后的集合对象
print(my_set_empty)
