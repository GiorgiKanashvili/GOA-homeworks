from turtle import *

#making wall of a house 

speed(4)

width(5)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)

#making door of a house


begin_fill()
left(90)
forward(70)
color("red")
left(90)
forward(100)
right(90)
forward(60)
right(90)
forward(100)
end_fill()


#making roof of our Chadest house:)
penup()
goto(200, 200)
pendown()

begin_fill()
right(120)
forward(150)
left(80)
forward(100)
end_fill()



#making windows

penup()
goto(25, 150)
pendown()

begin_fill()

color("blue")

left(35)
forward(25)
left(90)
forward(25)
left(90)
forward(25)
left(90)
forward(25)

end_fill()

#making second window


begin_fill()
color("brown")

penup()
goto(125, 150)
pendown()
left(90)
forward(25)
left(90)
forward(25)
left(90)
forward(25)
left(90)
forward(25)

end_fill()


exitonclick()