name = "sunny"
number = len(name) * 3
age = 29
print(
    "Hello {}, according to your age {} your lucky number is {}".format(
        name, age, number
    )
)  # String formating

print("your lucky number is {number}, {name}".format(name=name, number=len(name) * 3))


def student_grade(name, grade):
    return "{} received {}% on the exam".format(name, grade)


print(student_grade("Reed", 80))
print(student_grade("Paige", 92))
print(student_grade("Jesse", 85))

price = 8.5
with_tax = price * 1.35
print("Actual price is : $"+str(price), "Including taxes : $"+str(with_tax))  # This prints 8.5 2.97499, to print exact one float value use like below:
print("Actual price is : ${:.2f}, Including taxes : ${:.2f}".format(price, with_tax))   # This eliminates extra decimals , 2f is only 2 float values

def to_celsius(x):
    return(x-32)*5/9
for x in range(0,101,10):
    print("{:>3} F | {:>6.2f} C".format(x, to_celsius(x)))      # Formats with 3spaces with >3 and 6 spaces and 2 deciams with >6.2f

# "base string with {} placeholders".format(variables)

example = "format() method"

formatted_string = "this is an example of using the {} on a string".format(example)

print(formatted_string)


# "{0} {1}".format(first, second)

first = "apple"
second = "banana"
third = "carrot"

formatted_string = "{0} {2} {1}".format(first, second, third)

print(formatted_string)


# {:d} integer value   
# {:d}'.format(10.5) → '10'    # what comes after the colon is a formatting expression

def convert_distance(miles):
    km = miles * 1.6 
    result = "{} miles equals {:.1f} km"
    return result.format(miles,km)

print(convert_distance(12)) # Should be: 12 miles equals 19.2 km
print(convert_distance(5.5)) # Should be: 5.5 miles equals 8.8 km
print(convert_distance(11)) # Should be: 11 miles equals 17.6 km


def is_palindrome(input_string):
    	# We'll create two strings, to compare them
	new_string = ""
	reverse_string = ""
	# Traverse through each letter of the input string
	for string in input_string.lower():
		# Add any non-blank letters to the 
		# end of one string, and to the front
		# of the other string. 
		if string.replace(" ",""):
			new_string = new_string+string
			reverse_string = string+reverse_string
	# Compare the strings
	if reverse_string == new_string:
		return True
	return False

print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True


def nametag(first_name, last_name):
    	return"{} {}.".format(first_name, last_name[0])

print(nametag("Jane", "Smith")) 
# Should display "Jane S." 
print(nametag("Francesco", "Rinaldi")) 
# Should display "Francesco R." 
print(nametag("Jean-Luc", "Grand-Pierre")) 
# Should display "Jean-Luc G." 

def replace_ending(sentence, old, new):
    	# Check if the old string is at the end of the sentence 
	if sentence.endswith(old):
		# Using i as the slicing index, combine the part
		# of the sentence up to the matched string at the 
		# end with the new string
		i = sentence.rfind(old)
		new_sentence = sentence[:i]+new
		return new_sentence

	# Return the original sentence if there is no match 
	return sentence
	
print(replace_ending("It's raining cats and cats", "cats", "dogs")) 
# Should display "It's raining cats and dogs"
print(replace_ending("She sells seashells by the seashore", "seashells", "donuts")) 
# Should display "She sells seashells by the seashore"
print(replace_ending("The weather is nice in May", "may", "april")) 
# Should display "The weather is nice in May"
print(replace_ending("The weather is nice in May", "May", "April")) 
# Should display "The weather is nice in April"