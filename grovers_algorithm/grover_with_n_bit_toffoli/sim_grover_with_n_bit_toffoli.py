# import timing to get execution time
import sys
sys.path.append('../')
import timing

from qiskit import QuantumProgram
from qiskit.tools.visualization import plot_histogram, plot_circuit
from math import pi

backend = "local_qasm_simulator"

qp = QuantumProgram()

n = 8  # must be >= 2

ctrl = qp.create_quantum_register('ctrl', n)
anc = qp.create_quantum_register('anc', n-1)
tgt = qp.create_quantum_register('tgt', 1)
c = qp.create_classical_register('c', n+1)

circuits = ['qc']
qc = qp.create_circuit(circuits[0], [ctrl, anc, tgt], [c])

# Create superposition
for ind in range(n):
    qc.h(ctrl[ind])
qc.h(tgt[0])


# Oracle
# compute
qc.ccx(ctrl[0], ctrl[1], anc[0])
for i in range(2, n):
    qc.ccx(ctrl[i], anc[i-2], anc[i-1])

# CZ
qc.h(tgt[0])
qc.cx(anc[n-2], tgt[0])
qc.h(tgt[0])

# uncompute
for i in range(n-1, 1, -1):
    qc.ccx(ctrl[i], anc[i-2], anc[i-1])
qc.ccx(ctrl[0], ctrl[1], anc[0])  


## Diffusion operator
for ind in range(n):
    qc.h(ctrl[ind])
qc.h(tgt[0])

for ind in range(n):
    qc.x(ctrl[ind])
qc.x(tgt[0])

## Oracle
# compute
qc.ccx(ctrl[0], ctrl[1], anc[0])
for i in range(2, n):
    qc.ccx(ctrl[i], anc[i-2], anc[i-1])

# CZ
qc.h(tgt[0])
qc.cx(anc[n-2], tgt[0])
qc.h(tgt[0])

# uncompute
for i in range(n-1, 1, -1):
    qc.ccx(ctrl[i], anc[i-2], anc[i-1])
qc.ccx(ctrl[0], ctrl[1], anc[0])  

for ind in range(n):
    qc.x(ctrl[ind])
qc.x(tgt[0])

for ind in range(n):
    qc.h(ctrl[ind])
qc.h(tgt[0])

# Measurement
for ind in range(n):
    qc.measure(ctrl[ind], c[ind])
qc.measure(tgt[0], c[n])

# Execution
results = qp.execute(circuits, backend=backend, shots=8192, seed=1, timeout=1000) 

# Show result
# data = results.get_counts(circuits[0])
# plot_histogram(data)
# plot_circuit(qc)