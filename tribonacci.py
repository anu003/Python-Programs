##def tribonacci(signature,n):
##    #your code here
##    # base cases n = 0,1,2
##    result = []
##    if n <= 3:
##        result = signature[0:n]
##        return result
##    # for n > 3, To find tribonacci series for a sequence of n
##    else:    
##        while len(result) < n:
##            # Adding the latest 3 entries of the series to find a new entry of the series
##            g = lambda x,y,z:x+y+z
##            # Adding the new entry to the result set
##            result = result + [g(*(signature))]
##            # Assigning the latest 3 entries of the series to the signature
##            signature = result[-3:]
##    return result
##
##print tribonacci([1,1,1], 3)

##def tribonacci(signature,n):
##    #your code here
##    # base cases n = 0,1,2
##    result = []
##    if n == 0:
##        result = []
##    if n == 1:
##        result = [signature[0]]
##    if n == 2:
##        result = [signature[0],signature[1]]
##    if n == 3:
##        result = signature
##    # for n > 3, To find tribonacci series for a sequence of n
##    else:    
##        while len(result) < n:
##            # Adding the latest 3 entries of the series to find a new entry of the series
##            g = lambda x,y,z:x+y+z
##            # Adding the new entry to the result set
##            result = result + [g(*signature)]
##            # Assigning the latest 3 entries of the series to the signature
##            signature = result[-3:]
##    return result


def tribonacci(signature,n):
    #your code here
    #tribonacci series result set
    result = signature
    
    #To find tribonacci series for a sequence of n
    while len(result) < n:
        # Adding the latest 3 entries of the series to find a new entry of the series
        g = lambda x,y,z:x+y+z
        # Adding the new entry to the result set
        result = result + [g(*(signature))]
        # Assigning the latest 3 entries of the series to the signature
        signature = result[-3:]
    return result
