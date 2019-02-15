#下面是一个打印问候语的简单函数，名为greet_user()：
def greet_user():
    """显示简单的问候语"""  #被称为文档字符串（docstring）的注释，描述了函数是做什么的
    #文档字符串用三引号括起，Python使用它们来生成有关程序中函数的文档
    print("Hello!")
greet_user()

def greet_user(username):
    """显示简单的问候语"""
    print("Hello, " + username.title() + "!")
greet_user('jesse')

#在函数greet_user()的定义中，变量username是一个形参——函数完成其工作所需的一项信
#息。在代码greet_user('jesse')中，值'jesse'是一个实参。实参是调用函数时传递给函数的信
#息。我们调用函数时，将要让函数使用的信息放在括号内。在greet_user('jesse')中，将实参
#'jesse'传递给了函数greet_user()，这个值被存储在形参username中

#位置实参
#你调用函数时，Python必须将函数调用中的每个实参都关联到函数定义中的一个形参。为此，
#最简单的关联方式是基于实参的顺序。这种关联方式被称为位置实

#关键字实参
#关键字实参是传递给函数的名称—值对。你直接在实参中将名称和值关联起来了，因此向函
#数传递实参时不会混淆（不会得到名为Hamster的harry这样的结果）。关键字实参让你无需考虑函
#数调用中的实参顺序，还清楚地指出了函数调用中各个值的用途
def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet(animal_type='hamster', pet_name='harry')
num = 1
def set_num(x):
    """修改数值"""
    return x
num = set_num(10)
print(num)

#传递列表,在函数中对这个列表所做的任何修改都是永
#久性的，这让你能够高效地处理大量的数据
def greet_users(names):
    """向列表中的每位用户都发出简单的问候"""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)
usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)
#禁止函数修改列表  ,切片表示法[:]创建列表的副本
#print_models(unprinted_designs[:], completed_models)

#传递任意数量的实参
#下面的函数只有一个形参*toppings，但不管调用语句提供了多少实参，这个形参都将它们
#统统收入囊中：
def make_pizza(*toppings):
    """打印顾客点的所有配料"""
    print(toppings)
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
#如果要让函数接受不同类型的实参，必须在函数定义中将接纳任意数量实参的形参放在最
#后。Python先匹配位置实参和关键字实参，再将余下的实参都收集到最后一个形参中
def make_pizza(size, *toppings):
    """概述要制作的比萨"""
    print("\nMaking a " + str(size) +
        "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

#def build_profile(first, last, **user_info):  形参**user_info中的两个星号让Python创建一个名为user_info的空字典，并将收到的所
#有名称—值对都封装到这个字典中

#将函数存储在模块中,要让函数是可导入的，得先创建模块。模块是扩展名为.py的文件，包含要导入到程序中的代码
#import pizza
#pizza.make_pizza(16, 'pepperoni')
#导入特定的函数
#from module_name import function_name
#使用as 给函数指定别名
#from pizza import make_pizza as mp
#使用as 给模块指定别名
#import pizza as p
#p.make_pizza(16, 'pepperoni')
#导入模块中的所有函数
#from pizza import *