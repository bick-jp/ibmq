import getpass, time
from qiskit import ClassicalRegister, QuantumRegister
from qiskit import QuantumCircuit,  available_backends, execute, register, get_backend
from math import pi
from qiskit.tools.visualization import plot_histogram, plot_circuit

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

backend = "ibmqx4"
print("Backend is " + backend)

q = QuantumRegister(3)
c = ClassicalRegister(3)
qc = QuantumCircuit(q, c)

# Create superposition
qc.h(q[0])
qc.h(q[1])
qc.h(q[2])

# Grover iteration
iteration = 2
for num in range(iteration):
    # Oracle
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

    # Diffusion operator
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
qc.measure(q, c)

# Execution
job_exp = execute(qc, backend=backend, shots=1024, max_credits=3)

lapse = 0
interval = 10
while not job_exp.done:
    print('Status @ {} seconds'.format(interval * lapse))
    print(job_exp.status)
    time.sleep(interval)
    lapse += 1
print(job_exp.status)

# Show result
plot_histogram(job_exp.result().get_counts(qc))
# plot_circuit(qc)