class Apple:
    def __init__(self, color, flavor):  # Constructor __init__  special method , with instance self
        self.color = color
        self.flavor = flavor


kashmirapple = Apple("red", "sweet")
print(kashmirapple.flavor)


class Person:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        # Should return "hi, my name is " followed by the name of the Person.
        return "hi, my name is {}".format(self.name)


# Create a new instance with a name of your choice
some_person = Person("Mike")
# Call the greeting method
print(some_person.greeting())


''' Documenting Functions, Classes, and Methods  '''

class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor
    def __str__(self):
        return "This apple is {} and its flavour is {}".format(self.color, self.flavor)

help(Apple)     # Documetning purpose, to get information defined methods in the class, with small information

''' Doc String - a bried text that explains what something does '''

def to_seconds(hours, minutes, seconds):
    """Returns the amount of seconds in the given hours, minutes, and seconds.""" # This is a docstring, to show what def function does
    return hours*3600+minutes*60+seconds

help(to_seconds)

class Person:
    def __init__(self, name):
        self.name = name
    def greeting(self):                
        """Outputs a message with the name of the person."""                   # THis is another docstring
        print("Hello! My name is {name}.".format(name=self.name)) 

some_person=Person("Greg")
print(some_person.greeting())
help(Person)                     # Describe what Person methods/functions does, especially here to check the docstring written for greeting function

class Piglet:
    """Represents a piglet that can say their name """
    years = 0
    name = ""
    def speak(self):
        """Outputs a message including name of the piglet"""
        print("Oink ! I'm {}!".format(self.name))
    def pig_years(self):
        """ Converts the current age to piglet years"""
        return self.years * 18
help(Piglet)