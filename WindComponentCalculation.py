import math

def wind_info(runway, wind_direction, wind_speed):
    
    runway = runway[0]+runway[1]
    runway_degrees = int(runway)*10

    #converting degrees to radians
    angle = math.radians(runway_degrees - wind_direction)

    #calculating crosswind and headwind/tailwind components
    crosswind = int(round((wind_speed * math.sin(angle))))
    headwind = int(round(wind_speed * math.cos(angle)))

    if crosswind >=0:
        cw_direction = "left."
    else:
        cw_direction = "right." 
        
    if headwind >=0:
        return "Headwind {0} knots. Crosswind {1} knots from your ".format(headwind,abs(crosswind))+cw_direction
    else:
        return "Tailwind {0} knots. Crosswind {1} knots from your ".format(abs(headwind),crosswind)+cw_direction

print wind_info("18", 170, 15)
print wind_info("18", 210, 14)
print wind_info("22L", 160, 14)
print wind_info("18", 70, 15)

##("18", 170, 15),"Headwind 15 knots. Crosswind 3 knots from your left."),
##(("18", 210, 14),"Headwind 12 knots. Crosswind 7 knots from your right."),
##(("22L", 160, 14),"Headwind 7 knots. Crosswind 12 knots from your left."),
##(("18", 70, 15),"Tailwind 5 knots. Crosswind 14 knots from your left." )
##]

##A positive headwind value indicates the wind coming from ahead (headwind) and a negative value implies a tailwind.
##A positive crosswind value implies crosswind from the right and a negative value indicates a crosswind from the left.
