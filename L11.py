#Abstraction and Inheritance

from abc import ABC,abstractmethod
#Parent Constructor - Share the attributes to the child classes
class Animal(ABC):

    def __init__(self,name,habitat):
        self.name = name
        self.habitat = habitat
#Concrete Method-all child classes inherit this 
    def display(self):
        print(f"Name: {self.name} ¦ Habitat: {self.habitat}")
#This is the abstract method - all child need to implement this
    @abstractmethod
    def speak(self):
        pass

#Creating the first Child Class -  Dog
class Dog(Animal):
    def __init__(self,name,habitat,breed):
        super().__init__(name,habitat)
        self.breed = breed

    def speak(self):
        print(f"{self.name} the {self.breed} lives in a {self.habitat} and says 'Woof!' ")

class Cat(Animal):
    def __init__(self,name,habitat,diet):
        super().__init__(name,habitat)
        self.diet = diet

    def speak(self):
        print(f"{self.name} eats {self.diet}  and lives in {self.habitat} and says 'Meow!' ")

class Tiger(Animal):
    def __init__(self,name,habitat,species):
        super().__init__(name,habitat)
        self.species = species

    def speak(self):
        print(f"{self.name} the {self.species} lives in {self.habitat} and says 'Roar!' ")

#Creating the Objects

dog = Dog("Jacky","Golden Retriever","House")
cat  =Cat("Mr.Charles","Fish","American Animal Shelter")
tiger =Tiger("Simbah","Bengali Tiger","Madhya Pradesh(Sundarbans National Park)")

print("Animal Factfiles:")
for animal in [dog,cat,tiger]:
    animal.display()
    animal.speak()
    print( )

