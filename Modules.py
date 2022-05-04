'''   modules are separate files that contain classes, functions, and other data that allow us to import and make use of these methods and classes in our own code. 
Python comes with a lot of modules out of the box. These modules are referred to as the Python Standard Library. 
You can make use of these modules by using the import keyword, followed by the module name. '''

import random
print(random.randint(1,100))    # randint is the class of random module
print(random.randint(1,100))
print(random.randint(1,100))

import datetime
now = datetime.datetime.now()   # datetime is the class of datetime module
print(now)
print(type(now))    # Prints the type of now
print(now.year)
print(now + datetime.timedelta(days=25))     # timedelta is another class of datetime module




