

class Animal:
    def __init__(self, type, weight, color, breed, teeth ):
        #type, weight, color, breed, teeth are attributes
        self.weight = weight
        self.type = type
        self.color =color
        self.breed =breed
        self.teeth = teeth
#functions bark(), fly(), are called behaviours
#
    def bark(self):
        print("hoo hoo hoo")

    def fly(self):
        print("zzzzzz zzzzz zzzz")

    def set_number_teeth(self):
        teeth = self.teeth

    def get_number_teeth(self):
        return self.teeth


#instance of the class or object
my_dog = Animal("dog" ,76, "brown", "mexican", 42)
my_parrot = Animal("parrot" ,23, "green", "carribean", 0)

#dog and parrot inherits properties of animal 
my_dog.bark()
my_parrot.fly()



