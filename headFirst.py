from qiskit import *
from matplotlib import pyplot as plt
from qiskit.tools.visualization import plot_bloch_multivector


circ = QuantumCircuit(1, 1)
circ.x(0)

sim = Aer.get_backend('statevector_simulator')
res = execute(circ, backend=sim).result()
statevector = res.get_statevector()
print('\nstatevector: ', statevector)

plot_bloch_multivector(statevector)
plt.savefig("img/statevector.png")
plt.show()

sim = Aer.get_backend('unitary_simulator')
res = execute(circ, backend=sim).result()
unitary = res.get_unitary()
print('\nunitary matrix: \n', unitary)
