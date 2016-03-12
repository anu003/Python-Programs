from math import factorial
import string

def dec2FactString(nb):
  #your code here

    # generates a dictionary with alphabets enumerated starting from 10 eg: {10:"A", 11:"B"...35:"Z"}
    alphadic = dict([(a, b) for a,b in enumerate(list(string.ascii_uppercase), 10)])

    # returns quotient and remainder
    q, r = divmod(nb,1)

    # intializing the result list with the obtained remainder
    resultlist = [r]
    i = 2

    # store the remainders obtained from each division into the result list, by dividing the quotient
    while i != 0:        
        q, r = divmod(nb,i)
        nb = q
        if r < 10:
            resultlist.append(r)
        else:
            resultlist.append(alphadic[r])
            
        if q != 0:
            i += 1
        else:
            i = 0

    # reverses the resultlist
    resultlist.reverse()

    #returns the string output
    return "".join(map(str,resultlist))
        
    
    
def factString2Dec(stringip):
  #your code here
    result = 0

    # generates a dictionary with alphabets enumerated starting from 10 in reverse order eg: {"A":10, "B":11..."Z":35}
    alphadic = dict([(b,a) for a,b in enumerate(list(string.ascii_uppercase), 10)])

    # reversing the input string
    stringip = stringip[::-1]

    # obtaining the decimal value by adding the factorial(base i) multiplied by the corresponding number
    for i in range(0, len(stringip)):
        if stringip[i].isalpha():
            result = result + factorial(i) * alphadic[stringip[i]]
        else:
            result = result + factorial(i) * int(stringip[i])
    return result
            
print factString2Dec("341010")
print dec2FactString(463)
