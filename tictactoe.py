import itertools

def isEqual(line):   
        if len(set(line)) == 1:            
           return line[0]
        else:
           return 0
            
def isSolved(board):
    l = len(board)
    check_list = board
    check_list = check_list + map(list,zip(*board))
    check_list.append([board[i][i] for i in range(l)])
    check_list.append([board[l-1-i][i] for i in range(l-1,-1,-1)])
    for line in check_list: 
        if isEqual(line):
            return isEqual(line)
    return -1 if 0 in list(itertools.chain(*check_list)) else 0           

print isSolved([[1,2,1],[2,1,1],[2,1,2]])
