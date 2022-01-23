"""

Copyrights:\n
- © Qiskrypt, 2022 - All rights reserved.\n

Powered by:\n
- IBM
- IBM Quantum
- IBM Qiskit


Description:\n
- The Qiskrypt is a software suite of protocols of
  quantum_regime cryptography, quantum_regime communication and
  other protocols/algorithms, built using the IBM's Qiskit.

College(s):\n
- NOVA School of Science and Technology, NOVA University of Lisbon, Portugal.
- Faculty of Sciences, University of Lisbon, Portugal.
- Tecnico Lisboa, University of Lisbon, Portugal.
- School of Engineering, University of Connecticut, United States of America.

Other Institution(s):\n
- Instituto de Telecomunicacoes, Portugal.
- SQIG, Portugal.
- LASIGE, Portugal.
- UT Austin Program, Portugal.

Author(s):\n
- Ruben Barreiro (NOVA School of Science and Technology, NOVA University of Lisbon, Portugal).

Acknowledgement(s):\n
- Prof. Andre Souto (Faculty of Sciences, University of Lisbon, Portugal).
- Prof. Paulo Mateus (Tecnico Lisboa, University of Lisbon, Portugal).
- Prof. Nikola Paunkovic (Tecnico Lisboa, University of Lisbon, Portugal).
- Prof. Walter Krawec (School of Engineering, University of Connecticut, United States of America).
- Prof. Antonio Ravara (NOVA School of Science and Technology, NOVA University of Lisbon, Portugal).

"""

"""
Import required Libraries and Packages.
"""

from src.quantum_regime.circuit.QiskryptQuantumCircuit import QiskryptQuantumCircuit
"""
Import the Qiskrypt's Quantum Circuit.
"""


class QiskryptBlochSphere:
    """
    Object class for the Qiskrypt's Bloch Sphere.
    """

    def __init__(self, name: str, qiskrypt_quantum_circuit: QiskryptQuantumCircuit,
                 qiskit_quantum_register_index: int, qubit_index: int):
        """
        Constructor of the Qiskrypt's Bloch Sphere.

        :param name: the name of the Qiskrypt's Quantum Random Generator.
        :param qiskrypt_quantum_circuit: the Qiskrypt's Quantum Circuit of the Qiskrypt's Bloch Sphere.
        :param qiskit_quantum_register_index: the index of the IBM Qiskit's Quantum Register,
                                              involved in the Qiskrypt's Bloch Sphere.
        :param qubit_index: the index of the qubit in the IBM Qiskit's Quantum Register,
                            to which will be extracted the three-dimensional visualization,
                            involved in the Qiskrypt's Bloch Sphere.
        """

        self.name = name
        """
        Set the name for the Qiskrypt's Bloch Sphere.
        """

        self.qiskrypt_quantum_circuit = qiskrypt_quantum_circuit
        """
        Set the Qiskrypt's Quantum Circuit of
        the Qiskrypt's Bloch Sphere.
        """

        self.qiskit_quantum_register_index = \
            qiskit_quantum_register_index
        """
        Set the index of the IBM Qiskit's Quantum Register,
        involved in the Qiskrypt's Bloch Sphere.
        """

        self.qubit_index = qubit_index
        """
        Set the index of the qubit in the IBM Qiskit's Quantum Register,
        to which will be extracted the three-dimensional visualization,
        involved in the Qiskrypt's Bloch Sphere.
        """
