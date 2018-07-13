import getpass, time
from qiskit import ClassicalRegister, QuantumRegister, QuantumProgram
from qiskit import QuantumCircuit,  available_backends, execute, register, get_backend
from math import pi

# import basic plot tools
from qiskit.tools.visualization import plot_histogram, circuit_drawer, plot_circuit

# import original gate
from original_gate import ccz

backend = "local_qasm_simulator"
print("The best backend is " + backend)

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

# Two times Grover iteration to find |111>
for num in range(2):
    # Oracle to negate |111>
    qc.ccz(q[2], q[1], q[0])

    # Diffusion operator to amplify the probability amplitude of |111>
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

# Show result as histogram
data = results.get_counts(circuits[0])
plot_histogram(data)

# Don't know why but circuit_drawer does not work correctly.
# So I use plot_circuit instead.
# circuit_drawer(qc)
plot_circuit(qc)