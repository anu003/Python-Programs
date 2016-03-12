BRACES = {"(":")","{":"}","[":"]"}
def group_check(s):
    stack = []
    for b in s:
        c = BRACES.get(b)
        if c:
            stack.append(c)
        elif not stack or stack.pop() != b:
            return False
    return not stack

##def isopen(s):
##    s_open = ["(","{","["]
##    if s in s_open: return True
##    
##def group_check(s):
##    s_open = {"(":")","{":"}","[":"]"}
##    s_close = {")":"(","}":"{","]":"["}
##    s_len = len(s)
##    s_dic = {"(":0,"{":0,"[":0, ")":0,"]":0,"}":0}
##    s_list = list(s)
##    i = 0
##    if s_len%2:
##        return False
##    if s[0] not in s_open:
##        return False
##    for e in s:
##        if e in s_open:
##            s_dic[e] += 1
##        if e in s_close:
##            s_dic[e] += 1
##    print s_dic
##    for e in s:
##        if e in s_open:
##            if s_dic[e] != s_dic[s_open[e]]:
##                return False
##    while i < s_len-1:
##        if not isopen(s_list[i]):
##            if s_list[i-1] != s_close[s_list[i]]:
##                return False
##            if s_len != i+1:
##                s_list = s_list[:i-1]+s_list[i+1:]
##                s_len = len(s_list)
##                i = i-2
##        i = i+1
##    return True   
##    
            
print group_check("}([]){}[]{")

##    for i in range(0, len(s)):
##        if s_open(s[i]) == s[i+1]:
##            s[i+2:]
##    return True


##        if e in s_open:
##            pos_open = s.find(e)
##            pos_close = s.find(s_open[e])
##            if pos_close == -1:
##                return False
##            f = pos_close-pos_open
##            if not f%2:
##                return False
##        if e in s_close:
##            pos_close = s.find(e)
##            pos_open = s.find(s_close[e])
##            if pos_open == -1:
##                return False
##            f = pos_close-pos_open
##            if not f%2 or f < 0:
##                return False
