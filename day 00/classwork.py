from turtle import *

speed(50)
#we want to paint a house

#step 1: draw a rectangle
width(5)
color("blue")
begin_fill()
forward(200)
left(90)

forward(300)
left(90)

forward(200)
left(90)

forward(300)
left(90)

forward(70)
left(90)
end_fill()
#end of rectangle

#step 2: draw a door

color("red")
begin_fill()
forward(90)           #height of the door

right(90)
forward(40)

right(90)
forward(90)
end_fill()
penup()
goto(200, 300)

pendown()
 
 #step 3: draw a triangle

color("purple")
begin_fill()
right(135)
forward(130) 

left(85)
forward(140)
end_fill()
penup()
goto(40, 170)

pendown()

#step 4: draw windows

right(130)

color("black")
begin_fill()
forward(80)
right(90)
forward(40)
right(90)
forward(80)
right(90)
forward(40)

penup()
goto(160, 170)

pendown()

forward(40)
right(90)
forward(80)
right(90)
forward(40)
right(90)
forward(80)

end_fill()
penup()

goto(0, 0)
pendown()
color("green")
#step 5: make a grass
begin_fill()
left(90)
forward(600)

right(90)
forward(400)

right(90)
forward(1500)
right(90)
forward(400)
right(90)
forward(1600)
end_fill()

penup()
goto(-150, -300)
pendown()

color("blue")
begin_fill()
circle(100)
end_fill()












exitonclick()