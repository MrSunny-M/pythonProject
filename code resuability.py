name = "sunny"
number = len(name) * 9

print ("Hello " + name + " your lucky number is " + str(number))

name = "poojitha"
number = len (name) * 9

print ("Hello " + name + " Your lucky number is " + str(number))

## Above code can be written as

def lucky_number(name):
    number=len(name) * 9
    print("Hello " + name + " Your lucky number is " + str(number))

lucky_number("Sunny")
lucky_number("Poojitha")


#### I worked another example

''' # REPLACE THIS STARTER CODE WITH YOUR FUNCTION
june_days = 30
print("June has " + str(june_days) + " days.")
july_days = 31
print("July has " + str(july_days) + " days.") '''

def month_days(month, days):
    print(month + " has " + str(days) + " days.")

month_days ('June', 30)
month_days ('July', 31)

# Code styling is important, below is example for bad code with not understanding variables

def calculate(d):
    q = 3.14
    z = q * (d ** 2)
    print(z)

calculate(5)

def circle_area(radius):               # After refactoring the code
    pi = 3.14
    area = pi * (radius ** 2)
    print(area)

circle_area(5)

def rectangle_area(base, height):            # Another example for code refactor
	area = base*height  # the area is base*height
	print("The area is " + str(area))

rectangle_area(5, 6)