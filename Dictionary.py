host_names = {"router": "192.168.0.1", "localhost": "127.0.0.1", "cloudflareDNS": "1.1.1.1"}  # Example for dictionary, pair hostnames with address

x = {}
print(type(x))

file_count = {
    "txt": 8,
    "pdf": 16,
    "html": 2,
    "py": 7,
}  # Dicts are mutable and stored as key and value type
print(file_count)
print("txt" in file_count)
print(file_count["pdf"])  # Prints vaule of particular key
file_count["csv"] = 3   # Adds another key and value to existing
print(file_count)
file_count["html"] = 4          # Replaces existing key and value
print(file_count)
del file_count["csv"]
print(file_count)

toc = {"Introduction":1, "Chapter 1":4, "Chapter 2":11, "Chapter 3":25, "Chapter 4":30}
toc["Chapter 3"] = 24
toc.update({"Epilogue":39})
print # Epilogue starts on page 39
# Chapter 3 now starts on page 24
print(toc) # What are the current contents of the dictionary?
print("Chapter 5" in toc == 39) # Is there a Chapter 5?

file_counts={"pdf":1,"html":2,"csv":3}
for extension in file_counts:                        # Iterating over contents of a dictionary
    print(extension)

for ext, amount in file_counts.items():
    print("There are {} of file with {} type".format(amount, ext))

print(file_counts.keys())
print(file_counts.values())

cool_beasts = {"octopuses":"tentacles", "dolphins":"fins", "rhinos":"horns"}
for name, part in cool_beasts.items():
    print("{} have {}".format(name, part))

def count_letters(text):
    result = {}
    for letter in text:
        if letter not in result:
            result [letter] = 0
        result[letter] += 1
    return result
print(count_letters("what man"))
print(count_letters("heyyyy myannnn ssup"))

wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}       # Iterate Lists with dictionary keys and values
for apparel, colors in wardrobe.items():
	for colour in colors:
		print("{} {}".format(colour, apparel))


def add_prices(basket):
    	# Initialize the variable that will be used for the calculation
	total = 0
	# Iterate through the dictionary items
	for item, price in basket.items():
		# Add each price to the total calculation
		# Hint: how do you access the values of
		# dictionary items?
		total += price
	# Limit the return value to 2 decimal places
	return round(total, 2)  

groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59, 
	"coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}

print(add_prices(groceries)) # Should print 28.44


def email_list(domains):
    	emails = []
        for dom, users in domains.items():  
	  for user in users:
	    emails.append(user + "@" + dom)
	return(emails)

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))

''' Output should be : ['clark.kent@gmail.com', 'diana.prince@gmail.com', 'peter.parker@gmail.com', 'barbara.gordon@yahoo.com', 'jean.grey@yahoo.com', 'bruce.wayne@hotmail.com'] '''


def groups_per_user(group_dictionary):
    	user_groups = {}
	# Go through group_dictionary
	for group, users in group_dictionary.items():
		# Now go through the users in the group
		for user in users:
			# Now add the group to the the list of
# groups for this user, creating the entry
# in the dictionary if necessary
			if user not in user_groups:
				user_groups[user] = []
			user_groups[user].append(group)

	return(user_groups)

print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))

''' Output: {'admin': ['local', 'public', 'administrator'], 'userA': ['local'], 'userB': ['public']}
 '''