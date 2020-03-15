import turtle
import random
from datetime import datetime

# current date and time
now = datetime.now()
timestamp = datetime.timestamp(now)

# seed random number generator
random.seed(timestamp)

S = turtle.getscreen()
t = turtle.Turtle()

# generate some integers
for i in range(100):
    length = random.randint(8,9)
    radio = random.randint(0, 360)
    t.fd(length)
    t.right(radio)
turtle.exitonclick()
