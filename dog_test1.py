from adafruit_servokit import ServoKit
import time
kit = ServoKit(channels=16)
for i in range(16):
    time.sleep(0.1)
    kit.servo[i].angle=90
    print(i)
quit()
                                                         