def count(ipstr):
    count_letters = {}
    letters = tuple(ipstr)
    for e in letters:
        if e not in count_letters:
            count_letters[e] = 1
        else:
            count_letters[e] = count_letters[e] + 1
    return count_letters

print count("Hello")
