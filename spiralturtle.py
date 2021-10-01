import turtle
t=turtle.Pen()
turtle.bgcolor('black')
colors=["red", "orange", "yellow", "green", "blue", "purple", "gray", "brown", "aqua", "sea green"]
your_name = turtle.textinput("Enter Your Name", "What Is Your Name?")
sides = int(turtle.numinput("Number Of Sides", "How Many Sides Do You Want (1-10)", 5, 1, 10))
for x in range(100):
    t.pencolor(colors[x%sides%10])
    t.penup()
    t.forward(x*4)
    t.pendown()
    t.write(your_name, font=("Times", int( (x*2 + 4) /4), "bold"))
    #t.left(360/sides+2)