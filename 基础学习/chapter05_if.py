#编程时经常需要检查一系列条件，并据此决定采取什么措施。在Python
#中，if语句让你能够检查程序的当前状态，并据此采取相应的措施。
#在本章中，你将学习条件测试，以检查感兴趣的任何条件。你将
#学习简单的if语句，以及创建一系列复杂的if语句来确定当前到底处
#于什么情形。接下来，你将把学到的知识应用于列表，以编写for循
#环，以一种方式处理列表中的大多数元素，并以另一种不同的方式处
#理包含特定值的元素。
cars = ['audi','bwm','subaru','toyota']
for car in cars:
    if car == 'bwm':    # 符号==判断相等
        print(car.upper())
    else:
        print(car.title())
#判断相等时区分大小写，可以使用lower()
cars = ['audi','Bwm','subaru','toyota']
for car in cars:
    if car.lower() == 'bwm':    # lower() 不修改变量本身的值
        print(car.upper())
    else:
        print(car.title())
#不相等 != < > <= >=   and or

#关键字 in 判断特定值是否包含再列表中  / not in
requested_toppings = ['mushrooms', 'onions', 'pineapple']
if "mushrooms" in requested_toppings:
    print('mushrooms')

gemeactive = False
if gemeactive:
    print(gemeactive)
print(gemeactive)

# if elif esle 结构
age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")
# 判断列表是否为空
requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
        print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")