def ghostbusters(building):
    #your code here
    list_building = building.split() 
    result = "" # intialising an empty string 
    ghost = ' ' # assigning white space to a variable ghost
    
    # if a white space is in building, it is removed
    if ghost in building: 
        for e in list_building:
            result = result + e    
    # if no white space
    else:
        result = "You just wanted my autograph didn't you?"
        
    return result
