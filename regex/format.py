import re

name = input("enter your name: ").strip()
match = re.search(r"^(.+), *(.+)$", name)
if match:
    # last, first = match.groups()
    # groups() captures the capture groups specified within the parentheses
    last = match.group(1)
    first = match.group(2)
    name = f"{first} {last}"
    print(f"hello, {name}")

# Regular expressions can be used to search for patterns in a string
# These can be used to clean up data inputs
