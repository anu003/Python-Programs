import binascii
##
##def to_hex(data):
##    #binascii.a2b_uu(string
##  
##    
##
## #   binascii.b2a_hex(data)
##    return binascii.hexlify(data)
##
##    ##binascii.a2b_hex(hexstr)
##    ##
##def to_ascii(data):
##    return binascii.unhexlify(data)
##
##


def to_ascii(h):
    result = []
    for i in range(0, len(h), 2):
        result.append(chr(int(h[i:i + 2], 16)))
        #return ''.join(chr())
    return result 
             
#@staticmethod
def to_hex(s):
    result = []
    for char in s:
        result.append(hex(ord(char)))
        print hex(ord(char))[2:]
##    return ''.join(hex(ord(char))[2:] )
    return result

data = "Look mom, no hands"
print to_hex(data)

##data = ("4c6f6f6b206d6f6d2c206e6f2068616e6473")
##print to_ascii(data)
