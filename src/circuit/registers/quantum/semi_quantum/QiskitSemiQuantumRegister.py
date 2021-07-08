"""

© Copyright Qiskrypt, 2021 - All rights reserved.

Powered by:
- IBM
- IBM Quantum
- IBM Qiskit

Description:
- The Qiskrypt is a software suite of protocols of
  quantum cryptography, quantum communication and
  other protocols/algorithms, built using the IBM's Qiskit.

College(s):
- NOVA School of Science and Technology, NOVA University of Lisbon, Portugal.
- Faculty of Sciences, University of Lisbon, Portugal.
- Tecnico Lisboa, University of Lisbon, Portugal.
- School of Engineering, University of Connecticut, United States of America.

Other Institution(s):
- Instituto de Telecomunicacoes, Portugal.
- Security and Quantum Information Group, Portugal.
- LASIGE, Portugal.
- UT Austin Program, Portugal.

Author(s):
- Ruben Barreiro (NOVA School of Science and Technology, NOVA University of Lisbon, Portugal).

Supervisor(s):
- Prof. Andre Souto (Faculty of Sciences, University of Lisbon, Portugal).

Acknowledgement(s):
- Prof. Paulo Mateus (Tecnico Lisboa, University of Lisbon, Portugal).
- Prof. Nikola Paunkovic (Tecnico Lisboa, University of Lisbon, Portugal).
- Prof. Walter Krawec (School of Engineering, University of Connecticut, United States of America).
- Prof. Antonio Ravara (NOVA School of Science and Technology, NOVA University of Lisbon, Portugal).

"""

"""
Import required Libraries and Packages.
"""

from src.circuit.registers.quantum.QiskitQuantumRegister import QiskitQuantumRegister
"""
Import the IBM's Qiskit Quantum Register.
"""

from src.circuit.registers.quantum.semi_quantum.exception.QiskitSemiQuantumRegisterException \
    import QiskitSemiQuantumRegisterUnsupportedOperationError
"""
Import the Unsupported Operation Error for the IBM's Qiskit Semi-Quantum Register.
"""


class QiskitSemiQuantumRegister(QiskitQuantumRegister):
    """
    Object Class of the IBM's Qiskit Semi-Quantum Register.
    """

    def __init__(self, name="semi_qu_reg", num_qubits=1, quantum_register=None):
        """
        Constructor for the IBM's Qiskit Semi-Quantum Register.

        It calls the constructor of the super-class IBM's Qiskit Quantum Register.

        :param name: The name of the IBM's Qiskit Semi-Quantum Register.
        :param num_qubits: The number of bits of the IBM's Qiskit Semi-Quantum Register.
        :param quantum_register: A built-in quantum register object of
                                 the IBM's Qiskit Semi-Quantum Register.
        """
        super().__init__(name=name, num_qubits=num_qubits, quantum_register=quantum_register)
        """
        Calls the constructor of the super-class IBM's Qiskit Quantum Register.
        """

    @staticmethod
    def raise_unsupported_operation_error():

        """
        Return/Raise an Unsupported Operation Error for the IBM's Qiskit Semi-Quantum Register.
        :raise : an Unsupported Operation Error for the IBM's Qiskit Semi-Quantum Register.
        """

        unsupported_operation_error = QiskitSemiQuantumRegisterUnsupportedOperationError()
        """
        Retrieve the Unsupported Operation Error for the IBM's Qiskit Semi-Quantum Register.
        """

        """
        Raise the Unsupported Operation Error for the IBM's Qiskit Semi-Quantum Register.
        """
        raise unsupported_operation_error
