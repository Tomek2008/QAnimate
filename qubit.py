import numpy as np
from manim import *

class Qubit:
    def __init__(self, theta, phi):
        self.theta = ValueTracker(theta)
        self.phi = ValueTracker(phi)

    @classmethod
    def zero(cls):
        return cls(0, 0)

    @classmethod
    def one(cls):
        return cls(1, 1)

    def get_vector(selfs):