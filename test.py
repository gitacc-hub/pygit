from abc import abstractmethod,ABC
class Animal:
    def __init__(self,species,name):
        self.species=species
        self.name=name
    @abstractmethod
    def move(self):
        pass
class Human(Animal):
    def __init__(self,species,name,race):
        super().__init__(species,name)
        self.race=race
    def move(self):
        return "A human being can walk or run"
human1=Human("Mammal","Human","Somali")
print(human1.move())
