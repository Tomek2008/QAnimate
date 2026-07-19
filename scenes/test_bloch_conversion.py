import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from bloch_sphere import BlochSphere2D
from qubit import Qubit
from manim import *

class BlochSphereCheck(Scene):
    def construct(self):
        sphere = BlochSphere2D(radius=3)
        self.play(Create(sphere))

        q = Qubit.zero()
        vector = sphere.vector(q)
        self.play(Create(vector))
        self.wait(0.5)

        self.play(*q.set_angles(np.pi / 2), run_time=1.5)
        self.wait(0.5)

        self.play(*q.set_angles(np.pi, 0), run_time=1.5)
        self.wait(0.5)

        self.play(*q.set_angles(np.pi / 2, np.pi), run_time=1.5)
        self.wait()

        self.play(*q.set_angles(np.pi / 1.3, np.pi), run_time=1.5)
        self.wait()