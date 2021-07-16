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

from qiskit import QuantumRegister
"""
Import Quantum Register from IBM's Qiskit.
"""

from src.circuit.registers.quantum.exception.QiskryptQuantumRegisterException \
    import QiskryptNotQuantumRegisterError
"""
Import the Not Quantum Register Error for the Qiskrypt's Quantum Register.
"""

from src.circuit.registers.quantum.exception.QiskryptQuantumRegisterException \
    import QiskryptNotValidQuantumRegisterIndexError
"""
Import the Not a Valid Quantum Register Index Error for the Qiskrypt's Quantum Register.
"""


class QiskryptQuantumRegister:
    """
    Object Class of the Qiskrypt's Quantum Register.
    """

    def __init__(self, name="qu_reg", num_qubits=1, quantum_register=None):
        """
        Constructor for the Qiskrypt's Quantum Register.

        :param name: The name of the Qiskrypt's Quantum Register.
        :param num_qubits: The number of qubits of the Qiskrypt's Quantum Register.
        :param quantum_register: A built-in quantum register object of
                                 the IBM's Qiskit Quantum Register.
        """

        self.name = name
        """
        Set the name of the Qiskrypt's Quantum Register.
        """

        self.num_qubits = num_qubits
        """
        Set the number of the qubits of the Qiskrypt's Quantum Register.
        """

        if quantum_register is None:
            """
            If the Quantum Register is None.
            """

            self.quantum_register = QuantumRegister(name=name, size=num_qubits)
            """
            Set the built-in quantum register of the Qiskrypt's Quantum Register.
            """

        else:
            """
            If the Quantum Register is not None.
            """

            self.quantum_register = quantum_register
            """
            Set the built-in quantum register of the Qiskrypt's Quantum Register.
            """

    def get_name(self) -> str:
        """
        Return the name of the Qiskrypt's Quantum Register.

        :return self.name: the name of the Qiskrypt's Quantum Register.
        """

        return self.name

    def get_num_qubits(self) -> int:
        """
        Return the number of qubits of the Qiskrypt's Quantum Register.

        :return self.num_qubits: the number of qubits of the Qiskrypt's Quantum Register.
        """

        return self.num_qubits

    def get_quantum_register(self) -> QuantumRegister:
        """
        Return the IBM's Qiskit Quantum Register of the Qiskrypt's Quantum Register.

        :return self.quantum_register: the IBM's Qiskit Quantum Register of the Qiskrypt's Quantum Register.
        """

        return self.quantum_register

    @staticmethod
    def raise_not_quantum_register_error():
        """
        Return/Raise a Not a Quantum Register Error for the Qiskrypt's Quantum Register.

        :raise not_quantum_register_error: a Not a Quantum Register Error for
                                           the Qiskrypt's Quantum Register.
        """

        not_quantum_register_error = QiskryptNotQuantumRegisterError()
        """
        Retrieve the Not a Quantum Register Error for the Qiskrypt's Quantum Register.
        """

        """
        Raise the Not a Quantum Register Error for the Qiskrypt's Quantum Register.
        """
        raise not_quantum_register_error

    @staticmethod
    def raise_not_valid_quantum_register_index_error():
        """
        Return/Raise a Not a Valid Quantum Register Index Error for the Qiskrypt's Quantum Register.

        :raise not_valid_quantum_register_index_error: a Not a Valid Quantum Register Index Error for
                                                       the Qiskrypt's Quantum Register.
        """

        not_valid_quantum_register_index_error = QiskryptNotValidQuantumRegisterIndexError()
        """
        Retrieve the Not a Valid Quantum Register Index Error for the Qiskrypt's Quantum Register.
        """

        """
        Raise the Not a Valid Quantum Register Index Error for the Qiskrypt's Quantum Register.
        """
        raise not_valid_quantum_register_index_error
