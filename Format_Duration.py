
def format_duration(seconds):
    #your code here
    hours = 0
    days = 0
    years = 0
    result = ""
    minutes, seconds = divmod(seconds, 60)
    
    if minutes >= 60:
        hours, minutes = divmod(minutes, 60)
        if hours >= 24 :
            days, hours = divmod(hours, 24)
            if days >= 365:
                years, days = divmod(days, 365)

    if years != 0:
       if years == 1:
           result = str(years) + " year,;"
       else:
           result = str(years) + " years,;"

    if days != 0:
        if days == 1:
            result = result + str(days) + " Day,;"
        else:
            result = result + str(days) + " Days,;"

    if hours != 0:
        if hours == 1:
            result = result + str(hours) + " Hour,;"
        else:
            result = result + str(hours) + " Hours,;"

    if minutes != 0:
        if minutes == 1:
            result = result + str(minutes) + " Minute,;"
        else:
            result = result + str(minutes) + " Minutes,;"

    if seconds != 0:
        if seconds == 1:
            result = result + str(seconds) + " Second"
        else:
            result = result + str(seconds) + " Seconds"
            
    result = result.split(";")

    if "" in result: del result[result.index('')]
    if len(result) > 1:
        if result[-1][-1] == ",":
            result[-1] = "and " + result[-1][:-1]
        else:
            result[-1] = "and " + result[-1][:]
        result[-2] = result[-2][:-1]
        
    elif len(result) == 1 and result[-1][-1] == ",":
        result[-1] = result[-1][:-1]
        
    return " ".join(result)

print format_duration(120)

##times = [("year", 365 * 24 * 60 * 60), 
##         ("day", 24 * 60 * 60),
##         ("hour", 60 * 60),
##         ("minute", 60),
##         ("second", 1)]

##def format_duration(seconds):
##
##    if not seconds:
##        return "now"
##
##    chunks = []
##    for name, secs in times:
##        qty = seconds // secs
##        if qty:
##            if qty > 1:
##	  name += "s"
##            chunks.append(str(qty) + " " + name)
##
##        seconds = seconds % secs
##
##    return ', '.join(chunks[:-1]) + ' and ' + chunks[-1] if len(chunks) > 1 else chunks[0]

##   for i in range(0, len(result)):
##        if result[i][0] == '0':
##            del result[i]
##        elif result[i][0] == '1':
##            result[i] = result[i][:-1]
##    return result


        
