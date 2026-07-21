from constants import *

class Qubit:
    def __init__(self, theta, phi, r=1):
        self.theta = ValueTracker(theta)
        self.phi = ValueTracker(phi)
        self.r = ValueTracker(r)

    @classmethod
    def zero(cls):
        return cls(0, 0)

    @classmethod
    def one(cls):
        return cls(np.pi / 2, 0)

    def set_angles(self, theta, phi):
        return [self.theta.animate.set_value(theta), self.phi.animate.set_value(phi)]