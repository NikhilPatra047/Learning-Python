numbers = [1, 2, 3, 4, 5]

def sort_inc(num):
    return num <= 3

numbers = sorted(numbers, key=sort_inc, reverse=False)
print(numbers)

# 12345
