# Import basic graphic module ( -> beginner-friendly)

import turtle

# Defining a window that is native resolution

wn = turtle.Screen()
wn.title("Pong by Lenard")
wn.bgcolor("black")
wn = turtle.Screen()
wn.setup(width=1.0, height=1.0)

# This stops the window from updating ( -> speeds up game)
wn.tracer(0)

# Main game loop
while True:
    wn.update()
