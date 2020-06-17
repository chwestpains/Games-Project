from turtle import *
from dijkstra_alg import *
from countys import *




screen = Screen()
screen.title("Pizza Delivery")
turtle = Turtle()
turtle.speed(10)
screen.colormode(255)
turtle.penup()
turtle.pensize(2)

style = ("Arial", 20, "bold")

for x in connected_nodes:
    colour = random.randint(0,255),random.randint(0,255),random.randint(0,255)
    for item in townList:
        if x == item.get_name():
            currentTown = item
            penup()
            turtle.goto(item.get_coords())
            turtle.dot(20, colour)
            turtle.forward(-5)
            turtle.write(item.get_name(), font=style, align='center')
            turtle.forward(5)
            
    c_town = connected_nodes[x]
    for y in c_town:
        penup()

        for item in townList:
            if y == item.get_name():
                turtle.pendown()
                turtle.pencolor("black")

                turtle.setposition(item.get_coords())
                turtle.penup()
                turtle.setposition(currentTown.get_coords())

    
                


source = screen.textinput("Start", "Starting Point:")
destination = screen.textinput("Destination","Destination:")

turtle.clear()
turtle.goto(0,100)
style = ("Arial", 10, "bold")
turtle.write(dijkstra(connected_nodes, source, destination), font=style, align='center')

    
    
        
                





        
                
        



                        



