class Dog:
    def __init__(self, name):
        self.name = name

class Cat:
    def __init__(self, name):
        self.name = name

def animal_sound(animal):
    match animal:
        case Dog(name):  # Matches Dog object
            print(f"{name} says Woof!")
        case Cat(name):  # Matches Cat object
            print(f"{name} says Meow!")
        case _:
            print("Unknown animal")

dog = Dog("Rex")
cat = Cat("Whiskers")

animal_sound(dog)   # Output: Rex says Woof!
animal_sound(cat)   # Output: Whiskers says Meow!
