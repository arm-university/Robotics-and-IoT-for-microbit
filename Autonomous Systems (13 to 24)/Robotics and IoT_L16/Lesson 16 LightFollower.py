from microbit import *

leftA = pin0
leftB = pin8
rightA = pin1
rightB = pin12
lightSensor = pin2
lightSelect = pin16

while True:
    lightSelect.write_digital(0) # select left sensor
    rval = lightSensor.read_analog()
    leftA.write_analog(rval)
    leftB.write_digital(0)
    sleep(1)
    lightSelect.write_digital(1) # select right sensor
    rval = lightSensor.read_analog()
    rightA.write_analog(rval)
    rightB.write_digital(0)
    sleep(1)
