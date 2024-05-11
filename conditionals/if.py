x = input("what's x? ")
y = input("what's y? ")

# and or = && ||

if x.isdigit() and y.isdigit():
  x = int(x)
  y = int(y)
  
  if x != y: 
    print(f"{x} is not equal to {y}")
  else: 
    print(f"{x} is equal to {y}")
  # if x < y:
  #   print(f"{x} is less than {y}")
  # elif x > y:
  #   print(f"{x} is greater than {y}")
  # else: 
  #   print(f"{x} is equal to {y}")
else:
  print("Please input numbers")