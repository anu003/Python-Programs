def is_palindrome(num):
    return bool(str(num) == str(num)[::-1])

def create_palindrome(num, chain_length):
    chain_length += 1
    num_str = str(num)
    rev_num_str = num_str[::-1]
    new_num = int(num_str) + int(rev_num_str)
    return palindrome_chain_length(new_num, chain_length)

def palindrome_chain_length(n, chain_length = 0):
    # parameter n is a positive integer
    # your function should return the number of steps
    pass
    if is_palindrome(n):
        return chain_length
    return create_palindrome(n, chain_length)

print palindrome_chain_length(87)
