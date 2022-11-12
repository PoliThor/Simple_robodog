import math

import matplotlib.pyplot as plt


class Visualisation_Kit:
    def __init__(self, l1=5, l2=10, l3=10) -> None:
        '''
        l1: Длинна лопатки
        l2: Длинна плеча
        l3: Длинна локтя
        '''
        fig, ax = plt.subplots()
        self.fig = fig
        self.ax = ax

        self.x0 = 0
        self.y0 = 0
        self.z0 = 0
        self.l1 = l1
        self.l2 = l2
        self.l3 = l3
        # 1 not inverse, 2 inverse
        self.inv1 = 1
        self.inv2 = 1
        self.inv3 = 1

    

    def set_angle(self, angle1, angle2, angle3):
        angle1 = math.radians(angle1)
        angle2 = math.radians(angle2)
        angle3 = math.radians(angle3)
        x_points = [self.x0]
        y_points = [self.y0]
        z_points = [self.z0]

        


