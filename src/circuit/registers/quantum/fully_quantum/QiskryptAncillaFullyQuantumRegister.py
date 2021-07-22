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

from qiskit import AncillaRegister
"""
Import Ancilla Register from IBM's Qiskit.
"""

from src.circuit.registers.quantum.QiskryptAncillaQuantumRegister import QiskryptAncillaQuantumRegister
"""
Import the Qiskrypt's Ancilla Quantum Register.
"""

from src.circuit.registers.quantum.fully_quantum.exception.QiskryptAncillaFullyQuantumRegisterException \
    import QiskryptNotAncillaFullyQuantumRegisterError
"""
Import the Not Ancilla Fully-Quantum Register Error for the Qiskrypt's Ancilla Fully-Quantum Register.
"""

from src.circuit.registers.quantum.fully_quantum.exception.QiskryptAncillaFullyQuantumRegisterException \
    import QiskryptNotValidAncillaFullyQuantumRegisterIndexError
"""
Import the Not a Valid Ancilla Fully-Quantum Register Index Error for the Qiskrypt's Ancilla Fully-Quantum Register.
"""


class QiskryptAncillaFullyQuantumRegister(QiskryptAncillaQuantumRegister):
    """
    Object Class of the Qiskrypt's Ancilla Fully-Quantum Register.
    """

    def __init__(self, name="anc_fully_qu_reg", num_ancilla_qubits=1, qiskit_ancilla_quantum_register=None):
        """
        Constructor for the Qiskrypt's Ancilla Fully-Quantum Register.

        It calls the constructor of the super-class Qiskrypt's Ancilla Quantum Register.

        :param name: The name of the Qiskrypt's Ancilla Fully-Quantum Register.
        :param num_ancilla_qubits: The number of ancilla qubits of the Qiskrypt's Ancilla Fully-Quantum Register.
        :param qiskit_ancilla_quantum_register: an IBM Qiskit's Ancilla Quantum Register.
        """

        super().__init__(name=name, num_ancilla_qubits=num_ancilla_qubits, qiskit_ancilla_quantum_register=qiskit_ancilla_quantum_register)
        """
        Calls the constructor of the super-class Qiskrypt's Ancilla Quantum Register.
        """

    def get_name(self) -> str:
        """
        Return the name of the Qiskrypt's Ancilla Fully-Quantum Register.

        :return super().get_name(): the name of the Qiskrypt's Ancilla Fully-Quantum Register.
        """

        """
        Return the name of the Qiskrypt's Ancilla Fully-Quantum Register.
        """
        return super().get_name()

    def get_num_ancilla_qubits(self) -> int:
        """
        Return the number of ancilla qubits of the Qiskrypt's Ancilla Fully-Quantum Register.

        :return super().get_num_ancilla_qubits(): the number of ancilla qubits of
                                                  the Qiskrypt's Ancilla Fully-Quantum Register.
        """

        """
        Return the number of ancilla qubits of the Qiskrypt's Ancilla Fully-Quantum Register.
        """
        return super().get_num_ancilla_qubits()

    def get_qiskit_ancilla_fully_quantum_register(self) -> AncillaRegister:
        """
        Return the IBM Qiskit's Ancilla Quantum Register of the Qiskrypt's Ancilla Fully-Quantum Register.

        :return super().get_qiskit_ancilla_quantum_register(): the IBM Qiskit's Ancilla Quantum Register of
                                                               the Qiskrypt's Ancilla Fully-Quantum Register.
        """

        """
        Return the IBM Qiskit's Ancilla Quantum Register of the Qiskrypt's Ancilla Fully-Quantum Register.
        """
        return super().get_qiskit_ancilla_quantum_register()

    @staticmethod
    def raise_not_ancilla_fully_quantum_register_error() -> None:
        """
        Return/Raise a Not an Ancilla Fully-Quantum Register Error for
        the Qiskrypt's Ancilla Fully-Quantum Register.

        :raise not_ancilla_fully_quantum_register_error: a Not an Ancilla Fully-Quantum Register Error for
                                                         the Qiskrypt's Ancilla Fully-Quantum Register.
        """

        not_ancilla_fully_quantum_register_error = QiskryptNotAncillaFullyQuantumRegisterError()
        """
        Retrieve the Not an Ancilla Fully-Quantum Register Error for the Qiskrypt's Ancilla Fully-Quantum Register.
        """

        """
        Raise the Not a Fully-Quantum Register Error for the Qiskrypt's Fully-Quantum Register.
        """
        raise not_ancilla_fully_quantum_register_error

    @staticmethod
    def raise_not_valid_qiskrypt_ancilla_fully_quantum_register_index_error() -> None:
        """
        Return/Raise a Not a Valid Qiskrypt's Ancilla Fully-Quantum Register Index Error for
        the Qiskrypt's Ancilla Fully-Quantum Register.

        :raise not_valid_qiskrypt_ancilla_fully_quantum_register_index_error: a Not a Valid Qiskrypt's Ancilla Fully-Quantum Register Index Error for
                                                                              the Qiskrypt's Ancilla Fully-Quantum Register.
        """

        not_valid_qiskrypt_ancilla_fully_quantum_register_index_error = QiskryptNotValidAncillaFullyQuantumRegisterIndexError()
        """
        Retrieve the Not a Valid Qiskrypt's Ancilla Fully-Quantum Register Index Error for
        the Qiskrypt's Ancilla Fully-Quantum Register.
        """

        """
        Raise the Not a Valid Qiskrypt's Ancilla Fully-Quantum Register Index Error for
        the Qiskrypt's Ancilla Fully-Quantum Register.
        """
        raise not_valid_qiskrypt_ancilla_fully_quantum_register_index_error
