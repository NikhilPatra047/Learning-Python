from intro import square, hello
import pytest

# Three different tests
def test_positive():
    assert square(2) == 4

def test_float():
    assert square(5.5) == 30.25

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0

def test_str():
    with pytest.raises(TypeError):
        square("cat")

def test_default():
    assert hello("David Goggins") == "hello, David Goggins"

def test_arg():
    assert hello() == "hello, world"

def main():
    test_positive()
    test_negative()
    test_zero()
    test_float()
    test_default()
    test_arg()
    test_str()

if __name__ == "__main__":
    main()
