# 小黎专属python固定模板
# 开发时间：2024/7/14 13:58

class Phone:
    IMEI = None
    producer = "HM"

    def call_by_4g(self):
        print("4g通话")


# 单继承
class Phone2022(Phone):
    face_id = "10001"

    def call_by_5g(self):
        print("5g通话")


phone = Phone2022()
print(phone.producer)
phone.call_by_4g()
phone.call_by_5g()


# 多继承
class NFCReader:
    nfc_type = "第五代"
    producer = "HM"

    def read_card(self):
        print("NFC读卡")

    def write_card(self):
        print("NFC写卡")


class RemoteControl:
    rc_type = "红外遥控"

    def control(self):
        print("开启红外遥控")


class MyPhone(Phone,NFCReader, RemoteControl):

    producer = "xiaoli"

    def call_by_4g(self):
        print("子类对父类方法的复写_4g通话")


phone = MyPhone()
phone.call_by_4g()
phone.read_card()
phone.write_card()
phone.control()
print(phone.producer)