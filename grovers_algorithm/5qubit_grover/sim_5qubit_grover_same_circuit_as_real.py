import getpass, time
from qiskit import ClassicalRegister, QuantumRegister, QuantumProgram
from qiskit import QuantumCircuit,  available_backends, execute, register, get_backend
from math import pi
from qiskit.tools.visualization import plot_histogram, plot_circuit

qp = QuantumProgram()

nq = 5  # number of qubits
q = qp.create_quantum_register("q", nq)
c = qp.create_classical_register("c", nq)

circuits = ['qc']
qc = qp.create_circuit(circuits[0], [q], [c])

## Define oracle and related functions
# CCX: ctl=3 and 4. tgt=2.
def apply_ccx():
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

# CCCX: ctl=2, 3, and 4. tgt=1.
def apply_cccx():
	qc.h(q[1])

	## CCCZ start ##
	# CCX
	apply_ccx()

	# CZ^(-1/2)
	qc.cx(q[2],q[1])
	qc.t(q[1])
	qc.cx(q[2],q[1])
	qc.tdg(q[1])
	qc.tdg(q[2])

	# CCX
	apply_ccx()

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
	## CCCZ end ##

	qc.h(q[1])

# Oracle CCCCZ: ctl=1, 2, 3, and 4. tgt=0.
def apply_ccccz():

	# CCCX
	apply_cccx()

	# CZ^-1/2
	qc.cx(q[1],q[0])
	qc.t(q[0])
	qc.cx(q[1],q[0])
	qc.tdg(q[0])
	qc.tdg(q[1])

	# CCCX
	apply_cccx()

	# CZ^1/2
	qc.cx(q[1],q[0])
	qc.tdg(q[0])
	qc.cx(q[1],q[0])
	qc.t(q[0])
	qc.t(q[1])

	# CCX
	apply_ccx()

	# CZ^(-1/4)
	qc.cx(q[2],q[0])
	qc.u1((pi/8), q[0])
	qc.cx(q[2],q[0])
	qc.u1((-pi/8), q[0])
	qc.u1((-pi/8), q[2])

	# CCX
	apply_ccx()

	# CZ^(1/4)
	qc.cx(q[2],q[0])
	qc.u1((-pi/8), q[0])
	qc.cx(q[2],q[0])
	qc.u1((pi/8), q[0])
	qc.u1((pi/8), q[2])

	# CX
	qc.h(q[3])
	qc.h(q[4])
	qc.cx(q[3],q[4])
	qc.h(q[3])
	qc.h(q[4])


	## Apply CZ^-1/8 gate, ctl=3, tgt=0 ##
	# SWAP 0 and 2
	qc.cx(q[2],q[0])
	qc.h(q[0])
	qc.h(q[2])
	qc.cx(q[2],q[0])
	qc.h(q[0])
	qc.h(q[2])
	qc.cx(q[2],q[0])

	# CZ^(-1/8)
	qc.cx(q[3],q[2])
	qc.u1((pi/16), q[2])
	qc.cx(q[3],q[2])
	qc.u1((-pi/16), q[2])
	qc.u1((-pi/16), q[3])

	# CX
	qc.h(q[3])
	qc.h(q[4])
	qc.cx(q[3],q[4])
	qc.h(q[3])
	qc.h(q[4])

	# CZ^(1/8)
	qc.cx(q[3],q[2])
	qc.u1((-pi/16), q[2])
	qc.cx(q[3],q[2])
	qc.u1((pi/16), q[2])
	qc.u1((pi/16), q[3])

	# CZ^(1/8)
	qc.cx(q[4],q[2])
	qc.u1((-pi/16), q[2])
	qc.cx(q[4],q[2])
	qc.u1((pi/16), q[2])
	qc.u1((pi/16), q[4])

	# SWAP 0 and 2
	qc.cx(q[2],q[0])
	qc.h(q[0])
	qc.h(q[2])
	qc.cx(q[2],q[0])
	qc.h(q[0])
	qc.h(q[2])
	qc.cx(q[2],q[0])


# Create superposition
qc.h(q[0])
qc.h(q[1])
qc.h(q[2])
qc.h(q[3])
qc.h(q[4])

# Grover iteration
iteration = 4
for num in range(iteration):
	# Oracle
	apply_ccccz()

	# Diffustion
	qc.h(q[0])
	qc.h(q[1])
	qc.h(q[2])
	qc.h(q[3])
	qc.h(q[4])

	qc.x(q[0])
	qc.x(q[1])
	qc.x(q[2])
	qc.x(q[3])
	qc.x(q[4])

	apply_ccccz()

	qc.x(q[0])
	qc.x(q[1])
	qc.x(q[2])
	qc.x(q[3])
	qc.x(q[4])

	qc.h(q[0])
	qc.h(q[1])
	qc.h(q[2])
	qc.h(q[3])
	qc.h(q[4])


# Measurement
qc.measure(q[0], c[0])
qc.measure(q[1], c[1])
qc.measure(q[2], c[2])
qc.measure(q[3], c[3])
qc.measure(q[4], c[4])

# Execution
results = qp.execute(circuits, backend='local_qasm_simulator', shots=8192, seed=1) 

# Show result
plot_histogram(results.get_counts(circuits[0]))
# circuit_drawer(qc)