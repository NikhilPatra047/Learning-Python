from intro import take_user_input

def test_input():
    user_input = take_user_input()
    assert type(user_input) == int

def main():
    test_input()

if __name__ == "__main__":
    main()
