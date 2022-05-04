""" a method is a function that operates on a single instance of an object. Let's add a method to our class """


class Cat:
    def speaks(self):  # Defining a function as method of the class
        print("meow.. meow")


tommy = Cat()
tommy.speaks()


class Cat:
    name = "cat"  # Attribute of the instance

    def speaks(self):
        print("meow.. I'm {}".format(self.name))  # Another example to


pussy = Cat()  # First instance
pussy.name = "Pussy"
pussy.speaks()

gussy = Cat()  # Another instance
gussy.name = "Gussy"
gussy.speaks()

""" Variables that have different values for different instances of the same class are called instance variables, just like the name variable in this example """


class Cat:
    years = 0

    def cat_age(self):
        return self.years * 18  # Lets assume 1 human year is equal to 18 cat years


tommy = Cat()
print(tommy.cat_age())
tommy.years = 2
print(tommy.cat_age())


class Dog:
    years = 0

    def dog_years(self):
        return self.years * 7


fido = Dog()
fido.years = 3
print(fido.dog_years())
