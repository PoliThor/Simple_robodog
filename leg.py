from __future__ import division
import numpy as np
import pickle
import time
import matplotlib.pyplot as plt

class leg:
    def set_servos(self):
        if self.f_test == False:
            self.kit.servo[self.servos[self.sp1]].angle = self.servo_ang_1
            self.kit.servo[self.servos[self.sp2]].angle = self.servo_ang_2
            self.kit.servo[self.servos[self.sp3]].angle = self.servo_ang_3

    def __init__(self, kit, servos, servo_angles, a0, b0, l1, l2, name, f_test=True):
        self.f_test = f_test
        self.kit = kit
        self.servo_angles = servo_angles
        self.servos = servos
        self.name = name
        self.a0 = a0
        self.b0 = b0
        self.l1 = l1
        self.l2 = l2
        self.y0 = l1 + l2 # change

        with open('leg_solve_x.pickle', 'rb') as f:
            self.leg_solves_x = pickle.load(f)
        with open('leg_solve_y.pickle', 'rb') as f:
            self.leg_solves_y = pickle.load(f)

        self.sp1 = servos[name + '1']
        self.sp2 = servos[name + '2']
        self.sp3 = servos[name + '3']

        self.servo_ang_1 = servo_angles[name + '1']
        self.servo_ang_2 = servo_angles[name + '2']
        self.servo_ang_3 = servo_angles[name + '3']

        self.set_servos()

    def move(self, x, y, z=0):
        Start = time.time()

        d_x = self.leg_solves_x - x
        d_y = self.leg_solves_y - y
        d_xy = d_x**2 + d_y**2
        a, b = np.unravel_index(np.argmin(d_xy), d_xy.shape)

        print(time.time() - Start)
        print('a, b: ', a, b)

        if self.f_test:
            plt.scatter(x, y)
            plt.scatter(self.leg_solves_x[a, b], self.leg_solves_y[a, b])
            plt.xlim([-1, 1])
            plt.ylim([-1, 1])
            plt.show()

        self.servo_ang_1 = self.servo_angles[self.name + '1'] + a - 90
        self.servo_ang_2 = self.servo_angles[self.name + '2'] + b - 90
        self.servo_ang_3 = self.servo_angles[self.name + '3']

        print(self.servo_ang_1)
        print(self.servo_ang_2)

        self.set_servos()

    def init_pos(self):
        self.servo_ang_1 = self.servo_angles[self.name + '1']
        self.servo_ang_2 = self.servo_angles[self.name + '2']
        self.servo_ang_3 = self.servo_angles[self.name + '3']

        self.set_servos()
