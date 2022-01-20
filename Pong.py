# Import basic graphic module ( -> beginner-friendly)

import turtle

# Defining a window that is close to native resolution
wn = turtle.Screen()
wn.title("Pong by Lenard")
wn.bgcolor("black")
wn = turtle.Screen()
wn.setup(width=1.0, height=1.0)

# This stops the window from updating ( -> speeds up game)
wn.tracer(0)

# TODO test paddle
# Left paddle
paddle_left = turtle.Turtle()  # small t = module name, big T is class name
paddle_left.speed(0)  # this is animation speed, not refresh rate
paddle_left.shape("square")
paddle_left.color("white")
paddle_left.penup()  # This module draws a line with movement, but we don't need that here ( = pen up)
paddle_left   # TODO implement start position

# TODO  Implement right paddle
# Right paddle
paddle_right = turtle.Turtle()

# TODO
# Main game loop
while True:
    wn.update()
