import getpass, time
from qiskit import ClassicalRegister, QuantumRegister, QuantumProgram
from qiskit import QuantumCircuit,  available_backends, execute, register, get_backend
from math import pi

# import basic plot tools
from qiskit.tools.visualization import plot_histogram, circuit_drawer, plot_circuit

"""
APItoken = getpass.getpass('Please input your token and hit enter: ')
qx_config = {
    "APItoken": APItoken,
    "url":"https://quantumexperience.ng.bluemix.net/api"}

try:
    register(qx_config['APItoken'], qx_config['url'])

    print('\nYou have access to great power!')
    print(available_backends({'local': False, 'simulator': False}))
except: 
    print('Something went wrong.\nDid you enter a correct token?')

def lowest_pending_jobs():
    # Returns the backend with lowest pending jobs.
    list_of_backends = available_backends(
        {'local': False, 'simulator': False})
    device_status = [get_backend(backend).status
                     for backend in list_of_backends]

    best = min([x for x in device_status if x['available'] is True],
               key=lambda x: x['pending_jobs'])
    return best['name']

backend = lowest_pending_jobs()
"""
backend = "local_qasm_simulator"
print("The best backend is " + backend)

qp = QuantumProgram()

nq = 3  # number of qubits
q = qp.create_quantum_register("q", nq)
c = qp.create_classical_register("c", nq)

circuits = ['qc']
qc = qp.create_circuit(circuits[0], [q], [c])

# Apply H gate
qc.h(q[0])
qc.h(q[1])
qc.h(q[2])

### 1st iteration ###
# Oracle to negate |111>
qc.cx(q[1],q[0])
qc.tdg(q[0])
qc.cx(q[2],q[0])
qc.t(q[0])
qc.cx(q[1],q[0])
qc.tdg(q[0])
qc.cx(q[2],q[0])
qc.t(q[0])
qc.t(q[1])
qc.cx(q[2],q[1])
qc.tdg(q[1])
qc.cx(q[2],q[1])
qc.t(q[2])

# Diffusion operator to amplify the probability amplitude of |111>
qc.h(q[0])
qc.h(q[1])
qc.h(q[2])
qc.x(q[0])
qc.x(q[1])
qc.x(q[2])
qc.cx(q[1],q[0])
qc.tdg(q[0])
qc.cx(q[2],q[0])
qc.t(q[0])
qc.cx(q[1],q[0])
qc.tdg(q[0])
qc.cx(q[2],q[0])
qc.t(q[0])
qc.t(q[1])
qc.cx(q[2],q[1])
qc.tdg(q[1])
qc.cx(q[2],q[1])
qc.t(q[2])
qc.x(q[0])
qc.x(q[1])
qc.x(q[2])
qc.h(q[0])
qc.h(q[1])
qc.h(q[2])

### 2nd iteration ###
# Oracle to negate |111>
qc.cx(q[1],q[0])
qc.tdg(q[0])
qc.cx(q[2],q[0])
qc.t(q[0])
qc.cx(q[1],q[0])
qc.tdg(q[0])
qc.cx(q[2],q[0])
qc.t(q[0])
qc.t(q[1])
qc.cx(q[2],q[1])
qc.tdg(q[1])
qc.cx(q[2],q[1])
qc.t(q[2])

# Diffusion operator to amplify the probability amplitude of |111>
qc.h(q[0])
qc.h(q[1])
qc.h(q[2])
qc.x(q[0])
qc.x(q[1])
qc.x(q[2])
qc.cx(q[1],q[0])
qc.tdg(q[0])
qc.cx(q[2],q[0])
qc.t(q[0])
qc.cx(q[1],q[0])
qc.tdg(q[0])
qc.cx(q[2],q[0])
qc.t(q[0])
qc.t(q[1])
qc.cx(q[2],q[1])
qc.tdg(q[1])
qc.cx(q[2],q[1])
qc.t(q[2])
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
results = qp.execute(circuits, backend='local_qasm_simulator', shots=8192, seed=1) 

# Show result as histogram
data = results.get_counts(circuits[0])
plot_histogram(data)

# Keita Memo
# I don't know why but circuit_drawer does not work correctly.
# So I use plot_circuit instead.
# circuit_drawer(qc)
plot_circuit(qc)