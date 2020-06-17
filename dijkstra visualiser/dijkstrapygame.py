##To Do:
#create pixel art for background
#enable user to input start and end destinations (complete 17/06/20)
#toggle between visuals and graph visualiser

from tkinter import *
import random
import time

from dijkstra_alg import *
from countys import *

timeleft = 0


def create_route():
    global buttonPress, timeleft
    start = source.get()
    end = destination.get()
    timeleft = dijkstra(connected_nodes, start, end)
    times()
    canvasEntry.pack_forget()
    return timeleft



window = Tk()

window.title('Pizza Delivery')

canvas = Canvas(window, width=800, height=400, bg="black")
canvas.pack()

canvasEntry = Canvas(window, width = 800, height=200)
canvasEntry.pack()


    
title = canvas.create_text(400, 200, text="Pizza Delivery", fill="white", font=("Helvetica", 30))



lbl_source = Label(window, text="Start: ")
canvasEntry.create_window(320, 140, window=lbl_source)


lbl_dest = Label(window, text="End: ")
canvasEntry.create_window(320, 100, window=lbl_dest)
destination = Entry(window)
canvasEntry.create_window(400, 100, window=destination)
source = Entry(window)
canvasEntry.create_window(400, 140, window=source)


route = Button(text="create route", command=create_route)
canvasEntry.create_window(400, 180, window=route)








pizzatemp = 100



pizzatempDisplay = Label(window, text="Pizza Temperature: " + str(pizzatemp))
pizzatempDisplay.pack()

timeleftDisplay = Label(window, text="Time to Destination: " + str(timeleft))
timeleftDisplay.pack()
    
background = PhotoImage(file="ownbackground.png")

pizzaman = PhotoImage(file="pizzaman3.png")



bg = canvas.create_image(400, 200, image=background)
mychar = canvas.create_image(400, 210, image=pizzaman)


def end_title():
    global mychar, bg
    canvas.delete(title)
    

def moveUp():
    global mychar
    canvas.move(mychar, 0, 50)

def moveDown():
    global mychar
    canvas.move(mychar, 0, -50)
    
def driving():
    global mychar, canvas
    

    window.after(100, moveUp)
    print(" ")

    window.after(100, moveDown)
    window.after(150, driving)
    
    
    
def timeToDest():
    global timeleft
    
    timeleft = int(timeleft)
    timeleft -= 1
    timeleftDisplay.config(text="Time: " + str(timeleft))
    #update based on time left in minutes (in seconds for testing purposes)
    window.after(5000, timeToDest)
    

def cooling():
    global pizzatemp
    pizzatemp -= 1
    pizzatempDisplay.config(text="Pizza Temperature: " + str(pizzatemp))
    #update rate will be based on algorithm
    window.after(5000,cooling)

    

    


window.after(1000, end_title)


def times():
    
    window.after(1000, driving)
    window.after(5000, cooling)
    window.after(5000, timeToDest)


window.mainloop()
