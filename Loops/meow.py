# i = 3
# while i != 0: 
#   print("meow")
#   i -= 1

# for _ in range(3):
#   print("meow")
  
# print(f"meow\n" * 3, end="")

# n = abs(int(input("enter a number: ")))
# print("meow\n" * n, end="")

def main():
  number = get_number() 
  meow(number)

def get_number():
  while True: 
    n = int(input("Enter a number: "))
    if n > 0: 
      return n 
    else: 
      continue 

def meow(n): 
  for _ in range(n):
    print("meow")

main()