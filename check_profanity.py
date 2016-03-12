import urllib

def read_text():

    quotes = open("/Users/KittusMac/Documents/movie_quotes.txt")
    contents_of_file = quotes.read()
    #print contents_of_file
    quotes.close()
    check_text(contents_of_file)

def check_text(text_to_check):

    connection = urllib.urlopen("http://www.wdyl.com/profanity?q="+text_to_check)
    output = connection.read()
    if "true" in output:
        print "Profanity Alert!!!"
    elif "false" in output:
        print "This document has no curse words!!"
    else:
        print "Document was not scanned properly"
    connection.close()
    
read_text()
 
