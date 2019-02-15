#在本章中，你将学习能够将相关信息关联起来的Python字典。你
#将学习如何访问和修改字典中的信息。鉴于字典可存储的信息量几乎
#不受限制，因此我们会演示如何遍历字典中的数据。另外，你还将学
#习存储字典的列表、存储列表的字典和存储字典的字典。
#理解字典后，你就能够更准确地为各种真实物体建模。你可以创
#建一个表示人的字典，然后想在其中存储多少信息就存储多少信息
# 姓名、年龄、地址、职业以及要描述的任何方面。你还能够存储任意
#两种相关的信息，如一系列单词及其含义，一系列人名及其喜欢的数
#字，以及一系列山脉及其海拔等。

#来看一个游戏，其中包含一些外星人，这些外星人的颜色和点数各不相同。下面是一个简单
#的字典，存储了有关特定外星人的信息：
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])
#添加键—值对
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
#修改值
alien_0['y_position'] = 5
print(alien_0)
#删除键-值对
del alien_0['x_position']
print(alien_0)

#遍历字典
for k , v in alien_0.items():
    print("\nkey:" + k )
    print("value:" + v.__str__() )
#遍历字典所有键
for key1 in alien_0.keys():#遍历字典时，会默认遍历所有的键，因此，如果将上述代码中的for name in favorite_
#languages.keys():替换为for name in favorite_languages:，输出将不变
    print(key1)
#根据键获取值
    print(alien_0[key1])

#按顺序遍历键
for key2 in sorted(alien_0.keys()): #sorted函数获取了字典的副本
    print(key2)

#遍历值
for value1 in alien_0.values():
    print(value1)

print("使用set 去除重复值")
for value2 in set(alien_0.values()):
    print(value2)

#嵌套 字典列表
print("字典列表")
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

#列表字典
# 存储所点比萨的信息
pizza = {
        'crust': 'thick',
        'toppings': ['mushrooms', 'extra cheese'],
        }
# 概述所点的比萨
print("You ordered a " + pizza['crust'] + "-crust pizza " +
    "with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)
#字典中的字典
print("字典中的字典")
users = {
         'aeinstein': {
             'first': 'albert',
             'last': 'einstein',
             'location': 'princeton',
             },

         'mcurie': {
             'first': 'marie',
             'last': 'curie',
             'location': 'paris',
             },
         }

for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())
#字典中的字典，尽量保持字典结构相同，这样处理更简单