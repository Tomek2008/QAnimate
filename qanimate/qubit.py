from .constants import *


def bloch_to_statevector(theta, phi):
    return np.array([
        np.cos(theta / 2),
        np.exp(1j * phi) * np.sin(theta / 2),
    ])


def statevector_to_bloch(state):
    a, b = state
    theta = 2 * np.arccos(np.clip(np.abs(a), -1, 1))
    phi = np.angle(b) - np.angle(a)
    return theta, phi % (2 * np.pi)


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

    def gate_angles(self, gate_matrix):
        state = bloch_to_statevector(self.theta.get_value(), self.phi.get_value())
        new_state = gate_matrix @ state
        return statevector_to_bloch(new_state)

    def apply_gate(self, gate_matrix):
        theta, phi = self.gate_angles(gate_matrix)
        return self.set_angles(theta, phi)