def is_even(number):
    if number % 2 == 0:
        return True
    return False
is_even(3)

def hint_username(username):    # with elif
    if len(username) < 3:
        print("Invalid username.Must be atleast 3 characters long")
    elif len(username) > 15:
        print("Invalid username.Must not be more than 15 characters long")
    else:
        print("valid Username")
hint_username("su")
hint_username("sunny")
hint_username("sunnyistheusername")

def number_group(number):           # with elif
  if number > 0:
    return "Positive"
  elif number < 0:
    return "Negative"
  else:
    return "Zero"

print(number_group(10)) #Should be Positive
print(number_group(0)) #Should be Zero
print(number_group(-5)) #Should be Negative

def which(number):
    if number > 11:
        print(0)
    elif number != 10:
        print(1)
    elif number >= 20 or number < 12:
        print(2)
    else:
        print(3)
which(10)


def format_name(first_name, last_name):
    # code goes here
    if first_name == '' and last_name == '':
        string = ""

    elif last_name == "":
        string = "Name: " + first_name
    elif first_name == "":
        string = "Name: " + last_name
    else:
        string = "Name: " + last_name + ", " + first_name

    return string


print(format_name("Ernest", "Hemingway"))
# Should return the string "Name: Hemingway, Ernest"

print(format_name("", "Madonna"))
# Should return the string "Name: Madonna"

print(format_name("Voltaire", ""))
# Should return the string "Name: Voltaire"

print(format_name("", ""))


# Should return an empty string


def fractional_part(numerator, denominator):
	# Operate with numerator and denominator to
# keep just the fractional part of the quotient
	if denominator == 0 or numerator == 0:
		return 0
	else:
		fraction = ((numerator / denominator)-(numerator // denominator))
		return fraction

print(fractional_part(5, 5)) # Should be 0
print(fractional_part(5, 4)) # Should be 0.25
print(fractional_part(5, 3)) # Should be 0.66...
print(fractional_part(5, 2)) # Should be 0.5
print(fractional_part(5, 0)) # Should be 0
print(fractional_part(0, 5)) # Should be 0

def longest_word(word1, word2, word3):
	if len(word1) >= len(word2) and len(word1) >= len(word3):
		word = word1
	elif len(word2) >= len(word3):
		word = word2
	else:
		word = word3
	return(word)

print(longest_word("chair", "couch", "table"))
print(longest_word("bed", "bath", "beyond"))
print(longest_word("laptop", "notebook", "desktop"))

def calculate_storage(filesize):
    block_size = 4096

    # Use floor division to calculate how many blocks are fully occupied
    full_blocks = (filesize + block_size -  1) // block_size

    return full_blocks * block_size

assert calculate_storage(1) == 4096
assert calculate_storage(4096) == 4096
assert calculate_storage(4097) == 8192
assert calculate_storage(6000) == 8192


''' # If a filesystem has a block size of 4096 bytes,
   this means that a file comprised of only one byte will still use 4096 bytes of storage.
    A file made up of 4097 bytes will use 4096*2=8192 bytes of storage. Knowing this,
    can you fill in the gaps in the calculate_storage function below,
   which calculates the total number of bytes needed to store a file of a given size?
def calculate_storage(filesize):
    block_size = 4096
    # Use floor division to calculate how many blocks are fully occupied
    full_blocks = ___
    # Use the modulo operator to check whether there's any remainder
    partial_block_remainder = ___
    # Depending on whether there's a remainder or not, return
    # the total number of bytes required to allocate enough blocks
    # to store your data.
    if partial_block_remainder > 0:
        return ___
    return ___

print(calculate_storage(1))    # Should be 4096
print(calculate_storage(4096)) # Should be 4096
print(calculate_storage(4097)) # Should be 8192
print(calculate_storage(6000)) # Should be 8192 '''