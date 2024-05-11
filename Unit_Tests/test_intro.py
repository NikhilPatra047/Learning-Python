from intro import square

# this is a convention
def test_square():
    # if square(2) != 4:
    #     print("2 squared was not 4")
    # if square(3) != 9:
    #     print("3 squared was not 9")

    # print("square function works as expected")
    # assert is a built-in construct that allows us to test assumption of our code.
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(0) == 0

def main():
    test_square()

if __name__ == "__main__":
    main()
