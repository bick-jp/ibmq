# import timing to get execution time
import sys
sys.path.append('../')
import timing

from qiskit import QuantumProgram
from qiskit.tools.visualization import plot_histogram, circuit_drawer

# import original gates
import sys
sys.path.append('../../')
from original_gates_for_simulator import c5z

backend = "local_qasm_simulator"

qp = QuantumProgram()

nq = 6  # number of qubits
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
    qc.c5z(q[0], q[1], q[2], q[3], q[4], q[5])

    # Diffusion operator
    for ind in range(nq):
        qc.h(q[ind])
    for ind in range(nq):
        qc.x(q[ind])
    qc.c5z(q[0], q[1], q[2], q[3], q[4], q[5])
    for ind in range(nq):
        qc.x(q[ind])
    for ind in range(nq):
        qc.h(q[ind])

# Measurement
for ind in range(nq):
    qc.measure(q[ind], c[ind])

# Execution
results = qp.execute(circuits, backend=backend, shots=8192, seed=1) 

# Show result as histogram
# plot_histogram(results.get_counts(circuits[0]))
# circuit_drawer(qc)