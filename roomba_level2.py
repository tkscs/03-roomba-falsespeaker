# -----------------------------------------------------------------------------
# Roomba in Python
# This file implements an algorithm for a roomba cleaning a room.
#
# Author: Tyler Shub <------ REPLACE THIS WITH YOUR NAME!
# -----------------------------------------------------------------------------
 
from turtle import right, left, forward, backward, speed
import room

# Make the turtle go faster
speed(7)

# Draw the Level 2 version of the room
window = room.draw_room(level = 2)

###
# Start your code here
fd=forward
rt=right
lt=left

speed(25)
for i in range(9):
    fd(560)
    lt(90)
    fd(40)
    lt(90)
    fd(560)
    rt(90)
    fd(40)
    rt(90)

fd(560)
lt(90)
fd(40)
lt(90)
fd(560)
rt(90)
 
# End your code here
###
 
window.exitonclick()