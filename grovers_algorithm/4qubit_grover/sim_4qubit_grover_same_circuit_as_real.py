# import timing to get execution time
import sys
sys.path.append('../')
import timing

from qiskit import QuantumProgram
from qiskit.tools.visualization import plot_histogram, plot_circuit
from math import pi

backend = "local_qasm_simulator"

qp = QuantumProgram()

nq = 5  # number of qubits
q = qp.create_quantum_register("q", nq)
c = qp.create_classical_register("c", nq)

circuits = ['qc']
qc = qp.create_circuit(circuits[0], [q], [c])

# Define oracle
def apply_cccz():
	# CCX
	qc.h(q[2]) 
	qc.cx(q[3],q[2])
	qc.tdg(q[2])
	qc.cx(q[4],q[2])
	qc.t(q[2])
	qc.cx(q[3],q[2])
	qc.tdg(q[2])
	qc.cx(q[4],q[2])
	qc.t(q[2])
	qc.tdg(q[3])
	qc.h(q[2])
	qc.h(q[3])
	qc.h(q[4])
	qc.cx(q[3],q[4])
	qc.h(q[3])
	qc.h(q[4])
	qc.tdg(q[3])
	qc.h(q[3])
	qc.h(q[4])
	qc.cx(q[3],q[4])
	qc.h(q[3])
	qc.h(q[4])
	qc.s(q[3])
	qc.t(q[4])

	# CZ^(-1/2)
	qc.cx(q[2],q[1])
	qc.t(q[1])
	qc.cx(q[2],q[1])
	qc.tdg(q[1])
	qc.tdg(q[2])

	# CCX
	qc.h(q[2])
	qc.cx(q[3],q[2])
	qc.tdg(q[2])
	qc.cx(q[4],q[2])
	qc.t(q[2])
	qc.cx(q[3],q[2])
	qc.tdg(q[2])
	qc.cx(q[4],q[2])
	qc.t(q[2])
	qc.tdg(q[3])
	qc.h(q[2])
	qc.h(q[3])
	qc.h(q[4])
	qc.cx(q[3],q[4])
	qc.h(q[3])
	qc.h(q[4])
	qc.tdg(q[3])
	qc.h(q[3])
	qc.h(q[4])
	qc.cx(q[3],q[4])
	qc.h(q[3])
	qc.h(q[4])
	qc.s(q[3])
	qc.t(q[4])

	# CZ^(1/2)
	qc.cx(q[2],q[1])
	qc.tdg(q[1])
	qc.cx(q[2],q[1])
	qc.t(q[1])
	qc.t(q[2])

	# CX
	qc.h(q[3])
	qc.h(q[4])
	qc.cx(q[3],q[4])
	qc.h(q[3])
	qc.h(q[4])

	# Swap
	qc.cx(q[2],q[1])
	qc.h(q[1])
	qc.h(q[2])
	qc.cx(q[2],q[1])
	qc.h(q[1])
	qc.h(q[2])
	qc.cx(q[2],q[1])

	# CZ^(-1/4)
	qc.cx(q[3],q[2])
	qc.u1((pi/8), q[2])
	qc.cx(q[3],q[2])
	qc.u1((-pi/8), q[2])
	qc.u1((-pi/8), q[3])

	# CX
	qc.h(q[3])
	qc.h(q[4])
	qc.cx(q[3],q[4])
	qc.h(q[3])
	qc.h(q[4])

	# CZ^(1/4)
	qc.cx(q[3],q[2])
	qc.u1((-pi/8), q[2])
	qc.cx(q[3],q[2])
	qc.u1((pi/8), q[2])
	qc.u1((pi/8), q[3])

	# CZ^(1/4)
	qc.cx(q[4],q[2])
	qc.u1((-pi/8), q[2])
	qc.cx(q[4],q[2])
	qc.u1((pi/8), q[2])
	qc.u1((pi/8), q[4])

	# Swap
	qc.cx(q[2],q[1])
	qc.h(q[1])
	qc.h(q[2])
	qc.cx(q[2],q[1])
	qc.h(q[1])
	qc.h(q[2])
	qc.cx(q[2],q[1])


# Create superposition
qc.h(q[1])
qc.h(q[2])
qc.h(q[3])
qc.h(q[4])

# Grover iteration
iteration = 3
for num in range(iteration):
	# Oracle
	apply_cccz()

	# Diffusion operator
	qc.h(q[1])
	qc.h(q[2])
	qc.h(q[3])
	qc.h(q[4])

	qc.x(q[1])
	qc.x(q[2])
	qc.x(q[3])
	qc.x(q[4])

	apply_cccz()

	qc.x(q[1])
	qc.x(q[2])
	qc.x(q[3])
	qc.x(q[4])

	qc.h(q[1])
	qc.h(q[2])
	qc.h(q[3])
	qc.h(q[4])

# Measurement
qc.measure(q[1], c[1])
qc.measure(q[2], c[2])
qc.measure(q[3], c[3])
qc.measure(q[4], c[4])

# Execution
results = qp.execute(circuits, backend=backend, shots=8192, seed=1) 

# Show result
# data = results.get_counts(circuits[0])
# plot_histogram(data)
# plot_circuit(qc)
# print(results.get_data(circuits[0]))