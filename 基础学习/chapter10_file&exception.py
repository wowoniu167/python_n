try:
    with open('python_work/file_test2') as file_object: #关键字with在不再需要访问文件后将其关闭
        contents = file_object.read()
        print(contents.rstrip())
except FileNotFoundError:
    msg = "Sorry, the file  does not exist."
    print(msg)
#要以每次一行的方式检查文件，可对文件对象使用for循环
filename = 'python_work/file_test'
with open(filename) as file_object:
    for line in file_object:
        print (line.rstrip())
#创建一个包含文件各行内容的列表
#使用关键字with时，open()返回的文件对象只在with代码块内可用。如果要在with代码块外
#访问文件的内容，可在with代码块内将文件的各行存储在一个列表中，并在with代码块外使用该
#列表：你可以立即处理文件的各个部分，也可推迟到程序后面再处理
with open(filename) as file_object:
    lines = file_object.readlines()                   #方法readlines()从文件中读取每一行，并将其存储在一个列表中
for line in lines:                                    #列表lines的每个元素都对应于文件中的一行
    print(line.rstrip())
#如果你要写入的文件不存在，函数open()将自动创建它。然而，以写入（'w'）模式打开文
#件时千万要小心，因为如果指定的文件已经存在，Python将在返回文件对象前清空该文件
filename = 'python_work/write_file1.txt'
with open(filename,'w') as file_object:               #w模式写入会覆盖原文件  a 模式为附加
    file_object.write("I love programming.\n")        #写入时不换行，想要换行则在末尾添加 \n
    file_object.write("I love programming1.\n")

#Python使用被称为异常的特殊对象来管理程序执行期间发生的错误
try:
    answer = print(5/1)
except ZeroDivisionError:
    print("You can't divide by zero!")
else:                                           #else 代码块
    print(answer)
#分析文本 split() 将文本按空格拆分字符
filename = 'python_work/file_test'
try:
    with open(filename) as file_object:
        lines = file_object.read()
except FileNotFoundError:
    pass   #pass 表示什么都不做
else:
    words = lines.split()
    print(len(words))
#存储数据 使用json.dump()和json.load()
import json
numbers = [2, 3, 5, 7, 11, 13]
filename = 'numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)


filename = 'numbers.json'
with open(filename) as f_obj:
    numbers = json.load(f_obj)
print(numbers)