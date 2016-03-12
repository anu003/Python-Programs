import turtle

def initials():

    window = turtle.Screen()
    window.bgcolor("white")
    mypen = turtle.Turtle()
    mypen.speed(15)
    mypen.pencolor("orange")
    mypen.shape("turtle")
    mypen.setpos(0,100)
    mypen.setpos(35,100)
    mypen.setpos(35,50)
    mypen.setpos(0,50)
    mypen.setpos(35,50)
    mypen.setpos(35,0)
    mypen.pencolor("white")
    mypen.setpos(55,0)
    mypen.pencolor("orange")
    mypen.setpos(55,100)
    mypen.setpos(55,50)
    mypen.left(120)
    mypen.setpos(85,0)
    mypen.setpos(55,50)
    mypen.right(60)
    mypen.setpos(85,100)

    window.exitonclick()

def draw_rhombus(turtle_pen):
    for i in range(0,2):
        turtle_pen.forward(100)
        turtle_pen.right(160)
        turtle_pen.forward(100)
        turtle_pen.right(20)
                                        
def flower():

    window = turtle.Screen()
    window.bgcolor("black")
    mypen = turtle.Turtle()
    mypen.pencolor("yellow")
    mypen.speed(30)
    for i in range(0,72):
        draw_rhombus(mypen)
        mypen.right(5)
    mypen.penup()
    mypen.setpos((0,0))
    mypen.pendown()
    mypen.setpos((0,-200))
    window.exitonclick()

def draw_triangle(turtle_pen):
    turtle_pen.down()
    turtle_pen.begin_fill()
    for i in range(0,3):
        turtle_pen.backward(20)
        turtle_pen.right(120)       
    turtle_pen.end_fill()
    
def tri_pattern(turtle_pen, posx, posy):
    for i in range(0,2):
        turtle_pen.begin_fill()
        draw_triangle(turtle_pen)
        posx = posx + 20
        turtle_pen.setpos((posx,posy))
        print posx
        draw_triangle(turtle_pen)
        turtle_pen.penup()
        turtle_pen.left(120)
        turtle_pen.forward(20)
        turtle_pen.right(120)
        draw_triangle(turtle_pen)
        turtle_pen.penup()
        posx = posx + 2ß0
        turtle_pen.setpos((posx, posy))
    posx = 20
    posy = 36.5
    turtle_pen.setpos((posx, posy))
        
def triangle_pattern():
    window = turtle.Screen()
    window.bgcolor("white")
    mypen = turtle.Turtle()
    mypen.color("green")
    mypen.pencolor("blue")
    mypen.speed(30)
    posx = 0
    posy = 0
    #for i in range(0,2):
    tri_pattern(mypen, posx, posy)
##        posx = posx + 40
##        mypen.setpos((posx, posy))
##    mypen.penup()
##    posx = 20
##    posy = 36.5
##    mypen.setpos((posx, posy))
 #   tri_pattern(mypen, posx,posy)

    posx = 80
    posy = 
    
#tri_pattern()
triangle_pattern()   
#flower()
#initials()
 
    
