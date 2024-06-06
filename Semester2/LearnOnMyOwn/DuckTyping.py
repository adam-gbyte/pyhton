class Dog:
    def sound(self):
        return 'Woof'


class Cat:
    def sound(self):
        return 'Meow'


class Duck:
    def sound(self):
        return 'Quack'

    def say(self):
        return 'Hallo'


def make_sound(animal):
    return animal.sound()


def make_hello(animal):
    return animal.say()


dog = Dog()
cat = Cat()
duck = Duck()

print(make_sound(dog))
print(make_sound(cat))
print(make_hello(duck))
