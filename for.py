family = ["kamal", "poojitha", "purnima"]
for member in family:
    print("Hi " + member)
print("*********************************************************************")
values = [65, 56, 84, 96, 66]
sum = 0
length = 0
for value in values:
    sum += value
    length += 1

print("Total sum: " + str(sum) + " - Average " + str(sum / length))

print("*********************************************************************")


def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


print(factorial(4))  # should return 24
print(factorial(5))  # should return 120

print("*********************************************************************")


def square(n):
    return n * n


def sum_squares(x):
    sum = 0
    for n in range(x):  # ONE PARAMETRE in range, goes one by one in squence until x-1
        sum += int(square(n))
    return sum


print(sum_squares(10))  # Should be 285
print("*********************************************************************")

for x in range(1, 10):
    print(x**3)

product = 1
for n in range(
    1, 10
):  # TWO PARAMETRE in range, starts from 1 and then goes in squence until 9 (always takes 1 less which is 10-1 here)
    product *= n


print(product)  # should return multiplication of 1 to 9
print("*********************************************************************")


def to_celsius(x):
    return (x - 32) * 5 / 9


for x in range(
    0, 101, 10
):  # THREE PARAMETERS: starts from 0 , goes until 100, jumps with size of third number i.e, +10 everytime, Lookat output
    print(x, to_celsius(x))
print("*********************************************************************")

for x in range(0, 101, 7):
    print(x * 7)

def show_letters(word):
    for x in (word):
      print(x)

show_letters("Hello")
# Should print one line per letter


''' The counter function counts down from start to stop when start is bigger than stop, 
and counts up from start to stop otherwise. 
 '''

def counter(start, stop):
    	x = start
	if start > stop:
		return_string = "Counting down: "
		while x >= stop:
			return_string += str(x)
			if x != stop:
				return_string += ","
			x -= 1
	else:
		return_string = "Counting up: "
		while x <= stop:
			return_string += str(x)
			if x != stop:
				return_string += ","
			x += 1
	return return_string

print(counter(1, 10)) # Should be "Counting up: 1,2,3,4,5,6,7,8,9,10"
print(counter(2, 1)) # Should be "Counting down: 2,1"
print(counter(5, 5)) # Should be "Counting up: 5"


def even_numbers(maximum):
    	return_string = ""
    for x in (1, maximum+1):
	 if x % 2 == 0:
      return_string += str(x) + " "
	return return_string.strip()

print(even_numbers(6))  # Should be 2 4 6
print(even_numbers(10)) # Should be 2 4 6 8 10
print(even_numbers(1))  # No numbers displayed
print(even_numbers(3))  # Should be 2
print(even_numbers(0))  # No numbers displayed

