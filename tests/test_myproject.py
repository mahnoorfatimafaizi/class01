from class01 import main 

def test_function1():
    r = main.my_first_function()
    assert r == "Hello, world!"

def test_function2():
    r = main.my_first_function()
    assert r != "Pakistan Zindabad"