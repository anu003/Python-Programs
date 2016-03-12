import turtle

def draw_square(some_turtle):

    for i in range(1,5):
         some_turtle.forward(200)
         some_turtle.right(90)
 
    
def drawshape():
 
     window = turtle.Screen()
     window.bgcolor("black")

     # for square
     brad = turtle.Turtle()
     brad.color("red")
     brad.shape("square")
     brad.pencolor("yellow")
     brad.speed(5)
     for i in range(1,37):
         draw_square(brad)
         brad.right(10)
            
     # For circle        
##     angie = turtle.Turtle()
##     angie.shape("circle")
##     angie.color("pink")
##     angie.speed(6)
##     angie.circle(100)
##     
     # for triangle
##     sides = 0
##     shape_sides = 3
##     trello = turtle.Turtle()
##     trello.shape("triangle")
##     trello.color("brown")
##     trello.pencolor("blue")
##     trello.speed(10)
##     while sides < shape_sides:
##         trello.forward(100)
##         trello.left(120)
##         sides = sides + 1
     window.exitonclick()

drawshape()
