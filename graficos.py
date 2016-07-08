import turtle


turtle.setup(900, 700)
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("juan")

#mi intacia
aburrido = turtle.Turtle()
aburrido.speed(15)
aburrido.pensize(1)



for x in range(200):
    aburrido.forward(x)
    aburrido.color("blue")
    aburrido.forward(200)
    aburrido.left(90)
    aburrido.color("green")
    aburrido.forward(200)
    aburrido.left(90)
    aburrido.color("white")
    aburrido.forward(200)
    aburrido.left(90)
    aburrido.color("yellow")
    aburrido.forward(200)
    aburrido.color("red")
    aburrido.forward(320)
    aburrido.left(120)
    aburrido.color("blue")
    aburrido.forward(320)
    aburrido.left(120)
    aburrido.color("violet")
    aburrido.forward(320)
    aburrido.left(120)

aburrido.color("")
aburrido.pensize(0)
aburrido.goto(-65,0)
aburrido.color("White")
aburrido.write("hace mucho frio",font=("Algerian",20,"bold"))


wn.exitonclick()