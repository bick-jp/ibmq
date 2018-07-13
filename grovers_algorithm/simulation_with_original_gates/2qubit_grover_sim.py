import getpass, time
from qiskit import ClassicalRegister, QuantumRegister, QuantumProgram
from qiskit import QuantumCircuit,  available_backends, execute, register, get_backend
from math import pi

# import basic plot tools
from qiskit.tools.visualization import plot_histogram, circuit_drawer, plot_circuit

backend = "local_qasm_simulator"
print("The best backend is " + backend)

qp = QuantumProgram()

nq = 2  # number of qubits
q = qp.create_quantum_register("q", nq)
c = qp.create_classical_register("c", nq)

circuits = ['qc']
qc = qp.create_circuit(circuits[0], [q], [c])

# Create uniform superposition
qc.h(q[0])
qc.h(q[1])

# Oracle to negate |11>
qc.cz(q[1],q[0])

# Diffusion operator to amplify the probability amplitude of |11>
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
results = qp.execute(circuits, backend='local_qasm_simulator', shots=8192, seed=1) 

# Show result as histogram
data = results.get_counts(circuits[0])
plot_histogram(data)

# Don't know why but circuit_drawer does not work correctly.
# So I use plot_circuit instead.
# circuit_drawer(qc)
plot_circuit(qc)