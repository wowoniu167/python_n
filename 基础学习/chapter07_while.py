#函数input()
print("函数input")
#massge = input("Please input Y/N:")
#print(massge)

#int()函数获取数字
#age = input("How old are you: ")
#age = int(age)    #字符类型转换为数字
#if age == 18:
#    print(age)
#使用while 循环
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'Q/q' to end the program. "
message = ""
while message.title() != 'Q':     #title() 大写
    message = "Q"
#    message = input(prompt)
    if message.title() != 'Q':
        print(message)
#使用标志
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'Q/q' to end the program. "
message = ""
active = True
while active:     #title() 大写
#    message = input(prompt)
    message = "Q"
    if message.title() != 'Q':
        print(message)
    else:
        active = False   #使用break 退出循环
#使用continue
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

#for循环是一种遍历列表的有效方式，但在for循环中不应修改列表，否则将导致Python难以
#跟踪其中的元素。要在遍历列表的同时对其进行修改，可使用while循环。通过将while循环同列
#表和字典结合起来使用，可收集、存储并组织大量输入，供以后查看和显示
