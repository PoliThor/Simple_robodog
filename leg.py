from __future__ import division
from typing_extensions import Self
from sympy import *
from sympy.solvers import solve
from sympy import Symbol
import numpy as np

import pdb


class leg:
    def set_servos(self):
        if self.f_test == False:
            self.kit.servo[self.servos[self.sp1]].angle = self.self.servo_ang_1
            self.kit.servo[self.servos[self.sp2]].angle = self.self.servo_ang_2
            self.kit.servo[self.servos[self.sp3]].angle = self.self.servo_ang_3

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

        self.sym_a = Symbol('a', real=True)
        self.sym_b = Symbol('b', real=True)

        self.sp1 = servos[name + '1']
        self.sp2 = servos[name + '2']
        self.sp1 = servos[name + '3']

        self.servo_ang_1 = servo_angles[name + '1']
        self.servo_ang_2 = servo_angles[name + '2']
        self.servo_ang_3 = servo_angles[name + '3']

        self.X = 0
        self.Y = 0
        self.Z = 0

        self.set_servos()

    def move(self, x, y, z=0):
        a = self.sym_a
        b = self.sym_b
        eq1 = parse_expr(f'{self.l1} * sin(a) - {self.l2} * sin(a - b) - {x}')
        eq2 = parse_expr(f'{self.y0} - {self.l1} * cos(a) - {self.l2} * sin(pi / 2 - b + a) - {y}')

        print(eq1)
        print(eq2)
        ans = solveset([eq1, eq2], [a, b])
        print(ans)

    def init_pos(self):
        self.servo_ang_1 = self.servo_angles[self.name + '1']
        self.servo_ang_2 = self.servo_angles[self.name + '2']
        self.servo_ang_3 = self.servo_angles[self.name + '3']

        self.set_servos()
