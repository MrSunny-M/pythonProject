x = "this file is a"
y = "file"
print(x, y, sep=" .Py ", end="!")


print(2**3**2**1)

animal = "Hippopotamus"
print(animal[3:6])
print(animal[-5])
print(animal[10:])


def highlight_word(sentence, word):
    return sentence.replace(word, word.upper())


print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "loud"))
print(highlight_word("Automating with Python is fun", "fun"))


def format_address(address_string):
      # Declare variables
  house_number = ""
  street_name = ""
  # Separate the address string into parts
  address_string = address_string.split()
  # Traverse through the address parts
  for number in address_string:
    # Determine if the address part is the
    # house number or part of the street name
    if number.isdigit():
      house_number = number
  # Does anything else need to be done 
  # before returning the result?
    else:
      street_name += number
      street_name += " "
  # Return the formatted string  
  return "house number {} on street named {}".format(house_number, street_name)

print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"

def combine_lists(list1, list2):
      # Generate a new list containing the elements of list2
  # Followed by the elements of list1 in reverse order
    new_list=list2
    for i in reversed(range(len(list1))):
      new_list.append(list1[i])
    return new_list
	
Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]

print(combine_lists(Jamies_list, Drews_list))

def car_listing(car_prices):
    result = ""
    for key in car_prices:
        result += "{} costs {} dollars".format(key, car_prices[key]) + "\n"
    return result

print(car_listing({"Kia Soul":19000, "Lamborghini Diablo":55000, "Ford Fiesta":13000, "Toyota Prius":24000}))

def combine_guests(guests1, guests2):
      # Combine both dictionaries into one, with each key listed 
  # only once, and the value from guests1 taking precedence
     guests2.update(guests1)
     return guests2
Rorys_guests = { "Adam":2, "Brenda":3, "David":1, "Jose":3, "Charlotte":2, "Terry":1, "Robert":4}
Taylors_guests = { "David":4, "Nancy":1, "Robert":2, "Adam":1, "Samantha":3, "Chris":5}

print(combine_guests(Rorys_guests, Taylors_guests))

def count_letters(text):
  result = {}
  text = text.lower()
  # Go through each letter in the text
  for letter in text:
    # Check if the letter needs to be counted or not
    if letter.isalpha():
    # Add or increment the value in the dictionary
      count = text.count(letter)
      result[letter] = count
  return result

print(count_letters("AaBbCc"))
# Should be {'a': 2, 'b': 2, 'c': 2}

print(count_letters("Math is fun! 2+2=4"))
# Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}

print(count_letters("This is a sentence."))
# Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}