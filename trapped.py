from turtle import *
import random
from datetime import datetime

now = datetime.now()
timestamp = datetime.timestamp(now)

# seed random number generator
random.seed(timestamp)

def move_in_square(side):
    if ycor() < side and ycor() >= 0 and xcor() < side and xcor() >= 0:
        fd(1)
    else:
        # print('antes: ', heading())
        # top bounce
        if ycor() >= side and heading() < 90:
            right(2*heading())
        elif ycor() >= side and heading() > 90:
            left(2*(180-heading()))

        # right bounce
        if xcor() >= side and heading() < 180:
            left(2*(90-heading()))
        elif xcor() >= side and heading() > 180:
            right(2*(heading()-270))

        # left bounce
        if xcor() <= 0 and heading() < 180:
            right(2*(heading()-90))
        elif xcor() <= 0 and heading() > 180:
            left(2*(270-heading()))

        # bottom bounce
        if ycor() <= 0 and heading() < 270:
            right(2*(heading()-180))
        elif ycor() <= 0 and heading() > 270:
            left(2*(360-heading()))
        # print('despues: ', heading())
        fd(1)

SIDE = 100

# draw square
ht()

init_grad = random.randint(5, 85)
seth(90)
for i in range(4):
    fd(SIDE)
    right(90)

print(f'angulo de salida {init_grad}')
home()
seth(init_grad)
while 1:
    move_in_square(SIDE)
