from qiskit import QuantumProgram
from qiskit.tools.visualization import plot_histogram, circuit_drawer, plot_circuit

qp = QuantumProgram()

nq = 2  # number of qubits
q = qp.create_quantum_register("q", nq)
c = qp.create_classical_register("c", nq)

circuits = ['testQ']
testQ = qp.create_circuit(circuits[0], [q], [c])

testQ.h(q[0])
testQ.cx(q[0],q[1])

testQ.measure(q[0], c[0])
testQ.measure(q[1], c[1])

results = qp.execute(circuits, backend='local_qasm_simulator', shots=1024, seed=1) 

plot_histogram(results.get_counts(circuits[0]))
#circuit_drawer(testQ)
plot_circuit(testQ)