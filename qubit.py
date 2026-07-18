import numpy as np
from manim import *
from constants import *
from bloch_sphere import BlochSphere2D

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

    def get_vector(self, sphere):
        end = sphere.point_at(self.theta.get_value(), self.phi.get_value())
        start = sphere.outline.get_center()
        return Arrow(start, end, color=VECTOR_COLOR, stroke_width=2, max_tip_length_to_length_ratio=0.1)

    def set_angles(self, theta, phi):
        return [self.theta.animate.set_value(theta), self.phi.animate.set_value(phi)]