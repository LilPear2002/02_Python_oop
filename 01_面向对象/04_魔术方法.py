# 小黎专属python固定模板
# 开发时间：2024/7/14 10:29

# 类的内置方法被称为魔术方法
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("创建了一个对象，这是一个构造方法")

    def __str__(self):
        return f"Student类对象,name:{self.name},age:{self.age}"

    def __lt__(self, other):
        return self.age < other.age

    def __le__(self, other):
        return self.age <= other.age

    def __eq__(self, other):
        return self.age == other.age


stu1 = Student("小黎", 22)
stu2 = Student("小刘", 21)
print(stu1)
print(str(stu1))
print(stu1 > stu2)
print(stu1 <= stu2)
print(stu1 == stu2)
