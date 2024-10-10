# 小黎专属python固定模板
# 开发时间：2024/7/14 14:59

class Animal:
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        print("汪汪汪")


class Cat(Animal):
    def speak(self):
        print("喵喵喵")


def make_noise(animal: Animal):
    animal.speak()


# 多态的基本演示:
dog = Dog()
cat = Cat()

make_noise(dog)
make_noise(cat)
