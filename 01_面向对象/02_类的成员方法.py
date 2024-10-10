# 小黎专属python固定模板
# 开发时间：2024/7/14 10:05

class Student:
    name = None

    def sai_hi(self):
        print(f"大家好,我是{self.name}")

    def sai_hi2(self,msg):
        print(f"大家好,我是{self.name},{msg}")

# 创建对象
stu = Student()
stu.name = "小黎"
stu.sai_hi()

stu2 = Student()
stu2.name = "xiaoli"
stu2.sai_hi2("多多关照")
