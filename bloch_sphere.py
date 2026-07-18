import numpy as np
from manim import *
from constants import *

def bloch_to_2d(theta, phi, radius):
    x = radius * np.sin(theta) * np.cos(phi)
    y_depth = radius * np.sin(theta) * np.sin(phi) * DEPTH_FLATTEN
    z = radius * np.cos(theta)

    return np.array([x, z + y_depth, 0])


class BlochSphere2D(VGroup):
    def __init__(self, radius, **kwargs):
        super().__init__(**kwargs)
        self.radius = radius

        self.outline = self._make_axes()
        self.equator = self._make_equator()
        self.meridians = self._make_meridians()
        self.axes = self._make_axes()
        self.labels = self._make_labels()

        self.add(self.outline, self.equator, *self.meridians, self.axes, self.labels)


    def _make_outline(self):
        return Circle(radius=self.radius, color=SPHERE_COLOR, stroke_width=2)

    def _make_equator(self):
        return Ellipse(width=self.radius * 2,
                       height=self.radius * 2  * DEPTH_FLATTEN,
                       color=EQUATOR_COLOR,
                       stroke_width=1.5)

    def _make_meridians(self):
        return [Ellipse(width=self.radius * 2 * DEPTH_FLATTEN,
                       height=self.radius * 2,
                       color=MERIDIAN_COLOR,
                       stroke_width=1.5)]


    def _make_axes(self):
        axes = VGroup()
        axes.add(Line(bloch_to_2d(np.pi, 0, self.radius),
                 bloch_to_2d(0, 0, self.radius),
                 color=AXIS_COLOR, stroke_width=1.5))

        axes.add(Line(bloch_to_2d(np.pi / 2, np.pi, self.radius),
                      bloch_to_2d(np.pi / 2, 0, self.radius),
                      color=AXIS_COLOR, stroke_width=1.5))
        return axes

    def _make_labels(self):
        labels = VGroup()
        for key, (text, direction) in BLOCH_LABELS.items():
            theta, phi = self._direction_to_angle(direction)
            pos = bloch_to_2d(theta, phi, radius=self.radius)
            offset = np.array(direction) * 0.4
            label = Text(text, font=FONT, color=LABEL_COLOR, font_size=20)
            label.move_to(pos + offset)
            labels.add(label)
        return labels

    @staticmethod
    def _direction_to_angle(direction):
        x, y, z = direction
        theta = np.arccos(z)
        phi = np.arctan2(y, x)
        return theta, phi

    def point_at(self, thera, phi):
        local = bloch_to_2d(thera, phi, radius=self.radius)
        return self.outline.get_center() + local