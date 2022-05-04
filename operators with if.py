def hint_username(username):
    if len(username) < 3:
        print("Invalid username." "Must be atleast 3 characters long")
    else:
        print("valid Username")
hint_username("su")
hint_username("sunny")

def is_positive(number):
  if number > 0:
    return True
  else:
    return False

is_positive(13)

def greeting(name):
  if name == "Taylor":
    return "Welcome back Taylor!"
  else:
    return "Hello there, " + name

print(greeting("Taylor"))
print(greeting("John"))