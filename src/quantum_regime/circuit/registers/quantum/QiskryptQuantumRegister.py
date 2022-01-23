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

from src.quantum_regime.circuit.registers.quantum.exception.QiskryptQuantumRegisterException \
    import QiskryptNotQuantumRegisterError
"""
Import the Not Quantum Register Error for the Qiskrypt's Quantum Register.
"""

from src.quantum_regime.circuit.registers.quantum.exception.QiskryptQuantumRegisterException \
    import QiskryptNotValidQuantumRegisterIndexError
"""
Import the Not a Valid Quantum Register Index Error for the Qiskrypt's Quantum Register.
"""


class QiskryptQuantumRegister:
    """
    Object Class of the Qiskrypt's Quantum Register.
    """

    def __init__(self, name="qu_reg", num_qubits=1, qiskit_quantum_register=None):
        """
        Constructor for the Qiskrypt's Quantum Register.

        :param name: the name of the Qiskrypt's Quantum Register.
        :param num_qubits: the number of qubits of the Qiskrypt's Quantum Register.
        :param qiskit_quantum_register: an IBM Qiskit's Quantum Register.
        """

        self.name = name
        """
        Set the name of the Qiskrypt's Quantum Register.
        """

        self.num_qubits = num_qubits
        """
        Set the number of the qubits of the Qiskrypt's Quantum Register.
        """

        if qiskit_quantum_register is None:
            """
            If the IBM Qiskit's Quantum Register is None.
            """

            self.qiskit_quantum_register = QuantumRegister(name=name, size=num_qubits)
            """
            Set the IBM Qiskit's Quantum Register of the Qiskrypt's Quantum Register.
            """

        else:
            """
            If the IBM Qiskit's Quantum Register is not None.
            """

            self.qiskit_quantum_register = qiskit_quantum_register
            """
            Set the IBM Qiskit's Quantum Register of the Qiskrypt's Quantum Register.
            """

    def get_name(self) -> str:
        """
        Return the name of the Qiskrypt's Quantum Register.

        :return self.name: the name of the Qiskrypt's Quantum Register.
        """

        """
        Return the name of the Qiskrypt's Quantum Register.
        """
        return self.name

    def get_num_qubits(self) -> int:
        """
        Return the number of qubits of the Qiskrypt's Quantum Register.

        :return self.num_qubits: the number of qubits of the Qiskrypt's Quantum Register.
        """

        """
        Return the number of qubits of the Qiskrypt's Quantum Register.
        """
        return self.num_qubits

    def get_qiskit_quantum_register(self) -> QuantumRegister:
        """
        Return the IBM Qiskit's Quantum Register of the Qiskrypt's Quantum Register.

        :return self.qiskit_quantum_register: the IBM Qiskit's Quantum Register of
                                              the Qiskrypt's Quantum Register.
        """

        """
        Return the IBM Qiskit's Quantum Register of the Qiskrypt's Quantum Register.
        """
        return self.qiskit_quantum_register

    @staticmethod
    def raise_not_quantum_register_error() -> None:
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
    def raise_not_valid_qiskrypt_quantum_register_index_error() -> None:
        """
        Return/Raise a Not a Valid Qiskrypt's Quantum Register Index Error for the Qiskrypt's Quantum Register.

        :raise not_valid_qiskrypt_quantum_register_index_error: a Not a Valid Qiskrypt's Quantum Register Index Error for
                                                                the Qiskrypt's Quantum Register.
        """

        not_valid_qiskrypt_quantum_register_index_error = QiskryptNotValidQuantumRegisterIndexError()
        """
        Retrieve the Not a Valid Qiskrypt's Quantum Register Index Error for the Qiskrypt's Quantum Register.
        """

        """
        Raise the Not a Valid Qiskrypt's Quantum Register Index Error for the Qiskrypt's Quantum Register.
        """
        raise not_valid_qiskrypt_quantum_register_index_error
