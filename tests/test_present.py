from lib.present import *
import pytest

def test_present():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    error_message = str(e.value)
    assert error_message == "No contents have been wrapped."
    
    present.wrap("scarf")
    with pytest.raises(Exception) as e:
        present.wrap("scarf")
    error_message = str(e.value)
    assert error_message == "A contents has already been wrapped."