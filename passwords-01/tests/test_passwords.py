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

# user is able to change password
def test_positive():
    bob = user.User()
    bob.changePassword("abc123")

@pytest.mark.xfail(raises=Exception)
def test_samepwd_not_allowed():
    bob = user.User()
    bob.changePassword("abc123")
    bob.changePassword("abc123")
    
@pytest.mark.xfail(raises=Exception)
def test_historical_samepwd_not_allowed():
    bob = user.User()
    bob.changePassword("abc123")
    bob.changePassword("abc1234")
    bob.changePassword("abc123") #fails here
    assert 0 #should never touch this.

def test_historical12_pwdstored():
    maxHistorical = user.savePrevious
    bob = user.User()
    bob.changePassword("abc123")
    for n in range(maxHistorical-1):
        bob.changePassword(n) 
    bob.changePassword("abc123") # first should fall off

@pytest.mark.xfail(raises=Exception)
def test_historical12_samepwd_not_allowed():
    maxHistorical = user.savePrevious
    bob = user.User()
    bob.changePassword("abc123")
    for n in range(maxHistorical-2):
        bob.changePassword(n) 
    bob.changePassword("abc123") # first should fall off
    assert 0

@pytest.mark.skip(reason="current not built out")
def test_security_storage_protection():
    bob = user.User()
    tempPwd = "abc1"
    bob.changePassword(tempPwd)
    assert tempPwd != bob.getCurrentPassword()

