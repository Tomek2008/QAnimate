import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from bloch_sphere import BlochSphere3D
from qubit import Qubit
from manim import *
from constants import *

class BlochSphereTwoQubits(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=0 * DEGREES)

        shift1 = UP * 2.5
        shift2 = DOWN * 2.5

        sphere1 = BlochSphere3D(radius=1.5, show_labels=False)
        sphere2 = BlochSphere3D(radius=1.5, show_labels=False)

        group1 = VGroup(sphere1.surface, sphere1.equator, *sphere1.meridians, sphere1.axes)
        group2 = VGroup(sphere2.surface, sphere2.equator, *sphere2.meridians, sphere2.axes)

        group1.shift(shift1)
        group2.shift(shift2)

        q1 = Qubit.zero()
        q2 = Qubit.zero()

        vector1 = sphere1.vector(q1).shift(shift1)
        vector2 = sphere2.vector(q2).shift(shift2)

        self.add(vector1, vector2)
        self.add(group1, group2)

        self.play(
            *q1.set_angles(np.pi / 2, 0),
            *q2.set_angles(np.pi, 0),
            run_time=2.5,
        )
        self.play(
            *q1.set_angles(np.pi, 0),
            *q2.set_angles(np.pi / 2, np.pi),
            run_time=2.5,
        )

        ring1 = sphere1.set_entanglement_color(ENTANGLE_COLOR)
        ring1.shift(shift1)
        ring2 = sphere2.set_entanglement_color(ENTANGLE_COLOR)
        ring2.shift(shift2)

        self.play(
            Create(ring1),
            Create(ring2),
            run_time=1,
        )

        self.play(
            q1.r.animate.set_value(0),
            q2.r.animate.set_value(0),
            run_time=2,
        )

        self.wait(1)

        self.play(
            q1.r.animate.set_value(1),
            q1.set_angles(0, 0)[0],
            q1.set_angles(0, 0)[1],
            q2.r.animate.set_value(1),
            q2.set_angles(np.pi, 0)[0],
            q2.set_angles(np.pi, 0)[1],
            Flash(ring1, color=ENTANGLE_COLOR),
            Flash(ring2, color=ENTANGLE_COLOR),
            run_time=1,
        )

        self.wait(1)