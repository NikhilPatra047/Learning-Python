name = input("What's your name? ")
# print("hello, " + name)
# When passing multiple arguments to a print, a space is automatically added
# print("hello,", name)
# name = name.strip()
# name = name.capitalize() 
# name = name.title() #Does a title based capitalisation. Turns the first letter of every string separated by space into Capital letter

# Chaining functions
name = name.strip().title()
print(f"hello, {name}")