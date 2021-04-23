class Planet:
    population = []

    def __init__(self, *pop):
        self.population = pop


class Animal:
    pass

class Bear(Animal):
    name = "Misha"
    age = 10

    def myName(self):
        print(self.name)

    def __str__(self):
        return "Name:" + str(self.name) + " Age:" + str(self.age)


class Wolf(Animal):
    name = "Mars"
    age = 3

    def myName(self):
        print(self.name)

    def __str__(self):
        return "Name:" + str(self.name) + " Age:" + str(self.age)


class Fox(Animal):
    name = "Barn"
    age = 2

    def myAge(self):
        print(self.age)

    def __str__(self):
        return "Name:" + str(self.name) + " Age:" + str(self.age)


fox = Fox()
bear = Bear()
wolf = Wolf()

Earth = Planet(fox, bear, wolf)


def printing(obj):
    for i in obj.population:
        print(i.__str__())


printing(Earth)
