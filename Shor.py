import numpy as np
from qiskit import QuantumCircuit, Aer, execute
from qiskit.aqua.algorithms import Shor

N = 15

shor = Shor(N)

backend = Aer.get_backend('qasm_simulator')

result = shor.run(backend)

print("Factors of", N, "are:", result['factors'])