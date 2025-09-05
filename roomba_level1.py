# -----------------------------------------------------------------------------
# Roomba in Python
# This file implements an algorithm for a roomba cleaning a room.
#
# Author: Dr. EB <------ REPLACE THIS WITH YOUR NAME!
# -----------------------------------------------------------------------------
 
from turtle import left, forward, backward
import room

# Draw the Level 1 version of the room
window = room.draw_room(level = 1)

###
# Start your code here
fd=forward
lt=left
 
fd(160)
lt(90)
fd(160)
lt(90)
fd(160)
lt(90)
fd(120)
lt(90)
fd (120)
lt(90)
fd(80)
lt(90)
fd(80)
lt(90)
fd(40)
lt(90)
fd(40)
# End your code here
###
 
window.exitonclick()