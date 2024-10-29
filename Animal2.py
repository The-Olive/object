class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name} {self.age}"
    def myFunc(self, sound):
        print(sound, sound, "I am a cat")