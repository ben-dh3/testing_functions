from lib.greet import *

def test_greet():
    result = greet('Ben')
    assert result == "Hello, Ben!"