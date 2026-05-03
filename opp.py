class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} издаёт звук"


class Dog(Animal):
    def speak(self):
        return f"{self.name} говорит: Гав!"


class Cat(Animal):
    def speak(self):
        return f"{self.name} говорит: Мяу!"


dog = Dog("Шарик")
cat = Cat("Мурка")

print(dog.speak())  
print(cat.speak())  