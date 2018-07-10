from qiskit import QuantumProgram
from qiskit.tools.visualization import plot_histogram, circuit_drawer
from math import pi

# import original gate
from original_gate import cccz

qp = QuantumProgram()

nq = 4  # number of qubits
q = qp.create_quantum_register("q", nq)
c = qp.create_classical_register("c", nq)

circuits = ['qc']
qc = qp.create_circuit(circuits[0], [q], [c])

# Create uniform superposition
qc.h(q[0])
qc.h(q[1])
qc.h(q[2])
qc.h(q[3])

# Three times Grover iteration to find |1111>
for num in range(3):
    # Oracle to negate |1111>
    qc.cccz(q[0], q[1], q[2], q[3])

    # Diffusion operator to amplify the probability amplitude of |1111>
    qc.h(q[0])
    qc.h(q[1])
    qc.h(q[2])
    qc.h(q[3])
    qc.x(q[0])
    qc.x(q[1])
    qc.x(q[2])
    qc.x(q[3])
    qc.cccz(q[0], q[1], q[2], q[3])
    qc.x(q[0])
    qc.x(q[1])
    qc.x(q[2])
    qc.x(q[3])
    qc.h(q[0])
    qc.h(q[1])
    qc.h(q[2])
    qc.h(q[3])

# Measurement
qc.measure(q[0], c[0])
qc.measure(q[1], c[1])
qc.measure(q[2], c[2])
qc.measure(q[3], c[3])

# Execution
results = qp.execute(circuits, backend='local_qasm_simulator', shots=8192, seed=1) 

# Show result as histogram
plot_histogram(results.get_counts(circuits[0]))

#circuit_drawer(testQ)