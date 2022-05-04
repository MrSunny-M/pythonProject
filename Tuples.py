def convert_seconds(seconds):
    hours=seconds//3600
    minutes=(seconds-hours*3600)//60
    remaining_seconds=seconds-hours*3600 -minutes*60
    return hours, minutes, remaining_seconds

print(convert_seconds(1800))
print(type(convert_seconds(1800)))

hours, minutes, seconds = convert_seconds(1800)    # Tuples can be changed into seperate variables
print(hours, minutes, seconds)

def file_size(file_info):
    name, type, size = file_info
    return("{:.2f}".format(size / 1024))

print(file_size(('Class Assignment', 'docx', 17875))) # Should print 17.46
print(file_size(('Notes', 'txt', 496))) # Should print 0.48
print(file_size(('Program', 'py', 1239))) # Should print 1.21

animals = ["Tiger", "Zebra", "Lion", "Bear"]    # Lists
char = 0
for animal in animals:
    char += len(animal)             # To calculate the length of single element
print("Total Characters: {}, Average length:{}".format(char, char // len(animals))) # here len(animals) calculates total elements

students = ["sunny","kamal","poojitha"]
print("Ranks - Names")
for index, student in enumerate(students):  # Using enumerate function to index of the elements in the sequence
    print("{} - {}".format(index + 1, student))

# Iterating over Lists and Tuples #

def generate_emails(employees):
    result = []
    for email, name in employees:       # Iterating over lists
        result.append("{} <{}>".format(name, email))
    return result
print(generate_emails([("saikiran.m@company.com", "Saikiran M"),("Kamal@company.com", "Kamal")]))

def skip_elements(elements):
    	# code goes here
	list = []
	for index,element in enumerate(elements):
		if index % 2 == 0:
			list.append('{}'.format(element))
	return list

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
