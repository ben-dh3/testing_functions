# import function to test
from lib.add_five import *

def test_add_five_returns_eight_for_three():
    result = add_five(3)
    # should return 8
    assert result == 8