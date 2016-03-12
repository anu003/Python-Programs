##def find_missing(sequence):
##    d = sequence[1] - sequence[0]
##    i = 1
##    while i < len(sequence):
##        if sequence[i]-sequence[i-1] == d:
##            i += 1
##            continue
##        else:    
##            return sequence[i] - d

def find_missing(sequence):
    d = sequence[1] - sequence[0] 
    return [sequence[i]+d for i in range(0, len(sequence)-1) if sequence[i+1]-sequence[i] != d]

print find_missing([1, 2, 3, 4, 6, 7, 8, 9])
