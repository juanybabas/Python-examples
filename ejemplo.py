import turtle


turtle.setup(900, 700)
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("juan")


estres= turtle.Turtle()
estres.pensize(5)
estres.shape("turtle")
estres.speed(1)




frio = turtle.Turtle()
frio.pensize(5)
frio.shape("turtle")
frio.goto(-320,10)
frio.speed(1)
#mi instacia
aburrido=turtle.Turtle()
aburrido.pensize(5)
aburrido.shape("turtle")
aburrido.goto(-100,-245)




estres.color("red")
estres.forward(320)
estres.left(120)
estres.color("blue")
estres.forward(320)
estres.left(120)
estres.color("violet")
estres.forward(320)
estres.left(120)


frio.color("blue")
frio.forward(200)

frio.left(90)
frio.color("green")
frio.forward(200)

frio.left(90)
frio.color("white")
frio.forward(200)

frio.left(90)
frio.color("yellow")
frio.forward(200)

aburrido.color("light blue")
aburrido.write("loool",font=("Algerian",18,"bold"))
aburrido.left(0)
aburrido.color("GREEN")

aburrido.forward(70)
aburrido.color("")
aburrido.goto(-55,-320)
aburrido.color("blue")
aburrido.circle(85)
aburrido.fd(175)

wn.exitonclick()