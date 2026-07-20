import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from bloch_sphere import BlochSphere3D
from qubit import Qubit
from manim import *

class BlochSphereCheck(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=65 * DEGREES, theta=-45 * DEGREES)

        sphere = BlochSphere3D(radius=1.5, show_labels=True)
        bloch_sphere = VGroup(sphere.surface, sphere.equator, *sphere.meridians, sphere.axes)
        q = Qubit.zero()
        vector = sphere.vector(q)

        self.add(vector)
        self.add(bloch_sphere)
        self.add_fixed_orientation_mobjects(*sphere.labels)

        self.begin_ambient_camera_rotation(rate=2 * PI / 10)
        self.play(*q.set_angles(np.pi / 2, 0), run_time=2.5)
        self.play(*q.set_angles(np.pi, 0), run_time=2.5)
        self.play(*q.set_angles(0, np.pi), run_time=2.5)
        self.play(*q.set_angles(0, np.pi / 2), run_time=2.5)
        self.stop_ambient_camera_rotation()