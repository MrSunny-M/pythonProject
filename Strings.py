def double_word(word):
    result = word * 2
    return result + str(len(result))


print(double_word("hello"))  # Should return hellohello10
print(double_word("abc"))  # Should return abcabc6
print(double_word(""))  # Should return 0


def first_and_last(message):
    if not message or message[0] == message[-1]:
        return True
    return False


print(first_and_last("else"))
print(first_and_last("tree"))
print(first_and_last(""))


color = "orange"
print(color[1:5])  # for selecting particular letters range
fruit = "watermelon"
print(fruit[:5] + fruit[5:])  # for the first 5 letters and last 5 letters

message = "there was a typo in this message"
new_message = (
    message[:6] + "is" + message[9:]
)  # changing the variable by assigning it to new variable, by replacing text
print(new_message)


word = "supercalifragilisticexpialidocious"
print(word.index("x"))  # prints postition of letter

word = "super nice"
"super" in word  # Returns True/False , useful to check if we have particular word in a sentence
"delicious" in word

"Mountains".upper()  # Changes the upper case
"Mountains".lower()

answer = "YES"
if answer.lower() == "yes":  # lowers the upper case
    print("User said yes")

answer = "yes "
if (
    answer.strip() == "yes"
):  # removes whitespace, use .lstrip or .rstrip for left or right spaces
    print("User said yes again")


def replace_domain_in_email(
    email, old_domain, new_domain
):  # using strings with functions for a small program to replace domain name in e-mail
    if "@" + old_domain in email:
        index = email.index("@" + old_domain)
        new_email = email[:index] + "@" + new_domain
        return new_email
    return email


print(replace_domain_in_email("saikiran.m@outlook.in", "outlook.in", "gmail.com"))


"forest".endswith("rest")  # check if substring is ending with string

"This is my sentence".count("i")  # counts characters or strings in the sentence

"12345".isnumeric()  # Checks if the string is numeric

print(int("11111") + int("22222"))  # strings can be added if we add string type

print(
    " ".join(["this", "is", "a", "b", "c", "d"])
)  # joins the letters with join string
print("---".join(["this", "is", "a", "b"]))

split = "this is another example".split()
print(split)


def initials(phrase):
    words = phrase.split()
    result = ""
    for word in words:
        result += word[0].upper()
    return result


print(initials("Universal Serial Bus"))  # Should be: USB
print(initials("local area network"))  # Should be: LAN
print(initials("Operating system"))  # Should be: OS