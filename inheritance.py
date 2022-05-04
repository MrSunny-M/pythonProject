# Inheritance - Child classes having same attributes and methods in them.


class Fruit:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor


class Apple(Fruit):  # This is inheritance, using Fruit as parent
    pass


class Grape(Fruit):
    pass


kashmiriapple = Apple("Green", "sweet")  # instance of a class
keralagrape = Grape("Black", "sour")

print(kashmiriapple.color)
print(keralagrape.flavor)


class Clothing:
    material = ""

    def __init__(self, name):
        self.name = name

    def checkmaterial(self):
        print("This {} is made of {}".format(self.name, self.material))


class Shirt(Clothing):
    material = "Cotton"


polo = Shirt("Polo")
polo.checkmaterial()


class Animal:
    sound = ""

    def __init__(self, name):
        self.name = name

    def speak(self):
        print(
            "It is {name} and it says {sound}".format(name=self.name, sound=self.sound)
        )


class Piglet(Animal):
    sound = "Oink"


hamlet = Piglet("hamlet")
hamlet.speak()


class Cow(Animal):
    sound = "Moooo"


milky = Cow("Milky White")
milky.speak()


##  Composition


class Repository:
    def __init__(self):
        self.packages = {}  # Always initialize mutable attributes in the constructor.

    def add_packages(self, package):
        self.packages[package.name] = package

    def total_size(self):
        result = 0
        for package in self.packages.values():
            result += package.size
        return result


class Clothing:
    stock = {"name": [], "material": [], "amount": []}

    def __init__(self, name):
        material = ""
        self.name = name

    def add_item(self, name, material, amount):
        Clothing.stock["name"].append(self.name)
        Clothing.stock["material"].append(self.material)
        Clothing.stock["amount"].append(amount)

    def Stock_by_Material(self, material):
        count = 0
        n = 0
        for item in Clothing.stock["material"]:
            if item == material:
                count += Clothing.stock["amount"][n]
                n += 1
        return count


class shirt(Clothing):
    material = "Cotton"


class pants(Clothing):
    material = "Cotton"


polo = shirt("Polo")
sweatpants = pants("Sweatpants")
polo.add_item(polo.name, polo.material, 4)
sweatpants.add_item(sweatpants.name, sweatpants.material, 6)
current_stock = polo.Stock_by_Material("Cotton")
print(current_stock)
