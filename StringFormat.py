import re
##def validPhoneNumber(phoneNumber):
##    pass
##    #valid phonenumber format is defined as a regular expression
##    r = re.compile('\(\d{3}\)\s\d{3}-\d{4}')
##    #checking the length of the number
##    if len(phoneNumber) == 14:
##    #if format matches returns True otherwise False
##      if r.match(phoneNumber):
##         return True
##    return False

def validPhoneNumber(phoneNumber):
    pass
    return bool (len(phoneNumber) == 14 and (re.compile('\(\d{3}\)\s\d{3}-\d{4}')).match(phoneNumber))
    

print validPhoneNumber("(123) 456-7890")
