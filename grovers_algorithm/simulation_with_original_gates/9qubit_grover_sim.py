# import timing to get execution time
import sys
sys.path.append('../')
import timing

from qiskit import QuantumProgram
from qiskit.tools.visualization import plot_histogram, circuit_drawer

# import original gates
import sys
sys.path.append('../../')
from original_gates_for_simulator import c8z

backend = "local_qasm_simulator"
timeout = 10000

qp = QuantumProgram()

nq = 9  # number of qubits
q = qp.create_quantum_register("q", nq)
c = qp.create_classical_register("c", nq)

circuits = ['qc']
qc = qp.create_circuit(circuits[0], [q], [c])

# Create uniform superposition
for ind in range(nq):
    qc.h(q[ind])

# Grover iteration
iteration = 17
for num in range(iteration):
    # Oracle
    qc.c8z(q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7], q[8])

    # Diffusion operator
    for ind in range(nq):
        qc.h(q[ind])
    for ind in range(nq):
        qc.x(q[ind])
    qc.c8z(q[0], q[1], q[2], q[3], q[4], q[5], q[6], q[7], q[8])
    for ind in range(nq):
        qc.x(q[ind])
    for ind in range(nq):
        qc.h(q[ind])

# Measurement
for ind in range(nq):
    qc.measure(q[ind], c[ind])

# Execution
results = qp.execute(circuits, backend=backend, shots=8192, seed=1, timeout=timeout) 

# Show result
# plot_histogram(results.get_counts(circuits[0]))
# circuit_drawer(qc)