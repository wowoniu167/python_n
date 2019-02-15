class Dog():
    """一次模拟小狗的简单尝试"""
    def __init__(self, name, age):   #是一个特殊的方法，在这个方法的名称中，开头和末尾各有两个下划线，这是一种约
#定，旨在避免Python默认方法与普通方法发生名称冲突
        """初始化属性name和age"""
        self.name = name
        self.age = age
    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title() + " is now sitting.")
    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title() + " rolled over!")

my_dog = Dog('White',6)
print("My dog name is :" + my_dog.name.title() + ".")
print("My dog is :" + str(my_dog.age) + " years old!")
my_dog.sit()
my_dog.roll_over()

#继承
def __init__(self, make, model, year):
    """初始化父类的属性"""
    super().__init__(make, model, year)