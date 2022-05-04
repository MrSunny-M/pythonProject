def get_seconds(hours, minutes, seconds):
  return 3600*hours + 60*minutes + seconds

amount_a = get_seconds(2,30,0)
amount_b = get_seconds(0,45,15)
result = amount_a + amount_b
print(result)

# example to store and use traingle height and calculating
def area_triangle(base, height):
    return base*height/2

area_a = area_triangle(3,2)
area_b = area_triangle(5,2)
sum_of_area = area_b + area_a
print ("result is " + str(sum_of_area))

# Example to convert seconds to hours and minutes
def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds
hours , minutes, seconds = convert_seconds(3601)
print(hours, minutes, seconds)

# Example to return none, if we assign the value of function to variable

def greetings(name):
    print("Welcome " + name)
result=greetings("Sunny")           # shows
print(result)                      # returns nothing, indicates empty if none assigned in a variable


def lucky_number(name):            #returns


    number = len(name) * 9
    message = "Hello " + name + ". Your lucky number is " + str(number)
    return message

print(lucky_number("Kay"))
print(lucky_number("Cameron"))


def order_numbers(number1, number2):           #returns numbers
  if number2 > number1:

    return number1, number2

  else:

    return number2, number1


(smaller, bigger) = order_numbers(100, 99)

print(smaller, bigger)


def convert_distance(miles):                 #return km
  km = miles * 1.6
  return km


result = convert_distance(55)
print("The distance in Kilometers is " + str(result))
print("The round-trip in Kilometers is " + str(result * 2))