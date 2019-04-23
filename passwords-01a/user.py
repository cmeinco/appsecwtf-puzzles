"""
Module Docstring
"""

__author__ = "cmeinco"
__version__ = "0.1.0"
__license__ = "MIT"

from logzero import logger
import hashlib, binascii, os

MAX_HISTORICAL_PWDS = 5

class PasswordMatchException(Exception):
    pass
class HistoricalPasswordMatchException(Exception):
    pass

class User(object):

    def __init__(self): 
        self.curPwd = ""            # Instance Variable 
        self.pwdHistory = list() 

    #think of this like the call to the database to retrieve the password or whatever is in the db.
    def getCurrentPassword(self):
        return self.curPwd

    #think of this like the call to the database to retrieve the password or whatever is in the db.
    def getPasswordHistory(self):
        return self.pwdHistory

    def changePassword(self,newPassword):
        logger.debug("CurrentPassword: {}, NewPassword: {}".format(self.getCurrentPassword(),newPassword))
        # check against cur pwd
        #if self._verify_password(newPassword,self.getCurrentPassword()):
        if newPassword == self.getCurrentPassword():
            logger.fatal("Passwords match, heading back.")
            raise PasswordMatchException("Matches Current Go Home")
        # check against historical pwds 
        historicalPasswords = self.getPasswordHistory() 
        if newPassword in historicalPasswords:
            logger.fatal("Password is in historical list, try again. {}".format(historicalPasswords)) 
            raise HistoricalPasswordMatchException("Found in historical list")
        logger.debug("Current Historical List: {}".format(historicalPasswords))

        # got here, so lets update the pwd and add it to the history
        
        #stop storing pwds in clear
        self.curPwd = self._hash_password(str(newPassword))

        #historical pwds being stored in clear, need to check/prevent this
        historicalPasswords.append(newPassword)
        if len(historicalPasswords) >= MAX_HISTORICAL_PWDS:
            historicalPasswords.remove(historicalPasswords[0])
        logger.info("History: {}".format(len(historicalPasswords)))
    
        logger.debug("Password changed to {} hashed as {}".format(newPassword,self.curPwd))

    def login(self,password):
        logger.debug("Logging in User with password: {}".format(password))
        if self._verify_password(self.getCurrentPassword(),password):
            return True
        else:
            return False

    #from https://www.vitoshacademy.com/hashing-passwords-in-python/

    def _hash_password(self,password):
        """Hash a password for storing."""
        salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
        pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), 
                                    salt, 100000)
        pwdhash = binascii.hexlify(pwdhash)
        return (salt + pwdhash).decode('ascii')

    def _verify_password(self,stored_password, provided_password):
        """Verify a stored password against one provided by user"""
        salt = stored_password[:64]
        stored_password = stored_password[64:]
        pwdhash = hashlib.pbkdf2_hmac('sha512', 
                                    provided_password.encode('utf-8'), 
                                    salt.encode('ascii'), 
                                    100000)
        pwdhash = binascii.hexlify(pwdhash).decode('ascii')
        return pwdhash == stored_password

def main():
    pass
     
if __name__ == "__main__":
    main()

