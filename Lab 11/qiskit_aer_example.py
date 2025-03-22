import qiskit
from qiskit_aer import AerSimulator
from qiskit_ibm_runtime.fake_provider import FakeManilaV2
from qiskit_ibm_runtime import SamplerV2
from matplotlib import pyplot as plt

# changed this import to ibm_runtime


# Generate 3-qubit GHZ state
circ = qiskit.QuantumCircuit(3)
circ.h(0)
circ.cx(0, 1)
circ.cx(1, 2)
circ.measure_all()

# displays the qc
circ.draw("mpl", style="iqp")
plt.show()

# Construct an ideal simulator
aersim = AerSimulator()

# Perform an ideal simulation
result_ideal = aersim.run(circ).result()
counts_ideal = result_ideal.get_counts(0)
print('Counts(ideal):', counts_ideal)
# Counts(ideal): {'000': 493, '111': 531}

# Construct a noisy simulator backend from an IBMQ backend
# This simulator backend will be automatically configured
# using the device configuration and noise model

backend = FakeManilaV2()

# Removed because they do not work
# aersim_backend = AerSimulator.from_backend(backend)
# result_noise = aersim_backend.run(circ).result()
# counts_noise = result_noise.get_counts(0)


# Based on the IBM documentation
transpiled_circuit = qiskit.transpile(circ, backend)

sampler = SamplerV2(backend)
job = sampler.run([transpiled_circuit])
pub_result = job.result()[0]
counts_noise = pub_result.data.meas.get_counts()

print('Counts(noise):', counts_noise)
# Counts(noise): {'101': 16, '110': 48, '100': 7, '001': 31, '010': 7, '000': 464, '011': 15, '111': 436}
