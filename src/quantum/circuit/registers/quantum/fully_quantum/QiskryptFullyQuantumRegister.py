"""

Copyrights:\n
- © Qiskrypt, 2022 - All rights reserved.\n

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
- Prof. Antonio Ravara (NOVA School of Science and Technology, NOVA University of Lisbon, Portugal).

"""

"""
Import required Libraries and Packages.
"""

from qiskit import QuantumRegister
"""
Import Quantum Register from IBM's Qiskit.
"""

from src.quantum.circuit.registers.quantum.QiskryptQuantumRegister import QiskryptQuantumRegister
"""
Import the Qiskrypt's Quantum Register.
"""

from src.quantum.circuit.registers.quantum.fully_quantum.exception.QiskryptFullyQuantumRegisterException \
    import QiskryptNotFullyQuantumRegisterError
"""
Import the Not Fully-Quantum Register Error for the Qiskrypt's Fully-Quantum Register.
"""

from src.quantum.circuit.registers.quantum.fully_quantum.exception.QiskryptFullyQuantumRegisterException \
    import QiskryptNotValidFullyQuantumRegisterIndexError
"""
Import the Not a Valid Fully-Quantum Register Index Error for the Qiskrypt's Fully-Quantum Register.
"""


class QiskryptFullyQuantumRegister(QiskryptQuantumRegister):
    """
    Object Class of the Qiskrypt's Fully-Quantum Register.
    """

    def __init__(self, name="fully_qu_reg", num_qubits=1, qiskit_quantum_register=None):
        """
        Constructor for the Qiskrypt's Fully-Quantum Register.

        It calls the constructor of the super-class Qiskrypt's Quantum Register.

        :param name: the name of the Qiskrypt's Fully-Quantum Register.
        :param num_qubits: the number of qubits of the Qiskrypt's Fully-Quantum Register.
        :param qiskit_quantum_register: an IBM Qiskit's Quantum Register.
        """

        super().__init__(name=name, num_qubits=num_qubits, qiskit_quantum_register=qiskit_quantum_register)
        """
        Calls the constructor of the super-class Qiskrypt's Fully-Quantum Register.
        """

    def get_name(self) -> str:
        """
        Return the name of the Qiskrypt's Fully-Quantum Register.

        :return super().get_name(): the name of the Qiskrypt's Fully-Quantum Register.
        """

        """
        Return the name of the Qiskrypt's Fully-Quantum Register.
        """
        return super().get_name()

    def get_num_qubits(self) -> int:
        """
        Return the number of qubits of the Qiskrypt's Fully-Quantum Register.

        :return super().get_num_qubits(): the number of qubits of
                                          the Qiskrypt's Fully-Quantum Register.
        """

        """
        Return the number of qubits of the Qiskrypt's Fully-Quantum Register.
        """
        return super().get_num_qubits()

    def get_qiskit_fully_quantum_register(self) -> QuantumRegister:
        """
        Return the IBM Qiskit's Quantum Register of the Qiskrypt's Fully-Quantum Register.

        :return super().get_qiskit_quantum_register(): the IBM Qiskit's Quantum Register of
                                                       the Qiskrypt's Fully-Quantum Register.
        """

        """
        Return the IBM Qiskit's Quantum Register of the Qiskrypt's Fully-Quantum Register.
        """
        return super().get_qiskit_quantum_register()

    @staticmethod
    def raise_not_fully_quantum_register_error() -> None:
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

    @staticmethod
    def raise_not_valid_qiskrypt_fully_quantum_register_index_error() -> None:
        """
        Return/Raise a Not a Valid Qiskrypt's Fully-Quantum Register Index Error for
        the Qiskrypt's Fully-Quantum Register.

        :raise not_valid_qiskrypt_fully_quantum_register_index_error: a Not a Valid Fully-Quantum Register Index Error for
                                                                      the Qiskrypt's Fully-Quantum Register.
        """

        not_valid_qiskrypt_fully_quantum_register_index_error = QiskryptNotValidFullyQuantumRegisterIndexError()
        """
        Retrieve the Not a Valid Qiskrypt's Fully-Quantum Register Index Error for
        the Qiskrypt's Fully-Quantum Register.
        """

        """
        Raise the Not a Valid Qiskrypt's Fully-Quantum Register Index Error for
        the Qiskrypt's Fully-Quantum Register.
        """
        raise not_valid_qiskrypt_fully_quantum_register_index_error
