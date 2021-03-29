class SpaceObject:
        pass
class Planet(SpaceObject):
        population=[]
        def _init_(self,*population):
                self._population=population
        

class Animal:
        def repr(self):
                for i in self.population:
                        print(i.name)
        def str(self):
                for i in self.population:
                        print(i.name)


class Bear(Animal):
        def voise():
                print("Ga-a-a")
class Wolf(Animal):
        name="Mars"
        year=3
        def voise():
                print("Uu-u-u")
class Fox(Animal):
        name="Barn"
        year=2
        def voise():
                print("Pi-p-i")
earth = (Planet(Bear,Wolf,Fox))
       
