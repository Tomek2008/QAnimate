from manim import *

BLOCH_RADIUS = 1
DEPTH_FLATTEN = 0.4

SPHERE_COLOR = GRAY_A
EQUATOR_COLOR = GRAY_C
MERIDIAN_COLOR = GRAY_E
AXIS_COLOR = WHITE
VECTOR_COLOR = YELLOW
LABEL_COLOR = WHITE
STATE_TEXT_COLOR = TEAL
ENTANGLE_COLOR = LIGHT_PINK

FONT = "Helvetica"

BLOCH_LABELS = {
    "0":  ("|0⟩", (0, 0, 1)),
    "1":  ("|1⟩", (0, 0, -1)),
    "+":  ("|+⟩", (1, 0, 0)),
    "-":  ("|-⟩", (-1, 0, 0)),
    "i":  ("|i⟩", (0, 1, 0)),
    "-i": ("|-i⟩", (0, -1, 0)),
}