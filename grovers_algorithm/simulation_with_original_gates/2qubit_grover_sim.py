# import timing to get execution time
import sys
sys.path.append('../')
import timing

from qiskit import QuantumProgram
from qiskit.tools.visualization import plot_histogram, circuit_drawer, plot_circuit
from math import pi

backend = "local_qasm_simulator"

qp = QuantumProgram()

nq = 2  # number of qubits
q = qp.create_quantum_register("q", nq)
c = qp.create_classical_register("c", nq)

circuits = ['qc']
qc = qp.create_circuit(circuits[0], [q], [c])

# Create uniform superposition
qc.h(q[0])
qc.h(q[1])

# Oracle
qc.cz(q[1],q[0])

# Diffusion operator
qc.h(q[0])
qc.h(q[1])
qc.x(q[0])
qc.x(q[1])
qc.cz(q[1],q[0])
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
# data = results.get_counts(circuits[0])
# plot_histogram(data)
# plot_circuit(qc)