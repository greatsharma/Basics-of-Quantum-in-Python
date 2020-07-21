from qiskit import *
from qiskit.tools.monitor import job_monitor
from qiskit.tools.visualization import plot_histogram
from matplotlib import pyplot as plt


def make_circuit():
    qr = QuantumRegister(3)
    cr = ClassicalRegister(3)

    circuit = QuantumCircuit(qr, cr)

    circuit.h(qr[0])  # put q0 in quantum superposition
    circuit.cx(qr[0], qr[1])  # entangle q0 and q1
    circuit.cx(qr[1], qr[2])  # entangle q1 and a2

    circuit.measure(qr, cr)  # collapse the uncertainity

    return circuit


def run_on_simulator(circuit, shots=1024):
    print('\nrunning on simulator...\n')

    simulator = Aer.get_backend('qasm_simulator')
    result = execute(circuit, backend=simulator, shots=shots).result()

    return result


def run_on_machine(circuit, device_name='ibmq_essex', shots=1024):
    print('\nrunning on {}...\n'.format(device_name))

    IBMQ.load_account()

    provider = IBMQ.get_provider('ibm-q')
    device = provider.get_backend(device_name)

    job = execute(circuit, backend=device, shots=shots)
    job_monitor(job)

    return job.result()


def draw_circuit(circuit, title=''):
    circuit.draw(output='mpl')
    plt.title(title)
    plt.savefig("img/qe_circ.png")
    plt.show()


def draw_results(circuit, result, title=''):
    counts = result.get_counts(circuit)
    print(counts)
    plot_histogram(counts)
    plt.title(title)
    plt.savefig("img/qe_res.png")
    plt.show()


if __name__ == '__main__':

    circ = make_circuit()

    res = run_on_simulator(circ)
    #res = run_on_machine(circ, 'ibmq_essex')

    draw_circuit(circ, '3 qbits qauntum entaglement circuit')
    draw_results(circ, res, '3 qbits qauntum entaglement')
