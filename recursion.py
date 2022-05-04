''' The function sum_positive_numbers should return the sum of all positive numbers between the number n received and 1. 
For example, when n is 3 it should return 1+2+3=6, and when n is 5 it should return 1+2+3+4+5=15. Fill in the gaps to make this work: '''

def sum_positive_numbers(n):
    # The base case is n being smaller than 1
    sum = 0
    if n == 1:
        return 1
    # The recursive case is adding this number to 
    # the sum of the numbers smaller than this one.
    return sum+n + sum_positive_numbers(n-1)

print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15

print("************************************************************************************************")

''' Here, we're defining a function called factorial. 
At the beginning of the function, we have a conditional block defining the base case, where n is smaller than 2. 
It simply returns the value 1. After the base case, we have a line where the factorial function is calling itself with n minus 1. 
This is called the recursive case. This creates a loop. Each time the function is executed, it calls itself with a smaller number until it reaches the base case. 
Once it reaches the base case, it returns the value 1. 
Then the previously called function multiplies that by two and the previously called function multiplies it by three and so on. 
This loop will keep going until the first factorial function called returns the desired result. '''

def factorial(n):
    print("Factorial called with " +str(n))
    if n < 2:
        print("Returning 1")
        return 1                                                            # Base case
    result = n * factorial(n-1)                                             # Recursive case
    print("Returning " + str(result) + " for factorial of " + str(n))
    return result                                                           # recursive function to print all the results recursively.
factorial(10)


''' Problem: Fill in the blanks to make the is_power_of function return whether the number is a power of the given base. 
Note: base is assumed to be a positive number. 
Tip: for functions that return a boolean value, you can return the result of a comparison. '''

def is_power_of(number, base):
      # Base case: when number is smaller than base.
  if number < base:
    # If number is equal to 1, it's a power (base**0).
    return number == 1

  # Recursive case: keep dividing number by base.
  return is_power_of(number/base, base)

print(is_power_of(8,2)) # Should be True
print(is_power_of(64,4)) # Should be True
print(is_power_of(70,10)) # Should be False


''' def count_users(group):
      count = 0
  for member in get_members(group):
    count += 1
    if is_group(member):
      count += count_users(member) - 1
  return count

print(count_users("sales")) # Should be 3
print(count_users("engineering")) # Should be 8
print(count_users("everyone")) # Should be 18 '''


''' Implement the sum_positive_numbers function, as a recursive function that returns the sum of all positive numbers between the number n received and 1.
 For example, when n is 3 it should return 1+2+3=6, and when n is 5 it should return 1+2+3+4+5=15. '''

def sum_positive_numbers(n):
    if n == 0:
       return n
    return n + sum_positive_numbers(n-1)

print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15