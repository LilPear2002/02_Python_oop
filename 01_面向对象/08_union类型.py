# 小黎专属python固定模板
# 开发时间：2024/7/14 14:53

# 使用Union类型可以定义联合类型注解
from typing import Union

my_list: list[Union[str, int]] = [1, 2, "xiaoli"]
my_dict: dict[str, Union[str, int]] = {"xiaoli": 666, "小黎": "nb"}


def func(data: Union[int, str]) -> Union[int, str]:
    pass
