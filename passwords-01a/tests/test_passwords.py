"""
You can auto-discover and run all tests with this command:

   python -m pytest 

Documentation: https://docs.pytest.org/en/latest/
"""

__author__ = "cmeinco"
__version__ = "0.1.0"
__license__ = "MIT"

from logzero import logger
import pytest

import user 
# user is able to login

def test_positive_login():
    bob = user.User()
    tempPwd = "abc1234"
    bob.changePassword(tempPwd)
    assert bob.login(tempPwd)
    assert not bob.login("xxxx")

# user is able to change password
def test_positive_changepwd():
    bob = user.User()
    bob.changePassword("abc123")

def test_negative_samepwd_not_allowed():
    bob = user.User()
    bob.changePassword("abc123")
    with pytest.raises(user.PasswordMatchException):
        bob.changePassword("abc123")

def test_negative_historical_samepwd_not_allowed():
    bob = user.User()
    bob.changePassword("abc123")
    bob.changePassword("abc1234")
    with pytest.raises(user.HistoricalPasswordMatchException):
        bob.changePassword("abc123") #fails here

def test_security_historicalmax_positive():
    maxHistorical = user.MAX_HISTORICAL_PWDS
    bob = user.User()
    bob.changePassword("abc123")
    for n in range(maxHistorical-1):
        bob.changePassword(n) 
    bob.changePassword("abc123") # first should fall off
    assert True

def test_security_historicalmax_samepwd_not_allowed():
    maxHistorical = user.MAX_HISTORICAL_PWDS
    bob = user.User()
    bob.changePassword("abc123")
    for n in range(maxHistorical-2):
        bob.changePassword(n) 
    with pytest.raises(user.HistoricalPasswordMatchException):
        bob.changePassword("abc123") # first should not have fallen off yet

def test_security_storage_protection():
    bob = user.User()
    tempPwd = "abc1"
    bob.changePassword(tempPwd)
    assert tempPwd != bob.getCurrentPassword()

#historical passwords being stored in the clear. How to test for this problem?
@pytest.mark.skip(reason="current not built out")
def test_security_storage_protection_historical():
    pass

