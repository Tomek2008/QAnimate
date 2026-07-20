from qiskit import QuantumCircuit


def oracle(n_qubits, marked_state):
    qc = QuantumCircuit(n_qubits, name="Oracle")
    zero_indices = [i for i, bit in enumerate(reversed(marked_state)) if bit == "0"]
    qc.x(zero_indices)

    qc.h(n_qubits - 1)
    qc.mcx(list(range(n_qubits - 1)), n_qubits - 1)
    qc.h(n_qubits - 1)

    qc.x(zero_indices)
    return qc


def diffuser(n_qubits):
    qc = QuantumCircuit(n_qubits, name="Diffuser")
    qc.h(range(n_qubits))
    qc.x(range(n_qubits))

    qc.h(n_qubits - 1)
    qc.mcx(list(range(n_qubits - 1)), n_qubits - 1)
    qc.h(n_qubits - 1)

    qc.x(range(n_qubits))
    qc.h(range(n_qubits))
    return qc