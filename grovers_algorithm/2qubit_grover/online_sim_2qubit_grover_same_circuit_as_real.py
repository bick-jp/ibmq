# import timing to get execution time
import sys
sys.path.append('../')
import timing

import getpass, time
from qiskit import ClassicalRegister, QuantumRegister, QuantumProgram
from qiskit import QuantumCircuit,  available_backends, execute, register, get_backend
from math import pi
from qiskit.tools.visualization import plot_histogram, plot_circuit

qx_config = {
    "APItoken": "f7f5c264ff5275d134d712a2d6c3d46b9a25a464e9985adccc3892d9180e0333d7a8b5b05ef4079d887c4347d2c42b3a787651e74c934c2c8be7ee247a4cd83a",
    "url":"https://quantumexperience.ng.bluemix.net/api"}

register(qx_config['APItoken'], qx_config['url'])

backend = "ibmq_qasm_simulator"

qp = QuantumProgram()

nq = 2  # number of qubits
q = qp.create_quantum_register("q", nq)
c = qp.create_classical_register("c", nq)

circuits = ['qc']
qc = qp.create_circuit(circuits[0], [q], [c])

# Create superposition
qc.h(q[0])
qc.h(q[1])

# Oracle
qc.h(q[0])
qc.cx(q[1],q[0])
qc.h(q[0])

# Diffusion operator
qc.h(q[0])
qc.h(q[1])
qc.x(q[0])
qc.x(q[1])
qc.h(q[0])
qc.cx(q[1],q[0])
qc.h(q[0])
qc.x(q[0])
qc.x(q[1])
qc.h(q[0])
qc.h(q[1])

# Measurement
qc.measure(q[0], c[0])
qc.measure(q[1], c[1])

# Execution
results = qp.execute(circuits, backend=backend, shots=8192, seed=1)

# Show result
# hist = results.get_counts(circuits[0])
# plot_histogram(hist)
# plot_circuit(qc)
data = results.get_data(circuits[0])
print(data)