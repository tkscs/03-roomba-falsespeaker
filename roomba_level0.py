# -----------------------------------------------------------------------------
# Roomba in Python
# This file implements an algorithm for a roomba cleaning a room.
#
# Author: Dr. EB <------ REPLACE THIS WITH YOUR NAME!
# -----------------------------------------------------------------------------
 
from turtle import right, left, forward, backward
import room

# Draw the Level 0 version of the room
window = room.draw_room(level = 0)
fd=forward
rt=right
lt=left
###
# Start your code here
for i in range(2):
    fd(160)
    lt(90)
    fd(40)
    lt(90)
    fd(160)
    rt(90)
    fd(40)
    rt(90)
fd(160)

# End your code here
###
 
window.exitonclick()