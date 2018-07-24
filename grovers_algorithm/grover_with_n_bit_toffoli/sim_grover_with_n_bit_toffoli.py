# import timing to get execution time
import sys
sys.path.append('../')
import timing

from qiskit import QuantumProgram
from qiskit.tools.visualization import plot_histogram, plot_circuit
from math import pi

backend = "local_qasm_simulator"
timeout = 10000

qp = QuantumProgram()

n = 6 # n-qubit Grover's algorithm. n = k + 1. (+1 is for a target qubit). n must be >= 3.
k = n - 1 # number of control qubits. must be >= 2.

# Step 1: Preparation
ctrl = qp.create_quantum_register('ctrl', k)
anc = qp.create_quantum_register('anc', k-1)
tgt = qp.create_quantum_register('tgt', 1)
c = qp.create_classical_register('c', k+1)

circuits = ['qc']
qc = qp.create_circuit(circuits[0], [ctrl, anc, tgt], [c])

# Create superposition
for ind in range(k):
    qc.h(ctrl[ind])
qc.h(tgt[0])

# Oracle (C^k)Z gate
def oracle():
    # Step 2: Apply CCX gate
    qc.ccx(ctrl[0], ctrl[1], anc[0])
    for i in range(2, k):
        qc.ccx(ctrl[i], anc[i-2], anc[i-1])

    # Step 3: Apply CZ
    qc.h(tgt[0])
    qc.cx(anc[k-2], tgt[0])
    qc.h(tgt[0])

    # Step4: Reversely apply CCX 
    for i in range(k-1, 1, -1):
        qc.ccx(ctrl[i], anc[i-2], anc[i-1])
    qc.ccx(ctrl[0], ctrl[1], anc[0])

# Grover iteration
iteration = 6
for num in range(iteration):
    # Oracle
    oracle()  

    # Diffusion operator
    for ind in range(k):
        qc.h(ctrl[ind])
    qc.h(tgt[0])

    for ind in range(k):
        qc.x(ctrl[ind])
    qc.x(tgt[0])

    oracle()  

    for ind in range(k):
        qc.x(ctrl[ind])
    qc.x(tgt[0])

    for ind in range(k):
        qc.h(ctrl[ind])
    qc.h(tgt[0])

# Measurement
for ind in range(k):
    qc.measure(ctrl[ind], c[ind])
qc.measure(tgt[0], c[k])

# Execution
results = qp.execute(circuits, backend=backend, shots=8192, seed=1, timeout=timeout) 

# Show result
data = results.get_counts(circuits[0])
plot_histogram(data)
# plot_circuit(qc)
# print(results.get_data(circuits[0]))