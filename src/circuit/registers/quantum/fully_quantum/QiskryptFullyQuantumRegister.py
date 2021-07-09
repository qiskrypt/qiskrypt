"""

Copyrights:\n
- © Qiskrypt, 2021 - All rights reserved.\n

Powered by:\n
- IBM
- IBM Quantum
- IBM Qiskit


Description:\n
- The Qiskrypt is a software suite of protocols of
  quantum cryptography, quantum communication and
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

"""

"""
Import required Libraries and Packages.
"""

from src.circuit.registers.quantum.QiskryptQuantumRegister import QiskryptQuantumRegister
"""
Import the Qiskrypt's Quantum Register.
"""

from src.circuit.registers.quantum.fully_quantum.exception.QiskryptFullyQuantumRegisterException \
    import QiskryptNotFullyQuantumRegisterError
"""
Import the Not Fully-Quantum Register Error for the Qiskrypt's Fully-Quantum Register.
"""


class QiskryptFullyQuantumRegister(QiskryptQuantumRegister):
    """
    Object Class of the Qiskrypt's Fully-Quantum Register.
    """

    def __init__(self, name="fully_qu_reg", num_qubits=1, quantum_register=None):
        """
        Constructor for the Qiskrypt's Fully-Quantum Register.

        It calls the constructor of the super-class Qiskrypt's Quantum Register.

        :param name: The name of the Qiskrypt's Fully-Quantum Register.
        :param num_qubits: The number of bits of the Qiskrypt's Fully-Quantum Register.
        :param quantum_register: A built-in quantum register object of
                                 the IBM's Qiskit Quantum Register.
        """
        super().__init__(name=name, num_qubits=num_qubits, quantum_register=quantum_register)

    @staticmethod
    def raise_not_fully_quantum_register_error():
        """
        Return/Raise a Not a Fully-Quantum Register Error for the Qiskrypt's Fully-Quantum Register.

        :raise not_fully_quantum_register_error: a Not a Fully-Quantum Register Error for
                                                 the Qiskrypt's Fully-Quantum Register.
        """

        not_fully_quantum_register_error = QiskryptNotFullyQuantumRegisterError()
        """
        Retrieve the Not a Fully-Quantum Register Error for the Qiskrypt's Fully-Quantum Register.
        """

        """
        Raise the Not a Fully-Quantum Register Error for the Qiskrypt's Fully-Quantum Register.
        """
        raise not_fully_quantum_register_error
