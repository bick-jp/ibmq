from qiskit import QuantumProgram
from qiskit.tools.visualization import plot_histogram, circuit_drawer

# import original gates
import sys
sys.path.append('../../')
from original_gates_for_simulator import c6z


qp = QuantumProgram()

nq = 7  # number of qubits
q = qp.create_quantum_register("q", nq)
c = qp.create_classical_register("c", nq)

circuits = ['qc']
qc = qp.create_circuit(circuits[0], [q], [c])

# Create uniform superposition
for ind in range(nq):
    qc.h(q[ind])

# Grover iteration
for num in range(6):
    # Oracle
    qc.c6z(q[0], q[1], q[2], q[3], q[4], q[5], q[6])

    # Diffusion operator
    for ind in range(nq):
        qc.h(q[ind])
    for ind in range(nq):
        qc.x(q[ind])
    qc.c6z(q[0], q[1], q[2], q[3], q[4], q[5], q[6])
    for ind in range(nq):
        qc.x(q[ind])
    for ind in range(nq):
        qc.h(q[ind])

# Measurement
for ind in range(nq):
    qc.measure(q[ind], c[ind])

# Execution
results = qp.execute(circuits, backend='local_qasm_simulator', shots=8192, seed=1, timeout=300) 

# Show result as histogram
plot_histogram(results.get_counts(circuits[0]))

# Show circuit
# circuit_drawer(qc)