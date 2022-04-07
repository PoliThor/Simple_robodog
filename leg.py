from __future__ import division
import numpy as np
import pickle
import time
from sympy import Symbol, solve, Eq
import matplotlib.pyplot as plt
from math import floor

class leg:
    def set_servos(self):
        if self.f_test == False:
            self.kit.servo[self.servos[self.sp1]].angle = self.servo_ang_1 * self.servo_inv[self.name + '1']
            self.kit.servo[self.servos[self.sp2]].angle = self.servo_ang_2 * self.servo_inv[self.name + '2']
            self.kit.servo[self.servos[self.sp3]].angle = self.servo_ang_3 * self.servo_inv[self.name + '3']

    def __init__(self, kit, servos, servo_angles, servo_inv, a0, b0, l1, l2, name, f_test=True):
        self.f_test = f_test
        self.kit = kit
        self.servo_angles = servo_angles
        self.servo_inv = servo_inv
        self.servos = servos
        self.name = name
        self.a0 = a0
        self.b0 = b0
        self.l1 = l1
        self.l2 = l2
        self.y0 = l1 + l2  # change

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

        x = float(x)
        y = float(y)

        d_x = self.leg_solves_x - x
        d_y = self.leg_solves_y - y
        d_xy = d_x**2 + d_y**2
        a, b = np.unravel_index(np.argmin(d_xy), d_xy.shape)

        print('move time: ', time.time() - Start)
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

    def elips_init(self, t, coif_a, coif_b, speed):
        self.t0 = t
        self.el_coif_a = coif_a
        self.el_coif_b = coif_b
        self.speed = speed
        self.elips_a = Symbol('a')
        self.elips_b = Symbol('b')
        self.sym_y = Symbol('y')
        self.sym_x = Symbol('x')
        eq_y = Eq((self.sym_y - self.elips_b)**2, self.elips_a**2 - self.sym_x**2 * self.elips_a**2 / self.elips_b**2)
        self.s1, self.s2 = solve(eq_y, self.sym_y)

    def elips_step(self, t):  # ep. t = 0.5 is half of sicle
        S = time.time()

        x = self.speed * np.sin(2 * np.pi * (t + self.t0) / 2)
        t = t - floor(t)
        if t >= 0.25 and t <= 0.75:
            y = self.el_coif_a*np.sqrt(self.el_coif_b**2 - x**2)/self.el_coif_b + self.el_coif_b
        else:
            y = -self.el_coif_a*np.sqrt(self.el_coif_b**2 - x**2)/self.el_coif_b + self.el_coif_b
        print(x, y)
        print(time.time() - S)
        self.move(x, y)
