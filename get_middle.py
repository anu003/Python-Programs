def get_middle(s):
    #your code here
    #length of the string s
    s_len = len(s)
    s_list = list(s)
    if s_len%2 == 0:
        result = s_list[(s_len/2) - 1] + s_list[s_len/2]
        return result
    else:
        result = s_list[(s_len-1)/2]
        return result

