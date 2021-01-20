# Using logical operators, determine if a user-entered text string has a length greater than or equal to 3 and in turn is less than 10 (it is sufficient to show True or False).

string_user = input("Enter the string ")
string_user_length = len(string_user.strip())

if string_user_length >= 3 and string_user_length < 10:
    print(True)
else:
    print(False)
