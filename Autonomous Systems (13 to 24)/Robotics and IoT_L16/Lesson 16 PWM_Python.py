# Add your Python code here. E.g.
from microbit import *

leftA = pin0
leftB = pin8
rightA = pin1
rightB = pin12

def forward (speedpct):
    speed = speedpct * 10.23
    leftA.write_analog(speed)
    leftB.write_digital(0)
    rightA.write_analog(speed)
    rightB.write_digital(0)

def reverse (speedpct):
    speed = speedpct * 10.23
    leftA.write_analog(1023-speed)
    leftB.write_digital(1)
    rightA.write_analog(1023-speed)
    rightB.write_digital(1)

def spinLeft (speedpct):
    speed = speedpct * 10.23
    leftA.write_analog(1023-speed)
    leftB.write_digital(1)
    rightA.write_analog(speed)
    rightB.write_digital(0)

def spinRight (speedpct):
    speed = speedpct * 10.23
    leftA.write_analog(speed)
    leftB.write_digital(0)
    rightA.write_analog(1023-speed)
    rightB.write_digital(1)

def stop():
    leftA.write_analog(0)
    leftB.write_digital(0)
    rightA.write_analog(0)
    rightB.write_digital(0)

while True:
    display.show(Image.ARROW_N)
    forward(50)
    sleep(3000)
    display.show(Image.ARROW_E)
    spinRight(50)
    sleep(3000)
    display.show(Image.ARROW_S)
    reverse(50)
    sleep(3000)
    display.show(Image.ARROW_W)
    spinLeft(50)
    sleep(3000)
    display.show(Image.HAPPY)
    stop()
    sleep(3000)
