ip_address = ["192.168.0.1", "127.0.0.1", "1.1.1.1"]        # Example for lists, pass to ping each server


x = ["am", "trying", "to", "code"]  # example for list
print(x)
print(type(x))  # checks any data type of variable, outputs <class 'list'>
print(len(x))  # counts number of elements in a list
print("trying" in x)  # prints boolean value
print("he" in x)
print(x[0])  # prints first value


def get_word(sentence, n):
    # Only proceed if n is positive
    if n > 0:
        words = sentence.split(" ")
        # Only proceed if n is not more than the number of words
        if n <= len(words):
            return words[n - 1]
    return ""


print(get_word("This is a lesson about lists", 4))  # Should print: lesson
print(get_word("This is a lesson about lists", -4))  # Nothing
print(get_word("Now we are cooking!", 1))  # Should print: Now
print(get_word("Now we are cooking!", 5))  # Nothing

fruits = ["pineapple", "apple", "orange"]
fruits.append("kiwi")
print(fruits)
fruits.insert(0, "lemon")
print(fruits)
fruits.insert(30, "watermelon")
print(fruits)
fruits.remove("lemon")  # or also can use pop method
print(fruits)
fruits.pop(4)
print(fruits)
fruits[2] = "strawberry"
print(fruits)


def skip_elements(elements):
    # Initialize variables
    new_list = []
    i = 0

    # Iterate through the list
    for skip in elements:
        # Does this element belong in the resulting list?
        if i % 2 == 0:
            # Add this element to the resulting list
            new_list.append(skip)
        # Increment i
        i += 1

    return new_list


print(
    skip_elements(["a", "b", "c", "d", "e", "f", "g"])
)  # Should be ['a', 'c', 'e', 'g']
print(
    skip_elements(["Orange", "Pineapple", "Strawberry", "Kiwi", "Peach"])
)  # Should be ['Orange', 'Strawberry', 'Peach']
print(skip_elements([]))  # Should be []


# Lists Comprehensions #

multiples = []
for x in range(1, 11):
    multiples.append(x * 7)
print(multiples)

multiples = [x*10 for x in range (1,11)]
print(multiples)

languages = ["python", "java", "javascript", "c", "c++", "groovy"]
lengths = [len(lang) for lang in languages]
print(lengths)

z = [x for x in range(0, 101) if x % 3 == 0]	# prints 3 divisible with 0 as remainder
print(z)

def odd_numbers(n):
    	return [x for x in range(0, n+1) if x % 2 == 1]

print(odd_numbers(5))  # Should print [1, 3, 5]
print(odd_numbers(10)) # Should print [1, 3, 5, 7, 9]
print(odd_numbers(11)) # Should print [1, 3, 5, 7, 9, 11]
print(odd_numbers(1))  # Should print [1]
print(odd_numbers(-1)) # Should print []

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
newfilenames = [letter.replace('.hpp','.h') for letter in filenames]

print(newfilenames) 
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]



def pig_latin(text):
    words = text.split()
    text=[]
    for word in words:
    # Create the pig latin word and add it to the list
       word=word[1:]+word[0]+"ay"
    text.append(word)
    # Turn the list back into a phrase
    return " ".join(text)
		
print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"


def guest_list(guests):
        for guest in name, age, job in guests:
    name, age, job = guest
print("{} is {} years old and works as {}".format(name, age, job))

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])

"""
Output should match:
Ken is 30 years old and works as Chef
Pat is 35 years old and works as Lawyer
Amanda is 25 years old and works as Engineer
"""

def group_list(group, users):
    members = ", ".join(users)
    return ("{}: {}".format(group, members))

print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", "")) # Should be "Users:"

def octal_to_string(octal):
    result = ""
    value_letters = [(4,"r"),(2,"w"),(1,"x")]
    # Iterate over each of the digits in octal
    for i in [int(n) for n in str(octal)]:
        # Check for each of the permissions values
        for value, letter in value_letters:
            if i >= value:
                result += letter
                i -= value
            else:
                result += '-'
    return result
    
print(octal_to_string(755)) # Should be rwxr-xr-x
print(octal_to_string(644)) # Should be rw-r--r--
print(octal_to_string(750)) # Should be rwxr-x---
print(octal_to_string(600)) # Should be rw-------