import turtle
m = input("What would you like to do: print draw")
if m == print:
    a = input("What would you like to print?")
    print(a)
elif m == "draw":
    a = input("What would you like to draw: circle")
    if a == "circle":
        myTurtle = turtle.Turtle()
        myTurtle.circle(50)
        turtle.getscreen()._root.mainloop()
