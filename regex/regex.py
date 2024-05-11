import re
from sys import argv, exit

email = input("Enter your email address: ")
pattern = r"^\w+@(\w+\.)?\w+(.edu|.com|.in|.org)$"
# r"^.+@[a-z]+\.edu$" r represents raw string
# \w represents all alphanumeric characters including _
# \W not a word character
# \d decimal digit
# \D not a decimal digit
# \s whitespace character
# \S not a whitespace character
# (A | B) either A or B
# (...) a group
# (?:...) non-capturing version
# multiline, ignorecase, dotall - flags
match = re.search(f"{pattern}", email, re.IGNORECASE)

if match:
    print("VALID!")
else:
    print("INVALID!")

exit()
