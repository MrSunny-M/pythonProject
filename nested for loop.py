teams = ["Dragons", "Wolves", "Pandas", "Unicorns"]
for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print(
                "teams that are going to play one against are "
                + home_team
                + " vs "
                + away_team,
                end="",
            )
        print()
print(
    "****************************************************************************************"
)

# Example for dominos game

for left in range(7):
    for right in range(left, 7):
        print(
            "[" + str(left) + "|" + str(right) + "]", end=" "
        )  # end is new parameter, this eliminate new line, suppose print("hi, ", end = "")
        #               print(whassup)       this output will be == > hi, whassup
    print()
print(
    "****************************************************************************************"
)


''' def validate_users(users):
    for user in [users]:  # if using strings in for loop, mention them as list even its one string. which means in square brackets []
        if is_valid(user):
            print(user + " is valid")
        else:
            print(user + " is invalid")


validate_users("purplecat")

print(
    "****************************************************************************************"
) '''


def retry(operation, attempts):
    for n in range(attempts):
        if operation():
            print("Attempt " + str(n) + " succeeded")
            break  # to stop the loop when succeeded
        else:
            print("Attempt " + str(n) + " failed")


# retry(create_user, 3)
# retry(stop_service, 5)

print(
    "****************************************************************************************"
)


def factorial(n):
    result = 1
    for x in range(2,n+1):
        result *= x
    return result

for n in range(10):
    print(n, factorial(n))