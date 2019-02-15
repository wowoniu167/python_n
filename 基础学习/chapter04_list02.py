## 第四章 列表操作 --20190127
#for 循环遍历列表,,,For 循环在未缩进处结束
magicians = ['alice', 'david', 'carolina'];
for magician in magicians:    # 冒号是必须的
    print(magician)           # 缩进，在循环内执行
    print(magician + str(1))  # 缩进，在循环内执行
print(magician)               # 不缩进，不在循环内执行


#使用函数 range()创建一个数字列表，函数range()让Python从你指定的第一个值开始数，并在到达你指定的第二个值后停止，因此输出
#不包含第二个值（这里为5 ）
for value in range(1,5):
    print(value)
number = list(range(0,10));
print(number);
# min max sumn 计算数字列表
#
#squares = [value**2 for value in range(1,11)]
squares = [value**2 for value in range(1,11)]
print(squares);
#列表切片
print(squares[0:3]);
#使用切片复制列表
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print(my_foods);
print(friend_foods);
#元组看起来犹如列表，但使用圆括号而不是方括号来标识。定义元组后，就可以使用索引来
#访问其元素，就像访问列表元素一样
dimensions = (200, 50)
#元组的元素不能修改值
#dimensions[0] = 250   #试图修改元组元素，报错“TypeError: 'tuple' object does not support item assignment”
print(dimensions[0])

#遍历元组的元素，同列表使用for
for dimension in dimensions:
    print(dimension)

#修改元组变量
#虽然不能修改元组的元素，但可以给存储元组的变量赋值。因此，如果要修改前述矩形的尺
#寸，可重新定义整个元组：

dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
