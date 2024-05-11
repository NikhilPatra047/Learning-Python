# def hello(name="world"): 
#   return "hello, " + name 

def square(value=1): 
  # return value ** 2
  return pow(value, 2)

def main(): 
  # name = input("What's your name? ")
  # result = None 
  # if name == "":
  #   result = hello()
  # else: 
  #   result = hello(name.title())
  # print(result)
  
  x = input("enter a number: ")
  result = None 
  if x == "":
    result = square()
  else: 
    result = square(int(x))
  print(result)

main()