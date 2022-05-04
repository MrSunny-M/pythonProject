x = 0
while x < 5:
    print("loop until it equates 5, now the number is just " + str(x))
    x = x + 1
    print("x=" + str(x))


def attempts(n):
    x = 1
    while x <= n:
        print("Attempt " + str(x))
        x += 1  # short hand version x=x+1
    print("done")


attempts(5)


""" username=get_username()
while not valid_username(username):
    print("Invalid username")
username=get_username(sunny) """

my_var = 5
while my_var < 10:
    print("Hello")
    my_var += 1


def count_down(start_number):
    while start_number > 0:
        print(start_number)
        start_number -= 1
    print("Zero!")


count_down(3)


def print_range(start, end):
    # Loop through the numbers from start to end
    n = start
    while n <= end:
        print(n)
        n += 1  # will be infinite loop if not added this


print_range(1, 5)  # Should print 1 2 3 4 5 (each number on its own line)


if x != 0:
    while x % 2 == 0:
        x = x / 2

        # OR #

while x != 0 and x % 2 == 0:
    x = x / 2


""" while True:                                                             This is to break infinite loops with break
    do_something()
    if user_requested_to_stop():
        break """


number = 1
while number <= 7:
    print(number, end=" ")
    number += 1


# For calculating how many digits in a given number


def digits(n):
    count = 0
    if n == 0:
        return 1
    while n > 0:
        count += 1
        n = n // 10
        return count


print(digits(25))  # Should print 2
print(digits(144))  # Should print 3
print(digits(1000))  # Should print 4
print(digits(0))  # Should print 1

# Another short example to calculate how many in numbers in a integer, use below simple code below


def digits(n):
    return len(str(n))


print(digits(25))
print(digits(144))
print(digits(1000))
print(digits(0))


""" Fill in the blanks so that calling multiplication_table(1, 3) will print out:
1 2 3 
2 4 6 
3 6 9 """


def multiplication_table(start, stop):
    for x in range(start, stop + 1):
        for y in range(start, stop + 1):
            print(str(x * y), end=" ")
        print()


multiplication_table(1, 3)
# Should print the multiplication table shown above

for x in range(1, 10, 3):
    print(x)

for x in range(10):
    for y in range(x):
        print(y)



