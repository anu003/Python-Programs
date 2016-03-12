##def last_digit(a,b):
##    # find the last digit of a
##    # find the repitative pattern(last digit) of its power and store
##    # divide the power and extract the remainder and find the last digit from the list
##    if b == 0:
##        return 1
##    powers = {0:[0],1:[1],2:[2,4,8,6],3:[3,9,7,1],4:[4,6],5:[5],6:[6],7:[7,9,3,1],8:[8,4,2,6],9:[9,1]}
##    last_digi = int(str(a)[-1])
##    len_powers = len(powers[last_digi])
##    return powers[last_digi][(b % len_powers)-1]


def last_digit(n1,n2):
    return pow(n1, n2, 100)

print last_digit(107638291792048370329, 126879843437989)
