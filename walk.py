class walk:
    def __init__(self, FL, FR, RL, RR, l1, l2):
        self.FL = FL
        self.FR = FR
        self.RL = RL
        self.RR = RR
        self.l1 = l1
        self.l2 = l2

    def stop(self):
        self.FL.move(0, 0)
        self.FR.move(0, 0)
        self.RL.move(0, 0)
        self.RR.move(0, 0)

    def ready(self):
        pass
