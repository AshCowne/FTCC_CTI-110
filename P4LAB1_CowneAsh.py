# Ash Cowne
#11/7/2024
# P4LAB1
# Write a turtle graphics programs that draws a triangle and a square using loops.

import turtle
win = turtle.Screen()
t = turtle.Turtle()
win.bgcolor("teal")

# Defalt pensize is 0.
t.pensize(2)
t.pencolor("turquoise")

# This shape only makes the arrow bigger.
#t.shape("arrow")
# This shape does not work, as do many other things that I put in.
#t.shape("\U0001F600")

# While loop to draw a square and triangle.
num_sq = 0
num_tr = 0

while num_sq  < 4:
    t.forward(50)
    t.left(90)
    num_sq += 1

while num_tr < 3:
    t.forward(50)
    t.left(120)
    num_tr += 1

t.forward(100)


# For loop to drap a triangle and square.
for i in range(3):
    t.forward(50)
    t.left(120)

for i in range(4):
    t.forward(50)
    t.left(90)
