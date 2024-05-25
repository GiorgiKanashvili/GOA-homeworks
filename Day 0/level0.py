from turtle import *

#making wall of a house 

speed(10)

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
right(135)
forward(140)
left(90)
forward(140)
end_fill()

penup()
left(45)
forward(20)
left(90)
forward(25)
pendown()


#making widows

color("brown")
begin_fill()
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()

penup()
right(90)
forward(100)
pendown()
 

begin_fill()
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()



penup()
right(90)
forward(180)
left(90)
forward(100)
pendown()

color("yellow")
begin_fill()
circle(50)
end_fill()





exitonclick()