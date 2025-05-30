from turtle import *

#we want to paint a house
speed(10)

width(7)
color("red")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door

forward(70)
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)

penup()
goto(200, 200)
pendown()

color("green")
right(150)
forward(200)
left(120)
forward(200)
end_fill()

done
exitonclick()