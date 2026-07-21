import numpy as np
from manim import *
from constants import *


def bloch_to_3d(theta, phi, radius):
    x = radius * np.sin(theta) * np.cos(phi)
    y = radius * np.sin(theta) * np.sin(phi)
    z = radius * np.cos(theta)
    return np.array([x, y, z])


class BlochSphere3D(VGroup):
    def __init__(self, radius, show_labels=True, **kwargs):
        super().__init__(**kwargs)
        self.radius = radius
        self.entanglement_ring = None

        self.surface = self._make_surface()
        self.equator = self._make_equator()
        self.meridians = self._make_meridians()
        self.axes = self._make_axes()
        self.labels = self._make_labels()

        self.add(self.surface, self.equator, *self.meridians, self.axes)
        if show_labels:
            self.add(self.labels)

    def _make_surface(self):
        sphere = Sphere(
            radius=self.radius,
            resolution=(24, 24),
            fill_opacity=0.08,
            stroke_opacity=0.0,
            checkerboard_colors=[SPHERE_COLOR, SPHERE_COLOR],
        )
        sphere.set_color(SPHERE_COLOR)

        return sphere

    def _make_equator(self):
        return Circle(radius=self.radius, color=EQUATOR_COLOR, stroke_width=1.5)

    def _make_meridians(self):
        meridian_xz = Circle(radius=self.radius, color=MERIDIAN_COLOR, stroke_width=1.5)
        meridian_xz.rotate(PI / 2, axis=RIGHT)
        meridian_yz = Circle(radius=self.radius, color=MERIDIAN_COLOR, stroke_width=1.5)
        meridian_yz.rotate(PI / 2, axis=UP)
        return [meridian_xz, meridian_yz]

    def _make_axes(self):
        axes = VGroup()
        axes.add(Line3D(
            bloch_to_3d(np.pi, 0, self.radius),
            bloch_to_3d(0, 0, self.radius),
            color=AXIS_COLOR, thickness=0.01,
        ))
        axes.add(Line3D(
            bloch_to_3d(np.pi / 2, np.pi, self.radius),
            bloch_to_3d(np.pi / 2, 0, self.radius),
            color=AXIS_COLOR, thickness=0.01,
        ))
        axes.add(Line3D(
            bloch_to_3d(np.pi / 2, -np.pi / 2, self.radius),
            bloch_to_3d(np.pi / 2, np.pi / 2, self.radius),
            color=AXIS_COLOR, thickness=0.01,
        ))
        return axes

    def _make_labels(self):
        labels = VGroup()
        for key, (text, direction) in BLOCH_LABELS.items():
            theta, phi = self._direction_to_angle(direction)
            pos = bloch_to_3d(theta, phi, radius=self.radius)
            offset = np.array(direction) * 0.7
            label = Text(text, font=FONT, color=LABEL_COLOR, font_size=28)
            label.move_to(pos + offset)
            labels.add(label)
        return labels

    @staticmethod
    def _direction_to_angle(direction):
        x, y, z = direction
        theta = np.arccos(z)
        phi = np.arctan2(y, x)
        return theta, phi

    def point_at(self, theta, phi):
        local = bloch_to_3d(theta, phi, radius=self.radius)
        return self.get_center() + local

    def vector(self, qubit):
        return always_redraw(
            lambda: Arrow3D(
                start=self.get_center(),
                end=self.point_at(
                    qubit.theta.get_value(),
                    qubit.phi.get_value(),
                ),
                color=VECTOR_COLOR,
                thickness=0.02,
                base_radius=0.05,
            )
        )

    def set_entanglement_color(self, color):
        ring_a = Circle(
            radius=self.radius * 1.08,
            stroke_width=6,
            stroke_opacity=0.8,
            fill_opacity=0,
        )
        ring_a.set_stroke(color, width=6)
        ring_b = ring_a.copy().rotate(PI / 2, axis=RIGHT)
        ring_c = ring_a.copy().rotate(PI / 2, axis=UP)

        self.entanglement_ring = VGroup(ring_a, ring_b, ring_c)
        self.add(self.entanglement_ring)
        return self.entanglement_ring

    def clear_entanglement_color(self):
        if self.entanglement_ring is not None:
            self.remove(self.entanglement_ring)
            self.entanglement_ring = None