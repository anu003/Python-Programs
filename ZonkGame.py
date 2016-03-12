from collections import Counter

def get_score(dice):
    
    score = 0
    
    # keeping track of number of times each number appeared
    count_values = Counter(dice).values()

    # scores if the number appeared 3 times
    threes_dict = {1:1000, 2:200, 3:300, 4:400, 5:500, 6:600}

    # scores of each number if appeared less than 3 times
    every = {1:100, 2:0, 3:0, 4:0, 5:50, 6:0}

    # Straight
    if sorted(dice) == range(1,7):
        score = 1000
        return score
    
    # six of a kind
    if 6 in count_values:
        score = 4 * threes_dict[dice[0]]
        return score

    # five of a kind
    if 5 in count_values:
        for key, count in Counter(dice).items():
            if count == 5:
                score = score + 3 * threes_dict[key]
            else:
                score = score + every[key]
        return score

    # four of a kind
    if 4 in count_values:
        for key, count in Counter(dice).items():
            if count == 4:
                score = score + 2 * threes_dict[key]            
            else:
                score = score + count*every[key]
        return score

    # threes
    if 3 in count_values:
        for key, count in Counter(dice).items():
            if count == 3:
                score = score + threes_dict[key]
            else:
                score = score + count*every[key]
        return score
    
    # three pairs of any dice:
    if 2 in count_values:
        if len(set(dice)) == 3 and len(set(count_values)) == 1:          
            score = 750
            return score

    # calculate scores
    for key in Counter(dice):
         score = score + Counter(dice)[key] * every[key]
    if not score:
         return "Zonk"
    return score
        

print get_score([1]) == 100
print get_score([2]) == "Zonk"
print get_score([3]) == "Zonk"
print get_score([4]) == "Zonk"
print get_score([5]) == 50
print get_score([6]) == "Zonk"
print get_score([1,1]) == 200
print get_score([1,1,1]) == 1000
print get_score([1,2,3,4,5,6]) == 1000
print get_score([2,2,3,3,6,6]) == 750
print get_score([3,2,6,4,4,6]) == "Zonk"
