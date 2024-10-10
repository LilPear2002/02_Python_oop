# 小黎专属python固定模板
# 开发时间：2024/7/14 14:28

# 基础数据类型注解
var_1: int = 10
var_2: str = "xiaoli"
var_3: bool = True


# 类对象类型注解
class Student:
    pass


stu: Student = Student()
# 基础容器类型注解
my_list1: list = [1, 2, 3]
my_tuple1: tuple = (1, 2, 3)
my_dict1: dict = {"xiaoli": 666}
# 详细注解
my_list2: list[int] = [1, 2, 3]
my_tuple2: tuple[int, str, bool] = (1, "xiaoli", True)
my_dict2: dict[str, int] = {"xiaoli": 666}

# 在注释中注解
name = "xiaoli2"  # type: str


# 方法类型注解  形参注解 返回值注解
def add(x: int, y: int) -> int:
    return x + y


print(add(1, 2))
