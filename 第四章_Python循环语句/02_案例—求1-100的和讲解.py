"""
需求：通过while循环，计算从1累加到100的和

提示：
1. 终止条件不要忘记，设置为确保while循环100次
2. 确保累加的数字，从1开始，到100结束
"""
sum = 0
i = 1
while i<=100:
    sum += i
    i += 1

print(f"从1累加到100的和是:{sum}")