import getpass, time
from qiskit import ClassicalRegister, QuantumRegister
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

backend = lowest_pending_jobs()
print("The best backend is " + backend)

q = QuantumRegister(2)
c = ClassicalRegister(2)
qc = QuantumCircuit(q, c)

# Apply H gate
qc.h(q[0])
qc.h(q[1])

# Oracle to negate |11>
qc.h(q[0])
qc.cx(q[1],q[0])
qc.h(q[0])

# Diffusion operator to amplify the probability amplitude of |11>
qc.h(q[0])
qc.h(q[1])
qc.x(q[0])
qc.x(q[1])
qc.h(q[0])
qc.cx(q[1],q[0])
qc.h(q[0])
qc.x(q[0])
qc.x(q[1])
qc.h(q[0])
qc.h(q[1])

# Measurement
qc.measure(q, c)

job_exp = execute(qc, backend=backend, shots=1024, max_credits=3)

lapse = 0
interval = 10
while not job_exp.done:
    print('Status @ {} seconds'.format(interval * lapse))
    print(job_exp.status)
    time.sleep(interval)
    lapse += 1
print(job_exp.status)

plot_histogram(job_exp.result().get_counts(qc))

print('Done!')

# Keita Memo
# I don't know why but circuit_drawer does not work correctly.
# So I use plot_circuit instead.
# circuit_drawer(qc)
plot_circuit(qc)