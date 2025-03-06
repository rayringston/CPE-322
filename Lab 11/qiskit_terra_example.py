# https://en.wikipedia.org/wiki/Qiskit

import matplotlib.pyplot as plt
# included mpl to display the quantum circuits

from qiskit import QuantumCircuit, transpile

from qiskit_aer import Aer
# added this line, qiskit-aer is a separate package from qiskit now

qc = QuantumCircuit(2, 2)

qc.h(0)
qc.cx(0, 1)

qc.measure([0,1], [0,1])

qc.draw("mpl")
plt.show()

backend = Aer.get_backend('qasm_simulator')
transpiled_qc = transpile(qc, backend)
job_sim = backend.run(transpiled_qc)

sim_result = job_sim.result()

print(sim_result.get_counts(qc))
