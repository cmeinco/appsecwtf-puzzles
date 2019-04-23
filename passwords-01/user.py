"""
Module Docstring
"""

__author__ = "cmeinco"
__version__ = "0.1.0"
__license__ = "MIT"

from logzero import logger

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
        self.curPwd = newPassword
        historicalPasswords.append(newPassword)
        if len(historicalPasswords) >= MAX_HISTORICAL_PWDS:
            historicalPasswords.remove(historicalPasswords[0])

        logger.debug("Password changed to {} ".format(newPassword))

def main():
    pass
     
if __name__ == "__main__":
    main()

