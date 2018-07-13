import getpass, time
from qiskit import ClassicalRegister, QuantumRegister, QuantumProgram
from qiskit import QuantumCircuit,  available_backends, execute, register, get_backend
from math import pi

# import basic plot tools
from qiskit.tools.visualization import plot_histogram, circuit_drawer, plot_circuit

qp = QuantumProgram()

nq = 5  # number of qubits
q = qp.create_quantum_register("q", nq)
c = qp.create_classical_register("c", nq)

circuits = ['testQ']
testQ = qp.create_circuit(circuits[0], [q], [c])

# Apply H gate
testQ.h(q[0])
testQ.h(q[1])
testQ.h(q[2])
testQ.h(q[3])
testQ.h(q[4])

for num in range(4):
	########## CCCCZ Start #########

	##### CCCX #####
	testQ.h(q[1])
	## CCCZ start, tgt=1, ctl=2, 3, 4 ##
	# CCX
	testQ.h(q[2]) 
	testQ.cx(q[3],q[2])
	testQ.tdg(q[2])
	testQ.cx(q[4],q[2])
	testQ.t(q[2])
	testQ.cx(q[3],q[2])
	testQ.tdg(q[2])
	testQ.cx(q[4],q[2])
	testQ.t(q[2])
	testQ.tdg(q[3])
	testQ.h(q[2])
	testQ.h(q[3])
	testQ.h(q[4])
	testQ.cx(q[3],q[4])
	testQ.h(q[3])
	testQ.h(q[4])
	testQ.tdg(q[3])
	testQ.h(q[3])
	testQ.h(q[4])
	testQ.cx(q[3],q[4])
	testQ.h(q[3])
	testQ.h(q[4])
	testQ.s(q[3])
	testQ.t(q[4])

	# CZ^(-1/2)
	testQ.cx(q[2],q[1])
	testQ.t(q[1])
	testQ.cx(q[2],q[1])
	testQ.tdg(q[1])
	testQ.tdg(q[2])

	# CCX
	testQ.h(q[2])
	testQ.cx(q[3],q[2])
	testQ.tdg(q[2])
	testQ.cx(q[4],q[2])
	testQ.t(q[2])
	testQ.cx(q[3],q[2])
	testQ.tdg(q[2])
	testQ.cx(q[4],q[2])
	testQ.t(q[2])
	testQ.tdg(q[3])
	testQ.h(q[2])
	testQ.h(q[3])
	testQ.h(q[4])
	testQ.cx(q[3],q[4])
	testQ.h(q[3])
	testQ.h(q[4])
	testQ.tdg(q[3])
	testQ.h(q[3])
	testQ.h(q[4])
	testQ.cx(q[3],q[4])
	testQ.h(q[3])
	testQ.h(q[4])
	testQ.s(q[3])
	testQ.t(q[4])

	# CZ^(1/2)
	testQ.cx(q[2],q[1])
	testQ.tdg(q[1])
	testQ.cx(q[2],q[1])
	testQ.t(q[1])
	testQ.t(q[2])

	# CX
	testQ.h(q[3])
	testQ.h(q[4])
	testQ.cx(q[3],q[4])
	testQ.h(q[3])
	testQ.h(q[4])

	# CZ^(-1/4)
	## Swap
	testQ.cx(q[2],q[1])
	testQ.h(q[1])
	testQ.h(q[2])
	testQ.cx(q[2],q[1])
	testQ.h(q[1])
	testQ.h(q[2])
	testQ.cx(q[2],q[1])

	## CZ^(-1/4)
	testQ.cx(q[3],q[2])
	testQ.u1((pi/8), q[2])
	testQ.cx(q[3],q[2])
	testQ.u1((-pi/8), q[2])
	testQ.u1((-pi/8), q[3])

	# CX
	testQ.h(q[3])
	testQ.h(q[4])
	testQ.cx(q[3],q[4])
	testQ.h(q[3])
	testQ.h(q[4])

	## CZ^(1/4)
	testQ.cx(q[3],q[2])
	testQ.u1((-pi/8), q[2])
	testQ.cx(q[3],q[2])
	testQ.u1((pi/8), q[2])
	testQ.u1((pi/8), q[3])

	## CZ^(1/4)
	testQ.cx(q[4],q[2])
	testQ.u1((-pi/8), q[2])
	testQ.cx(q[4],q[2])
	testQ.u1((pi/8), q[2])
	testQ.u1((pi/8), q[4])

	## Swap
	testQ.cx(q[2],q[1])
	testQ.h(q[1])
	testQ.h(q[2])
	testQ.cx(q[2],q[1])
	testQ.h(q[1])
	testQ.h(q[2])
	testQ.cx(q[2],q[1])
	## CCCZ end ##

	testQ.h(q[1])
	##### CCCX end#####

	# CZ^-1/2 #
	testQ.cx(q[1],q[0])
	testQ.t(q[0])
	testQ.cx(q[1],q[0])
	testQ.tdg(q[0])
	testQ.tdg(q[1])

	##### CCCX #####
	testQ.h(q[1])
	## CCCZ start, tgt=1, ctl=2, 3, 4 ##
	# CCX
	testQ.h(q[2]) 
	testQ.cx(q[3],q[2])
	testQ.tdg(q[2])
	testQ.cx(q[4],q[2])
	testQ.t(q[2])
	testQ.cx(q[3],q[2])
	testQ.tdg(q[2])
	testQ.cx(q[4],q[2])
	testQ.t(q[2])
	testQ.tdg(q[3])
	testQ.h(q[2])
	testQ.h(q[3])
	testQ.h(q[4])
	testQ.cx(q[3],q[4])
	testQ.h(q[3])
	testQ.h(q[4])
	testQ.tdg(q[3])
	testQ.h(q[3])
	testQ.h(q[4])
	testQ.cx(q[3],q[4])
	testQ.h(q[3])
	testQ.h(q[4])
	testQ.s(q[3])
	testQ.t(q[4])

	# CZ^(-1/2)
	testQ.cx(q[2],q[1])
	testQ.t(q[1])
	testQ.cx(q[2],q[1])
	testQ.tdg(q[1])
	testQ.tdg(q[2])

	# CCX
	testQ.h(q[2])
	testQ.cx(q[3],q[2])
	testQ.tdg(q[2])
	testQ.cx(q[4],q[2])
	testQ.t(q[2])
	testQ.cx(q[3],q[2])
	testQ.tdg(q[2])
	testQ.cx(q[4],q[2])
	testQ.t(q[2])
	testQ.tdg(q[3])
	testQ.h(q[2])
	testQ.h(q[3])
	testQ.h(q[4])
	testQ.cx(q[3],q[4])
	testQ.h(q[3])
	testQ.h(q[4])
	testQ.tdg(q[3])
	testQ.h(q[3])
	testQ.h(q[4])
	testQ.cx(q[3],q[4])
	testQ.h(q[3])
	testQ.h(q[4])
	testQ.s(q[3])
	testQ.t(q[4])

	# CZ^(1/2)
	testQ.cx(q[2],q[1])
	testQ.tdg(q[1])
	testQ.cx(q[2],q[1])
	testQ.t(q[1])
	testQ.t(q[2])

	# CX
	testQ.h(q[3])
	testQ.h(q[4])
	testQ.cx(q[3],q[4])
	testQ.h(q[3])
	testQ.h(q[4])

	# CZ^(-1/4)
	## Swap
	testQ.cx(q[2],q[1])
	testQ.h(q[1])
	testQ.h(q[2])
	testQ.cx(q[2],q[1])
	testQ.h(q[1])
	testQ.h(q[2])
	testQ.cx(q[2],q[1])

	## CZ^(-1/4)
	testQ.cx(q[3],q[2])
	testQ.u1((pi/8), q[2])
	testQ.cx(q[3],q[2])
	testQ.u1((-pi/8), q[2])
	testQ.u1((-pi/8), q[3])

	# CX
	testQ.h(q[3])
	testQ.h(q[4])
	testQ.cx(q[3],q[4])
	testQ.h(q[3])
	testQ.h(q[4])

	## CZ^(1/4)
	testQ.cx(q[3],q[2])
	testQ.u1((-pi/8), q[2])
	testQ.cx(q[3],q[2])
	testQ.u1((pi/8), q[2])
	testQ.u1((pi/8), q[3])

	## CZ^(1/4)
	testQ.cx(q[4],q[2])
	testQ.u1((-pi/8), q[2])
	testQ.cx(q[4],q[2])
	testQ.u1((pi/8), q[2])
	testQ.u1((pi/8), q[4])

	## Swap
	testQ.cx(q[2],q[1])
	testQ.h(q[1])
	testQ.h(q[2])
	testQ.cx(q[2],q[1])
	testQ.h(q[1])
	testQ.h(q[2])
	testQ.cx(q[2],q[1])
	## CCCZ end ##

	testQ.h(q[1])
	##### CCCX end#####

	# CZ^1/2 #
	testQ.cx(q[1],q[0])
	testQ.tdg(q[0])
	testQ.cx(q[1],q[0])
	testQ.t(q[0])
	testQ.t(q[1])

	# CCX
	testQ.h(q[2]) 
	testQ.cx(q[3],q[2])
	testQ.tdg(q[2])
	testQ.cx(q[4],q[2])
	testQ.t(q[2])
	testQ.cx(q[3],q[2])
	testQ.tdg(q[2])
	testQ.cx(q[4],q[2])
	testQ.t(q[2])
	testQ.tdg(q[3])
	testQ.h(q[2])
	testQ.h(q[3])
	testQ.h(q[4])
	testQ.cx(q[3],q[4])
	testQ.h(q[3])
	testQ.h(q[4])
	testQ.tdg(q[3])
	testQ.h(q[3])
	testQ.h(q[4])
	testQ.cx(q[3],q[4])
	testQ.h(q[3])
	testQ.h(q[4])
	testQ.s(q[3])
	testQ.t(q[4])

	## CZ^(-1/4)
	testQ.cx(q[2],q[0])
	testQ.u1((pi/8), q[0])
	testQ.cx(q[2],q[0])
	testQ.u1((-pi/8), q[0])
	testQ.u1((-pi/8), q[2])

	# CCX
	testQ.h(q[2]) 
	testQ.cx(q[3],q[2])
	testQ.tdg(q[2])
	testQ.cx(q[4],q[2])
	testQ.t(q[2])
	testQ.cx(q[3],q[2])
	testQ.tdg(q[2])
	testQ.cx(q[4],q[2])
	testQ.t(q[2])
	testQ.tdg(q[3])
	testQ.h(q[2])
	testQ.h(q[3])
	testQ.h(q[4])
	testQ.cx(q[3],q[4])
	testQ.h(q[3])
	testQ.h(q[4])
	testQ.tdg(q[3])
	testQ.h(q[3])
	testQ.h(q[4])
	testQ.cx(q[3],q[4])
	testQ.h(q[3])
	testQ.h(q[4])
	testQ.s(q[3])
	testQ.t(q[4])

	## CZ^(1/4)
	testQ.cx(q[2],q[0])
	testQ.u1((-pi/8), q[0])
	testQ.cx(q[2],q[0])
	testQ.u1((pi/8), q[0])
	testQ.u1((pi/8), q[2])

	# CX
	testQ.h(q[3])
	testQ.h(q[4])
	testQ.cx(q[3],q[4])
	testQ.h(q[3])
	testQ.h(q[4])


	## Apply CZ^-1/8 gate, ctl=3, tgt=0 ##
	# SWAP 0 and 2
	testQ.cx(q[2],q[0])
	testQ.h(q[0])
	testQ.h(q[2])
	testQ.cx(q[2],q[0])
	testQ.h(q[0])
	testQ.h(q[2])
	testQ.cx(q[2],q[0])

	## CZ^(-1/8)
	testQ.cx(q[3],q[2])
	testQ.u1((pi/16), q[2])
	testQ.cx(q[3],q[2])
	testQ.u1((-pi/16), q[2])
	testQ.u1((-pi/16), q[3])

	# CX
	testQ.h(q[3])
	testQ.h(q[4])
	testQ.cx(q[3],q[4])
	testQ.h(q[3])
	testQ.h(q[4])

	## CZ^(1/8)
	testQ.cx(q[3],q[2])
	testQ.u1((-pi/16), q[2])
	testQ.cx(q[3],q[2])
	testQ.u1((pi/16), q[2])
	testQ.u1((pi/16), q[3])

	## CZ^(1/8)
	testQ.cx(q[4],q[2])
	testQ.u1((-pi/16), q[2])
	testQ.cx(q[4],q[2])
	testQ.u1((pi/16), q[2])
	testQ.u1((pi/16), q[4])

	# SWAP 0 and 2
	testQ.cx(q[2],q[0])
	testQ.h(q[0])
	testQ.h(q[2])
	testQ.cx(q[2],q[0])
	testQ.h(q[0])
	testQ.h(q[2])
	testQ.cx(q[2],q[0])

	# CCCCZ End ########################

	##### Diffustion #####
	testQ.h(q[0])
	testQ.h(q[1])
	testQ.h(q[2])
	testQ.h(q[3])
	testQ.h(q[4])

	testQ.x(q[0])
	testQ.x(q[1])
	testQ.x(q[2])
	testQ.x(q[3])
	testQ.x(q[4])

	########## CCCCZ Start #########

	##### CCCX #####
	testQ.h(q[1])
	## CCCZ start, tgt=1, ctl=2, 3, 4 ##
	# CCX
	testQ.h(q[2]) 
	testQ.cx(q[3],q[2])
	testQ.tdg(q[2])
	testQ.cx(q[4],q[2])
	testQ.t(q[2])
	testQ.cx(q[3],q[2])
	testQ.tdg(q[2])
	testQ.cx(q[4],q[2])
	testQ.t(q[2])
	testQ.tdg(q[3])
	testQ.h(q[2])
	testQ.h(q[3])
	testQ.h(q[4])
	testQ.cx(q[3],q[4])
	testQ.h(q[3])
	testQ.h(q[4])
	testQ.tdg(q[3])
	testQ.h(q[3])
	testQ.h(q[4])
	testQ.cx(q[3],q[4])
	testQ.h(q[3])
	testQ.h(q[4])
	testQ.s(q[3])
	testQ.t(q[4])

	# CZ^(-1/2)
	testQ.cx(q[2],q[1])
	testQ.t(q[1])
	testQ.cx(q[2],q[1])
	testQ.tdg(q[1])
	testQ.tdg(q[2])

	# CCX
	testQ.h(q[2])
	testQ.cx(q[3],q[2])
	testQ.tdg(q[2])
	testQ.cx(q[4],q[2])
	testQ.t(q[2])
	testQ.cx(q[3],q[2])
	testQ.tdg(q[2])
	testQ.cx(q[4],q[2])
	testQ.t(q[2])
	testQ.tdg(q[3])
	testQ.h(q[2])
	testQ.h(q[3])
	testQ.h(q[4])
	testQ.cx(q[3],q[4])
	testQ.h(q[3])
	testQ.h(q[4])
	testQ.tdg(q[3])
	testQ.h(q[3])
	testQ.h(q[4])
	testQ.cx(q[3],q[4])
	testQ.h(q[3])
	testQ.h(q[4])
	testQ.s(q[3])
	testQ.t(q[4])

	# CZ^(1/2)
	testQ.cx(q[2],q[1])
	testQ.tdg(q[1])
	testQ.cx(q[2],q[1])
	testQ.t(q[1])
	testQ.t(q[2])

	# CX
	testQ.h(q[3])
	testQ.h(q[4])
	testQ.cx(q[3],q[4])
	testQ.h(q[3])
	testQ.h(q[4])

	# CZ^(-1/4)
	## Swap
	testQ.cx(q[2],q[1])
	testQ.h(q[1])
	testQ.h(q[2])
	testQ.cx(q[2],q[1])
	testQ.h(q[1])
	testQ.h(q[2])
	testQ.cx(q[2],q[1])

	## CZ^(-1/4)
	testQ.cx(q[3],q[2])
	testQ.u1((pi/8), q[2])
	testQ.cx(q[3],q[2])
	testQ.u1((-pi/8), q[2])
	testQ.u1((-pi/8), q[3])

	# CX
	testQ.h(q[3])
	testQ.h(q[4])
	testQ.cx(q[3],q[4])
	testQ.h(q[3])
	testQ.h(q[4])

	## CZ^(1/4)
	testQ.cx(q[3],q[2])
	testQ.u1((-pi/8), q[2])
	testQ.cx(q[3],q[2])
	testQ.u1((pi/8), q[2])
	testQ.u1((pi/8), q[3])

	## CZ^(1/4)
	testQ.cx(q[4],q[2])
	testQ.u1((-pi/8), q[2])
	testQ.cx(q[4],q[2])
	testQ.u1((pi/8), q[2])
	testQ.u1((pi/8), q[4])

	## Swap
	testQ.cx(q[2],q[1])
	testQ.h(q[1])
	testQ.h(q[2])
	testQ.cx(q[2],q[1])
	testQ.h(q[1])
	testQ.h(q[2])
	testQ.cx(q[2],q[1])
	## CCCZ end ##

	testQ.h(q[1])
	##### CCCX end#####

	# CZ^-1/2 #
	testQ.cx(q[1],q[0])
	testQ.t(q[0])
	testQ.cx(q[1],q[0])
	testQ.tdg(q[0])
	testQ.tdg(q[1])

	##### CCCX #####
	testQ.h(q[1])
	## CCCZ start, tgt=1, ctl=2, 3, 4 ##
	# CCX
	testQ.h(q[2]) 
	testQ.cx(q[3],q[2])
	testQ.tdg(q[2])
	testQ.cx(q[4],q[2])
	testQ.t(q[2])
	testQ.cx(q[3],q[2])
	testQ.tdg(q[2])
	testQ.cx(q[4],q[2])
	testQ.t(q[2])
	testQ.tdg(q[3])
	testQ.h(q[2])
	testQ.h(q[3])
	testQ.h(q[4])
	testQ.cx(q[3],q[4])
	testQ.h(q[3])
	testQ.h(q[4])
	testQ.tdg(q[3])
	testQ.h(q[3])
	testQ.h(q[4])
	testQ.cx(q[3],q[4])
	testQ.h(q[3])
	testQ.h(q[4])
	testQ.s(q[3])
	testQ.t(q[4])

	# CZ^(-1/2)
	testQ.cx(q[2],q[1])
	testQ.t(q[1])
	testQ.cx(q[2],q[1])
	testQ.tdg(q[1])
	testQ.tdg(q[2])

	# CCX
	testQ.h(q[2])
	testQ.cx(q[3],q[2])
	testQ.tdg(q[2])
	testQ.cx(q[4],q[2])
	testQ.t(q[2])
	testQ.cx(q[3],q[2])
	testQ.tdg(q[2])
	testQ.cx(q[4],q[2])
	testQ.t(q[2])
	testQ.tdg(q[3])
	testQ.h(q[2])
	testQ.h(q[3])
	testQ.h(q[4])
	testQ.cx(q[3],q[4])
	testQ.h(q[3])
	testQ.h(q[4])
	testQ.tdg(q[3])
	testQ.h(q[3])
	testQ.h(q[4])
	testQ.cx(q[3],q[4])
	testQ.h(q[3])
	testQ.h(q[4])
	testQ.s(q[3])
	testQ.t(q[4])

	# CZ^(1/2)
	testQ.cx(q[2],q[1])
	testQ.tdg(q[1])
	testQ.cx(q[2],q[1])
	testQ.t(q[1])
	testQ.t(q[2])

	# CX
	testQ.h(q[3])
	testQ.h(q[4])
	testQ.cx(q[3],q[4])
	testQ.h(q[3])
	testQ.h(q[4])

	# CZ^(-1/4)
	## Swap
	testQ.cx(q[2],q[1])
	testQ.h(q[1])
	testQ.h(q[2])
	testQ.cx(q[2],q[1])
	testQ.h(q[1])
	testQ.h(q[2])
	testQ.cx(q[2],q[1])

	## CZ^(-1/4)
	testQ.cx(q[3],q[2])
	testQ.u1((pi/8), q[2])
	testQ.cx(q[3],q[2])
	testQ.u1((-pi/8), q[2])
	testQ.u1((-pi/8), q[3])

	# CX
	testQ.h(q[3])
	testQ.h(q[4])
	testQ.cx(q[3],q[4])
	testQ.h(q[3])
	testQ.h(q[4])

	## CZ^(1/4)
	testQ.cx(q[3],q[2])
	testQ.u1((-pi/8), q[2])
	testQ.cx(q[3],q[2])
	testQ.u1((pi/8), q[2])
	testQ.u1((pi/8), q[3])

	## CZ^(1/4)
	testQ.cx(q[4],q[2])
	testQ.u1((-pi/8), q[2])
	testQ.cx(q[4],q[2])
	testQ.u1((pi/8), q[2])
	testQ.u1((pi/8), q[4])

	## Swap
	testQ.cx(q[2],q[1])
	testQ.h(q[1])
	testQ.h(q[2])
	testQ.cx(q[2],q[1])
	testQ.h(q[1])
	testQ.h(q[2])
	testQ.cx(q[2],q[1])
	## CCCZ end ##

	testQ.h(q[1])
	##### CCCX end#####

	# CZ^1/2 #
	testQ.cx(q[1],q[0])
	testQ.tdg(q[0])
	testQ.cx(q[1],q[0])
	testQ.t(q[0])
	testQ.t(q[1])

	# CCX
	testQ.h(q[2]) 
	testQ.cx(q[3],q[2])
	testQ.tdg(q[2])
	testQ.cx(q[4],q[2])
	testQ.t(q[2])
	testQ.cx(q[3],q[2])
	testQ.tdg(q[2])
	testQ.cx(q[4],q[2])
	testQ.t(q[2])
	testQ.tdg(q[3])
	testQ.h(q[2])
	testQ.h(q[3])
	testQ.h(q[4])
	testQ.cx(q[3],q[4])
	testQ.h(q[3])
	testQ.h(q[4])
	testQ.tdg(q[3])
	testQ.h(q[3])
	testQ.h(q[4])
	testQ.cx(q[3],q[4])
	testQ.h(q[3])
	testQ.h(q[4])
	testQ.s(q[3])
	testQ.t(q[4])

	## CZ^(-1/4)
	testQ.cx(q[2],q[0])
	testQ.u1((pi/8), q[0])
	testQ.cx(q[2],q[0])
	testQ.u1((-pi/8), q[0])
	testQ.u1((-pi/8), q[2])

	# CCX
	testQ.h(q[2]) 
	testQ.cx(q[3],q[2])
	testQ.tdg(q[2])
	testQ.cx(q[4],q[2])
	testQ.t(q[2])
	testQ.cx(q[3],q[2])
	testQ.tdg(q[2])
	testQ.cx(q[4],q[2])
	testQ.t(q[2])
	testQ.tdg(q[3])
	testQ.h(q[2])
	testQ.h(q[3])
	testQ.h(q[4])
	testQ.cx(q[3],q[4])
	testQ.h(q[3])
	testQ.h(q[4])
	testQ.tdg(q[3])
	testQ.h(q[3])
	testQ.h(q[4])
	testQ.cx(q[3],q[4])
	testQ.h(q[3])
	testQ.h(q[4])
	testQ.s(q[3])
	testQ.t(q[4])

	## CZ^(1/4)
	testQ.cx(q[2],q[0])
	testQ.u1((-pi/8), q[0])
	testQ.cx(q[2],q[0])
	testQ.u1((pi/8), q[0])
	testQ.u1((pi/8), q[2])

	# CX
	testQ.h(q[3])
	testQ.h(q[4])
	testQ.cx(q[3],q[4])
	testQ.h(q[3])
	testQ.h(q[4])


	## Apply CZ^-1/8 gate, ctl=3, tgt=0 ##
	# SWAP 0 and 2
	testQ.cx(q[2],q[0])
	testQ.h(q[0])
	testQ.h(q[2])
	testQ.cx(q[2],q[0])
	testQ.h(q[0])
	testQ.h(q[2])
	testQ.cx(q[2],q[0])

	## CZ^(-1/8)
	testQ.cx(q[3],q[2])
	testQ.u1((pi/16), q[2])
	testQ.cx(q[3],q[2])
	testQ.u1((-pi/16), q[2])
	testQ.u1((-pi/16), q[3])

	# CX
	testQ.h(q[3])
	testQ.h(q[4])
	testQ.cx(q[3],q[4])
	testQ.h(q[3])
	testQ.h(q[4])

	## CZ^(1/8)
	testQ.cx(q[3],q[2])
	testQ.u1((-pi/16), q[2])
	testQ.cx(q[3],q[2])
	testQ.u1((pi/16), q[2])
	testQ.u1((pi/16), q[3])

	## CZ^(1/8)
	testQ.cx(q[4],q[2])
	testQ.u1((-pi/16), q[2])
	testQ.cx(q[4],q[2])
	testQ.u1((pi/16), q[2])
	testQ.u1((pi/16), q[4])

	# SWAP 0 and 2
	testQ.cx(q[2],q[0])
	testQ.h(q[0])
	testQ.h(q[2])
	testQ.cx(q[2],q[0])
	testQ.h(q[0])
	testQ.h(q[2])
	testQ.cx(q[2],q[0])

	# CCCCZ End ########################

	testQ.x(q[0])
	testQ.x(q[1])
	testQ.x(q[2])
	testQ.x(q[3])
	testQ.x(q[4])

	testQ.h(q[0])
	testQ.h(q[1])
	testQ.h(q[2])
	testQ.h(q[3])
	testQ.h(q[4])

	##### Diffusion end #####


# Measurement
testQ.measure(q[0], c[0])
testQ.measure(q[1], c[1])
testQ.measure(q[2], c[2])
testQ.measure(q[3], c[3])
testQ.measure(q[4], c[4])

# Execution
results = qp.execute(circuits, backend='local_qasm_simulator', shots=8192, seed=1) 

# Show result as histogram
plot_histogram(results.get_counts(circuits[0]))