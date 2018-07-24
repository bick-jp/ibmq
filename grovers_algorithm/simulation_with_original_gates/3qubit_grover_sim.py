# import timing to get execution time
import sys
sys.path.append('../')
import timing

from qiskit import QuantumProgram
from qiskit.tools.visualization import plot_histogram, plot_circuit

# import original gate
import sys
sys.path.append('../../')
from original_gates_for_simulator import ccz

backend = "local_qasm_simulator"

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

# Grover iteration
iteration = 2
for num in range(iteration):
    # Oracle
    qc.ccz(q[2], q[1], q[0])

    # Diffusion operator
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
results = qp.execute(circuits, backend=backend, shots=8192, seed=1) 

# Show result
# data = results.get_counts(circuits[0])
# plot_histogram(data)
# plot_circuit(qc)