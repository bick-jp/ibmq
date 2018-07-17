# import timing to get execution time
import sys
sys.path.append('../')
import timing

from qiskit import QuantumProgram
from qiskit.tools.visualization import plot_histogram, plot_circuit

# import original gate
import sys
sys.path.append('../../')
from original_gates_for_simulator import cccz

backend = "local_qasm_simulator"

qp = QuantumProgram()

nq = 4  # number of qubits
q = qp.create_quantum_register("q", nq)
c = qp.create_classical_register("c", nq)

circuits = ['qc']
qc = qp.create_circuit(circuits[0], [q], [c])

# Create uniform superposition
for ind in range(nq):
    qc.h(q[ind])

# Grover iteration
for num in range(3):
    # Oracle
    qc.cccz(q[0], q[1], q[2], q[3])

    # Diffusion operator
    for ind in range(nq):
        qc.h(q[ind])
    for ind in range(nq):
        qc.x(q[ind])
    qc.cccz(q[0], q[1], q[2], q[3])
    for ind in range(nq):
        qc.x(q[ind])
    for ind in range(nq):
        qc.h(q[ind])

# Measurement
for ind in range(nq):
    qc.measure(q[ind], c[ind])

# Execution
results = qp.execute(circuits, backend=backend, shots=8192, seed=1) 

# Show result
# plot_histogram(results.get_counts(circuits[0]))
# plot_circuit(qc)