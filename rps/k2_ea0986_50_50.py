import getpass, time
from qiskit import ClassicalRegister, QuantumRegister, QuantumProgram
from qiskit import QuantumCircuit,  available_backends, execute, register, get_backend
from math import pi

# import basic plot tools
from qiskit.tools.visualization import plot_histogram, circuit_drawer, plot_circuit

backend = "local_qasm_simulator"
print("The best backend is " + backend)

qp = QuantumProgram()

nq = 2  # number of qubits
q = qp.create_quantum_register("q", nq)
c = qp.create_classical_register("c", nq)

circuits = ['qc']
qc = qp.create_circuit(circuits[0], [q], [c])

qc.u3(2.5028,0,0,q[0])
qc.u3(1.5694,0,0,q[1])

qc.u1((-pi),q[0])
qc.u3(-2.5028,0,0,q[0])
qc.u3(-1.5694-(pi/2),0,0,q[1])
qc.cx(q[0],q[1])
qc.u3(2.5028,0,0,q[0])
qc.u3(1.5694+(pi/2),0,0,q[1])

qc.u1((-pi),q[0])
qc.u3(-2.5028,0,0,q[0])
qc.u3(-1.5694-(pi/2),0,0,q[1])
qc.cx(q[0],q[1])
qc.u3(2.5028,0,0,q[0])
qc.u3(1.5694+(pi/2),0,0,q[1])

# Measurement
qc.measure(q[0], c[0])
qc.measure(q[1], c[1])

# Execution
results = qp.execute(circuits, backend='local_qasm_simulator', shots=8192, seed=1) 

# Show result as histogram
data = results.get_counts(circuits[0])
plot_histogram(data)

# Keita Memo
# I don't know why but circuit_drawer does not work correctly.
# So I use plot_circuit instead.
# circuit_drawer(qc)
# plot_circuit(qc)