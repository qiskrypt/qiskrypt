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
Import Ancilla Quantum Register from IBM's Qiskit.
"""

from src.circuit.registers.quantum.exception.QiskryptAncillaQuantumRegisterException \
    import QiskryptNotAncillaQuantumRegisterError
"""
Import the Not Ancilla Quantum Register Error for the Qiskrypt's Ancilla Quantum Register.
"""


class QiskryptAncillaQuantumRegister:
    """
    Object Class of the Qiskrypt's Ancilla Quantum Register.
    """

    def __init__(self, name="anc_qu_reg", num_ancilla_qubits=1, ancilla_quantum_register=None):
        """
        Constructor for the Qiskrypt's Ancilla Quantum Register.

        :param name: The name of the Qiskrypt's Ancilla Quantum Register.
        :param num_ancilla_qubits: The number of qubits of the Qiskrypt's Ancilla Quantum Register.
        :param ancilla_quantum_register: A built-in ancilla quantum register object of
                                         the IBM's Qiskit Ancilla Quantum Register.
        """

        self.name = name
        """
        Set the name of the Qiskrypt's Ancilla Quantum Register.
        """

        self.num_ancilla_qubits = num_ancilla_qubits
        """
        Set the number of the qubits of the Qiskrypt's Ancilla Quantum Register.
        """

        if ancilla_quantum_register is None:
            """
            If the Ancilla Quantum Register is None.
            """

            self.ancilla_quantum_register = AncillaRegister(name=name, size=num_ancilla_qubits)
            """
            Set the built-in ancilla quantum register of the Qiskrypt's Ancilla Quantum Register.
            """

        else:
            """
            If the Ancilla Quantum Register is not None.
            """

            self.ancilla_quantum_register = ancilla_quantum_register
            """
            Set the built-in ancilla quantum register of the Qiskrypt's Ancilla Quantum Register.
            """

    def get_name(self):
        """
        Return the name of the Qiskrypt's Ancilla Quantum Register.

        :return self.name: the name of the Qiskrypt's Ancilla Quantum Register.
        """

        return self.name

    def get_num_ancilla_qubits(self):
        """
        Return the number of qubits of the Qiskrypt's Ancilla Quantum Register.

        :return self.num_ancilla_qubits: the number of qubits of the Qiskrypt's Ancilla Quantum Register.
        """

        return self.num_ancilla_qubits

    def get_ancilla_quantum_register(self):
        """
        Return the IBM's Qiskit Ancilla Quantum Register of the Qiskrypt's Ancilla Quantum Register.

        :return self.ancilla_quantum_register: the IBM's Qiskit Ancilla Quantum Register of
                                               the Qiskrypt's Ancilla Quantum Register.
        """

        return self.ancilla_quantum_register

    @staticmethod
    def raise_not_ancilla_quantum_register_error():
        """
        Return/Raise a Not an Ancilla Quantum Register Error for the Qiskrypt's Ancilla Quantum Register.

        :raise not_ancilla_quantum_register_error: a Not an Ancilla Quantum Register Error for
                                                   the Qiskrypt's Ancilla Quantum Register.
        """

        not_ancilla_quantum_register_error = QiskryptNotAncillaQuantumRegisterError()
        """
        Retrieve the Not an Ancilla Quantum Register Error for the Qiskrypt's Ancilla Quantum Register.
        """

        """
        Raise the Not an Ancilla Quantum Register Error for the Qiskrypt's Ancilla Quantum Register.
        """
        raise not_ancilla_quantum_register_error
