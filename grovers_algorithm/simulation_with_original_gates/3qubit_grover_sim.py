import getpass, time
from qiskit import ClassicalRegister, QuantumRegister, QuantumProgram
from qiskit import QuantumCircuit,  available_backends, execute, register, get_backend
from math import pi
from qiskit.tools.visualization import plot_histogram, plot_circuit

# import original gate
import sys
sys.path.append('../../')
from original_gates_for_simulator import ccz


qp = QuantumProgram()

nq = 3  # number of qubits
q = qp.create_quantum_register("q", nq)
c = qp.create_classical_register("c", nq)

circuits = ['qc']
qc = qp.create_circuit(circuits[0], [q], [c])

# Create uniform superposition
qc.h(q[0])
qc.h(q[1])
qc.h(q[2])

# Grover iteration
for num in range(2):
    # Oracle
    qc.ccz(q[2], q[1], q[0])

    # Diffusion operator
    qc.h(q[0])
    qc.h(q[1])
    qc.h(q[2])
    qc.x(q[0])
    qc.x(q[1])
    qc.x(q[2])
    qc.ccz(q[2], q[1], q[0])
    qc.x(q[0])
    qc.x(q[1])
    qc.x(q[2])
    qc.h(q[0])
    qc.h(q[1])
    qc.h(q[2])

# Measurement
qc.measure(q[0], c[0])
qc.measure(q[1], c[1])
qc.measure(q[2], c[2])

# Execution
results = qp.execute(circuits, backend='local_qasm_simulator', shots=8192, seed=1) 

# Show result
data = results.get_counts(circuits[0])
plot_histogram(data)
# plot_circuit(qc)