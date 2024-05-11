list = [1, 2, 3, 4, 5] 
def greater_than_2(ele):
  return ele < 2
new_list = sorted(list, key=greater_than_2, reverse=False)

print(new_list)