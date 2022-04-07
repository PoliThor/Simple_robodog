import time
import pickle

from leg import leg

f_test = True

# constants in mm
l1 = 1
l2 = 1
a0 = 0
b0 = 0

if f_test == False:
    from adafruit_servokit import ServoKit
    kit = ServoKit(channels=16)
else:
    kit = None

# do leg init first
servos = {'RR1': 1, 'RR2': 2, 'RR3': 3, 'RL3': 7, 'RL2': 6, 'RL1': 5, 'FR3': 9, 'FR2': 10,
          'FR1': 11, 'FL2': 13, 'FL3': 14, 'FL1': 15}

try:
    with open('colib_coif.pickle', 'rb') as f:
        colibration_coif = pickle.load(f)
    print('coif load')
    print('colib coif: ', colibration_coif)
except FileNotFoundError:
    colibration_coif = {}

servo_angles = {}
for n in servos:
    if n in colibration_coif.keys():
        servo_angles[n] = 90 + colibration_coif[n]
    else:
        servo_angles[n] = 90


print(servo_angles)

FL = leg(kit, servos, servo_angles, a0, b0, l1, l2, name='FL')
FR = leg(kit, servos, servo_angles, a0, b0, l1, l2, name='FR')
RL = leg(kit, servos, servo_angles, a0, b0, l1, l2, name='RL')
RR = leg(kit, servos, servo_angles, a0, b0, l1, l2, name='RR')

FL.move(0.3, 0.3)
