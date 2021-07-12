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

from src.circuit.registers.quantum.QiskryptAncillaQuantumRegister import QiskryptAncillaQuantumRegister
"""
Import the Qiskrypt's Ancilla Quantum Register.
"""

from src.circuit.registers.quantum.semi_quantum.exception.QiskryptAncillaSemiQuantumRegisterException \
    import QiskryptAncillaSemiQuantumRegisterUnsupportedOperationError
"""
Import the Unsupported Operation Error for the Qiskrypt's Ancilla Semi-Quantum Register.
"""

from src.circuit.registers.quantum.semi_quantum.exception.QiskryptAncillaSemiQuantumRegisterException \
    import QiskryptNotAncillaSemiQuantumRegisterError
"""
Import the Not Ancilla Semi-Quantum Register Error for the Qiskrypt's Ancilla Semi-Quantum Register.
"""


class QiskryptAncillaSemiQuantumRegister(QiskryptAncillaQuantumRegister):
    """
    Object Class of the Qiskrypt's Ancilla Semi-Quantum Register.
    """

    def __init__(self, name="anc_semi_qu_reg", num_ancilla_qubits=1, ancilla_quantum_register=None):
        """
        Constructor for the Qiskrypt's Ancilla Semi-Quantum Register.

        It calls the constructor of the super-class Qiskrypt's Ancilla Quantum Register.

        :param name: The name of the Qiskrypt's Ancilla Semi-Quantum Register.
        :param num_ancilla_qubits: The number of ancilla qubits of the Qiskrypt's Ancilla Semi-Quantum Register.
        :param ancilla_quantum_register: A built-in ancilla quantum register object of
                                         the IBM's Qiskit Ancilla Quantum Register.
        """
        super().__init__(name=name, num_ancilla_qubits=num_ancilla_qubits, ancilla_quantum_register=ancilla_quantum_register)
        """
        Calls the constructor of the super-class Qiskrypt's Ancilla Quantum Register.
        """

    def get_name(self):
        """
        Return the name of the Qiskrypt's Ancilla Semi-Quantum Register.

        :return super().get_name(): the name of the Qiskrypt's Ancilla Semi-Quantum Register.
        """

        return super().get_name()

    def get_num_ancilla_qubits(self):
        """
        Return the number of ancilla qubits of the Qiskrypt's Ancilla Semi-Quantum Register.

        :return super().get_num_ancilla_qubits(): the number of ancilla qubits of
                                                  the Qiskrypt's Ancilla Semi-Quantum Register.
        """

        return super().get_num_ancilla_qubits()

    def get_ancilla_semi_quantum_register(self):
        """
        Return the IBM's Qiskit Ancilla Quantum Register of the Qiskrypt's Ancilla Semi-Quantum Register.

        :return super().get_ancilla_quantum_register(): the IBM's Qiskit Ancilla Quantum Register of
                                                        the Qiskrypt's Ancilla Semi-Quantum Register.
        """

        return super().get_ancilla_quantum_register()

    @staticmethod
    def raise_unsupported_operation_error():
        """
        Return/Raise an Unsupported Operation Error for the Qiskrypt's Ancilla Semi-Quantum Register.

        :raise unsupported_operation_error: an Unsupported Operation Error for
                                            the Qiskrypt's Ancilla Semi-Quantum Register.
        """

        unsupported_operation_error = QiskryptAncillaSemiQuantumRegisterUnsupportedOperationError()
        """
        Retrieve the Unsupported Operation Error for the Qiskrypt's Ancilla Semi-Quantum Register.
        """

        """
        Raise the Unsupported Operation Error for the Qiskrypt's Ancilla Semi-Quantum Register.
        """
        raise unsupported_operation_error

    @staticmethod
    def raise_not_ancilla_semi_quantum_register_error():
        """
        Return/Raise a Not an Ancilla Semi-Quantum Register Error for the Qiskrypt's Ancilla Semi-Quantum Register.

        :raise not_ancilla_semi_quantum_register_error: a Not an Ancilla Semi-Quantum Register Error for
                                                        the Qiskrypt's Ancilla Semi-Quantum Register.
        """

        not_ancilla_semi_quantum_register_error = QiskryptNotAncillaSemiQuantumRegisterError()
        """
        Retrieve the Not an Ancilla Semi-Quantum Register Error for the Qiskrypt's Ancilla Semi-Quantum Register.
        """

        """
        Raise the Not an Ancilla Semi-Quantum Register Error for the Qiskrypt's Ancilla Semi-Quantum Register.
        """
        raise not_ancilla_semi_quantum_register_error