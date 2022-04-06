from adafruit_servokit import ServoKit
import time
import pickle

kit = ServoKit(channels=16)
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
    kit.servo[servos[n]].angle=servo_angles[n]
print(servo_angles)

while True:
    name = input('servo mane: ')
    if name == '':
        break
    while True:
        ang = input('angle: ')
        if ang == '':
            break
        else:
            if name not in colibration_coif.keys():
                colibration_coif[name] = int(ang)
            colibration_coif[name] += int(ang)
            servo_angles[name] += int(ang) 
            kit.servo[servos[name]].angle=servo_angles[name]

print(colibration_coif)

with open('colib_coif.pickle', 'wb') as f:
    pickle.dump(colibration_coif, f)
