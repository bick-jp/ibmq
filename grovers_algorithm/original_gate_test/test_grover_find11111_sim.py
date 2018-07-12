from qiskit import QuantumProgram
from qiskit.tools.visualization import plot_histogram, circuit_drawer
from original_gate import ccccz

qp = QuantumProgram()

nq = 5  # number of qubits
q = qp.create_quantum_register("q", nq)
c = qp.create_classical_register("c", nq)

circuits = ['qc']
qc = qp.create_circuit(circuits[0], [q], [c])

# Create uniform superposition
for ind in range(nq):
    qc.h(q[ind])

# Grover iteration
for num in range(4):
    # Oracle
    qc.ccccz(q[0], q[1], q[2], q[3], q[4])

    # Diffusion operator
    for ind in range(nq):
        qc.h(q[ind])

    for ind in range(nq):
        qc.x(q[ind])

    qc.ccccz(q[0], q[1], q[2], q[3], q[4])

    for ind in range(nq):
        qc.x(q[ind])

    for ind in range(nq):
        qc.h(q[ind])

# Measurement
for ind in range(nq):
    qc.measure(q[ind], c[ind])

# Execution
results = qp.execute(circuits, backend='local_qasm_simulator', shots=8192, seed=1) 

# Show result as histogram
plot_histogram(results.get_counts(circuits[0]))

# Show circuit
# circuit_drawer(qc)