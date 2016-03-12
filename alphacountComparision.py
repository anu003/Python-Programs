##from string import ascii_lowercase
##    
##def mix(s1, s2):
##    small_alpha = ascii_lowercase
##    s1_count = {}
##    s2_count = {}
##    res = []
##    result = ""
##    for c in small_alpha:
##        if c in s1 and c in s2:           
##            s1_count[c], s2_count[c] = s1.count(c), s2.count(c)
##        elif c in s1 and c not in s2:
##            s1_count[c], s2_count[c] = s1.count(c), 0
##        elif c in s2 and c not in s1:
##            s1_count[c], s2_count[c] = 0, s2.count(c)
##   
##    for key in s1_count:
##        if s1_count[key] > s2_count[key] and s1_count[key] > 1:
##            res.append((s1_count[key], 1, key))
##        elif s1_count[key] < s2_count[key] and s2_count[key] > 1:
##            res.append((s2_count[key], 2, key))
##        elif s1_count[key] == s2_count[key] and s1_count[key] > 1:
##            res.append((s1_count[key], 3, key))
##
##    res = sorted(res, key= lambda tup: (tup[0], -tup[1], -ord(tup[2])), reverse = True)
##
##    for wc, strng, letter in res:
##        if strng == 3:
##            strng = "="
##        result = result + str(strng) + ":" +  str (wc * letter) + "/"
##    return result[:-1]

##print mix("Are they here", "yes, they are here")
##    
##    
##print mix("looping is fun but dangerous", "less dangerous than coding")
# "1:ooo/1:uuu/2:sss/=:nnn/1:ii/2:aa/2:dd/2:ee/=:gg")

print mix(" In many languages", " there's a pair of functions")
#"1:aaa/1:nnn/1:gg/2:ee/2:ff/2:ii/2:oo/2:rr/2:ss/2:tt")


mix = lambda s1, s2, g = ('=:','1:','2:'): '/'.join(
sorted([g[cmp(c1,c2)] + s*max(c1,c2)
            for s, c1, c2 in 
                ((s, s1.count(s), s2.count(s)) 
                    for s in set(s1 + s2) 
                    if s.islower())
            if max(c1,c2)>1], 
        key=lambda g: (-len(g), g))
)
