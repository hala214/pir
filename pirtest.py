from gpiozero import MotionSensor
from gpiozero import Buzzer
from time import sleep
pir=MotionSensor(4)
buzzer=Buzzer(17)

while True:
    if pir.wait_for_motion():
        print("you moved")
        buzzer.on()
        sleep(1)
    if pir.wait_for_no_motion():
        print("no motion")
        buzzer.off()
        sleep(1)