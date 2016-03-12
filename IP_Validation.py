import re
def is_valid_IP(strng):
   
   # return bool(re.match("(\d)|(\d(\d))|1(\d\d)|2([0-5][0-5])\.(\d)|(\d(\d))|1(\d\d)|2([0-5][0-5])\.(\d)|(\d(\d))|1(\d\d)|2([0-5][0-5])\.(\d)|(\d(\d))|1(\d\d)|2([0-5][0-5]))", strng))
    return bool(re.match("^([0-9]|[1-9][0-9]|1([0-9][0-9])|2(5([0-5]))|2([0-4][0-9]))\.([0-9]|[1-9][0-9]|1([0-9][0-9])|2(5([0-5]))|2([0-4][0-9]))\.([0-9]|[1-9][0-9]|1([0-9][0-9])|2(5([0-5]))|2([0-4][0-9]))\.([0-9]|[1-9][0-9]|1([0-9][0-9])|2(5([0-5]))|2([0-4][0-9]))\Z",strng))
print is_valid_IP('236.34.58.181')

##
##import socket
##
##def is_valid_IP(addr):
##    try:
##        socket.inet_pton(socket.AF_INET, addr)
##        return True
##    except socket.error:
##        return False
