from lib.gratitudes import *

def test_gratitudes():
    gratitudes = Gratitudes()
    gratitudes.add("food")
    result = gratitudes.format()
    assert result == "Be grateful for: food"