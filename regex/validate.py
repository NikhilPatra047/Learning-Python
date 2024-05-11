# regular expressions are used to validate patterns
email_add = input("Please enter your email address: ").strip()
# Just to remove the spaces around the string
#
# if "@" in email_add and "." in email_add:
#     print("Valid")
# else:
#     print("Invalid")

# exit()

try:
    username, domain = email_add.split("@")
except ValueError:
    raise ValueError("The E-mail address is missing @")
else:
    if username and "." in domain:
        print("valid")
    else:
        print("Invalid")

exit()
