# 小黎专属python固定模板
# 开发时间：2024/7/14 10:21

class Student:

    def __init__(self, name, age, tel):
        self.name = name
        self.age = age
        self.tel = tel
        print("创建了一个对象，这是一个构造方法")


stu = Student("小黎", 22, 130)
print(stu.name)
print(stu.age)
print(stu.tel)
