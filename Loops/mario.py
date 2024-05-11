def main(): 
  print_column(3)
  print_row(4)
  print_grid(3, 4)
  
def print_grid(row, col): 
  for _ in range(col): 
    for _ in range(row): 
      print("# ", end="")
    print()

def print_row(width): 
  print("? " * width)
  
def print_column(height): 
  print("#\n" * height, end="")
  
main()