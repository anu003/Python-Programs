##def title_case(title, minor_words=''):
##    # convert everything to lower case and converting string to a list
##    minor_words_list = (minor_words.lower()).split()
##    title_list = (title.lower()).split()
##    result = []
##    
##    for i in range(0,len(title_list)):
##        if title_list[i] in minor_words_list:
##            if i == 0:
##                 result.append(title_list[i][0].upper()+title_list[i][1:])
##            else:
##                 result.append(title_list[i])
##        else:
##            result.append(title_list[i][0].upper()+title_list[i][1:])
##    return " ".join(result)

def title_case(title, minor_words=''):
    title = title.capitalize().split()
    print title
    minor_words = minor_words.lower().split()
    return ' '.join([word if word in minor_words else word.capitalize() for word in title])

    

print title_case('THE WIND IN THE WILLOWS', 'The In')
