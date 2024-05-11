# Types of errors - SyntaxErrors - These occur when there is a syntactical or grammatical error in the code that violates the grammar of the programming language
#

def get_int():
    while True:
        try:
            x = int(input("What's x? \n"))
            return x
        except ValueError as e:
            pass

def main():
    x = get_int()
    if x < 0:
        # This is for raising exceptions if there exists any
        raise Exception("Sorry, no numbers below 0")
    else:
        print(f"x is {x}")

main()
# the above code will generate nameError because when the ValueError occurs, it occurs on the right side
# of the assignment operation. So no value has been assigned to the variable x. Hence the name error.
# In this case, x has not been assigned any value

# Code under the try block will be executed once.
# If any error occurs, the code under except will be executed
# The code under finally will be executed irrespective of whether the code under try block was executed successfully or not
