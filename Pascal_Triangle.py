def pascal(p):
    #your code here
    prev_value = 0
    s = 0
    result = []
    if p == 1:
        return [[1]]
    if p == 2:
        return [[1],[1, 1]]
    if p > 2:
        result += pascal(2) 
        for i in range(3,p+1):
            res = []
            temp = pascal(i-1)[-1] + [0]
            for e in temp:
               s = e + prev_value
               res.append(s)
               prev_value = e
            result += [res]
    return result
        
print pascal(5)

##
##def pascal(p):
##
##    t = [[1]]
##
##    for _ in range(2, p + 1):
##        t.append([1] + [a + b for a, b in zip(t[-1][:-1], t[-1][1:])] + [1])
##
##    return t
##
##
##def pascal(p):
##    triangle = [[1]]
##    for _ in range(p - 1):
##        to_sum = zip([0] + triangle[-1], triangle[-1] + [0])
##        triangle.append(map(sum, to_sum))
##    return triangle
##
##from operator import add
##def pascal(p):
##    tr = [[1]]
##    for i in range(p-1):
##        tr.append(map(add, [0]+tr[i], tr[i]+[0]))
##    return tr

##next_step = lambda arr: [1]+[arr[i]+arr[i+1] for i in range(len(arr)-1)]+[1]
##def pascal(p):
##    cur=[1]
##    res=[]
##    for i in range(p):
##        res.append(cur)
##        cur = next_step(cur)
##    return res
