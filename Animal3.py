class Bird:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def __str__(self):
        return f"{self.name} {self.type}"

    def sound(self):
        return "I wanna cracker"