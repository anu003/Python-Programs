def divisors(integer):
    pass
    result = []
    for i in range(2,integer):
        quotient, remainder = divmod(integer,i)
        if remainder == 0:
            result.append(quotient)
    if result != []:
        return sorted(result)
    else:
        return str(integer) + " is prime"

print divisors(15)
