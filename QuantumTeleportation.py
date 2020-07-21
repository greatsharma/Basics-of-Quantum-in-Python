"""
Quantum teleportation is a process by which information (e.g.,
the exact state of an atom or photon) can be transmitted (exactly,
in principle) from one location to another, with the help of
classical communication and previously shared quantum entanglement
between the sending and receiving location.
"""

from qiskit import *
import matplotlib.pyplot as plt
from qiskit.tools.monitor import job_monitor
from qiskit.tools.visualization import plot_histogram


def build_circuit():
    circ = QuantumCircuit(3, 3)

    circ.x(0)
    circ.barrier()

    circ.h(1)
    circ.cx(1, 2)
    circ.cx(0, 1)
    circ.h(0)
    circ.barrier()

    circ.measure(0, 0)
    circ.measure(1, 1)
    circ.barrier()

    circ.cx(1, 2)
    circ.cz(0, 2)
    circ.barrier()

    circ.measure(2, 2)

    return circ


def run_on_simulator(circ, shots=1024):
    print('\nrunning on simulator...\n')

    sim = Aer.get_backend('qasm_simulator')
    result = execute(circ, backend=sim, shots=shots).result()

    return result


def run_on_machine(circ, device_name='ibmq_essex', shots=1024):
    print('\nrunning on {}...\n'.format(device_name))

    IBMQ.load_account()

    provider = IBMQ.get_provider('ibm-q')
    device = provider.get_backend(device_name)

    job = execute(circ, backend=device, shots=shots)
    job_monitor(job)

    return job.result()


def draw_circuit(circ, title=''):
    circ.draw(output='mpl')
    plt.title(title)
    plt.savefig("img/qt_circ.png")
    plt.show()


def plot_results(result, title=''):
    counts = result.get_counts()
    print('\ncounts : {}\n'.format(counts))
    plot_histogram(counts)
    plt.title(title)
    plt.savefig("img/qt_res.png")
    plt.show()


if __name__ == '__main__':
    circ = build_circuit()

    draw_circuit(circ, 'circuit quantum teleportation')

    result = run_on_simulator(circ)
    # result = run_on_machine(circ)

    plot_results(result, 'result quantum teleportation')
