import  turtle
my_turtle=turtle.Turtle()

def my_function(length,angle):
 for i in range(9):
    my_turtle.forward(length)
    my_turtle.left(angle)
    my_turtle.left(angle)
    my_turtle.forward(length)


for i in range(50):
    my_function(100,30)
    my_turtle.right(10)