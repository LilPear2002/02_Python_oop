# 小黎专属python固定模板
# 开发时间：2024/7/14 11:56

# 定义一个类，其中包含私有成员变量和私有成员方法
class Phone:

    __current_voltage = 0.5

    def __keep_single_core(self):
        print("让CPU以单核模式运行")

    def call_by_5g(self):
        if self.__current_voltage >= 1:
            print("5g通话已开启")
        else:
            self.__keep_single_core()
            print("无法使用5g通话")


phone = Phone()
phone.call_by_5g()