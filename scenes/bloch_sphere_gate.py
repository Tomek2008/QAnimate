import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from qanimate.bloch_sphere import BlochSphere3D
from qanimate.qubit import Qubit
from manim import *

H_GATE = np.array([[1, 1], [1, -1]]) / np.sqrt(2)
X_GATE = np.array([[0, 1], [1, 0]])
Y_GATE = np.array([[0, -1j], [1j, 0]])
Z_GATE = np.array([[1, 0], [0, -1]])


class GateScene(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=65 * DEGREES, theta=-45 * DEGREES)

        bloch = BlochSphere3D(radius=2)
        qubit = Qubit.zero()
        vector = bloch.vector(qubit)

        self.add(bloch, vector)
        self.wait(0.5)

        for label_text, gate in [("H", H_GATE), ("X", X_GATE), ("Z", Z_GATE)]:
            label = Text(label_text, font_size=40)

            self.play(FadeIn(label, scale=0.5), run_time=0.3)
            label.to_corner(UL)
            self.add_fixed_in_frame_mobjects(label)
            self.play(*qubit.apply_gate(gate), run_time=1.5)
            self.play(FadeOut(label), run_time=0.3)
            self.wait(0.3)

        self.wait(1)