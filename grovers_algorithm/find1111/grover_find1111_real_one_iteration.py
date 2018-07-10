import getpass, time
from qiskit import ClassicalRegister, QuantumRegister, QuantumProgram
from qiskit import QuantumCircuit,  available_backends, execute, register, get_backend
from math import pi

# import basic plot tools
from qiskit.tools.visualization import plot_histogram, circuit_drawer, plot_circuit

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
    """Returns the backend with lowest pending jobs."""
    list_of_backends = available_backends(
        {'local': False, 'simulator': False})
    device_status = [get_backend(backend).status
                     for backend in list_of_backends]

    best = min([x for x in device_status if x['available'] is True],
               key=lambda x: x['pending_jobs'])
    return best['name']

#backend = lowest_pending_jobs()
backend = "ibmqx4"
print("The best backend is " + backend)

qp = QuantumProgram()

nq = 5  # number of qubits
q = qp.create_quantum_register("q", nq)
c = qp.create_classical_register("c", nq)

circuits = ['testQ']
testQ = qp.create_circuit(circuits[0], [q], [c])

# Apply H gate
testQ.h(q[1])
testQ.h(q[2])
testQ.h(q[3])
testQ.h(q[4])

##### CCCZ start #####
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
##### CCCZ end #####

##### Diffusion start #####
testQ.h(q[1])
testQ.h(q[2])
testQ.h(q[3])
testQ.h(q[4])

testQ.x(q[1])
testQ.x(q[2])
testQ.x(q[3])
testQ.x(q[4])


### CCCZ inside diffusion start ###
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
### CCCZ inside diffusion end ###

testQ.x(q[1])
testQ.x(q[2])
testQ.x(q[3])
testQ.x(q[4])

testQ.h(q[1])
testQ.h(q[2])
testQ.h(q[3])
testQ.h(q[4])
##### Diffusion end #####


# Measurement
testQ.measure(q[1], c[1])
testQ.measure(q[2], c[2])
testQ.measure(q[3], c[3])
testQ.measure(q[4], c[4])

job_exp = execute(testQ, backend=backend, shots=1024, max_credits=3)

lapse = 0
interval = 10
while not job_exp.done:
    print('Status @ {} seconds'.format(interval * lapse))
    print(job_exp.status)
    time.sleep(interval)
    lapse += 1
print(job_exp.status)

plot_histogram(job_exp.result().get_counts(circuits[0]))

print('Done!')

# Keita Memo
# I don't know why but circuit_drawer does not work correctly.
# So I use plot_circuit instead.
# circuit_drawer(qc)
plot_circuit(testQ)