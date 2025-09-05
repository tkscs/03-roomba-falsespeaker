# -----------------------------------------------------------------------------
# Roomba in Python
# This file implements an algorithm for a roomba cleaning a room.
#
# Author: Dr. EB <------ REPLACE THIS WITH YOUR NAME!
# -----------------------------------------------------------------------------
 
from turtle import right, left, forward, backward, speed
import room

# Make the turtle go faster
speed(7)

# Draw the Level 3 version of the room
window = room.draw_room(level = 3, radius = 5)

###
# Start your code here
fd=forward
rt=right
lt=left

def draw_shape(number_of_sides):
    angle = 360 / number_of_sides
    for _ in range(number_of_sides):
        fd(50)
        lt(angle)
draw_shape(8)
draw_shape(7)
draw_shape(6)
draw_shape(5)
draw_shape(4)
draw_shape(3)
draw_shape(2)

# End your code here
###
 
window.exitonclick()