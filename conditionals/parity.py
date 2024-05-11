def parity(x): 
  return True if x % 2 == 0 else False 

def main(): 
  x = int(input("enter x: "))
  result = parity(x)
  print(result)
  
main()