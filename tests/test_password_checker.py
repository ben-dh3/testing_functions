from lib.password_checker import *
import pytest

def test_password_checker():
    password_checker = PasswordChecker()
    result = password_checker.check('12345678')
    result == True
    
    with pytest.raises(Exception) as e:
        password_checker.check('1234')
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters."
    