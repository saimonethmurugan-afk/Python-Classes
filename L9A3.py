#Parrot Class

class parrot:
    species = "bird"

    def __init__ (self,name,age):
        self.name = name
        self.age = age

Bob = parrot("Bob",13)
Bart = parrot("Bart",12)

print("Bob is a {}".format(Bob.species))
print("Bart is {}".format(Bart.species))

print("{} is {} years old".format(Bob.name,Bob.age))
print("{} is {} years old".format(Bart.name,Bart.age))
