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

MESSAGE_NOT_ANCILLA_FULLY_QUANTUM_REGISTER_EXCEPTION = "Invalid Register: It was expected a Qiskrypt's Ancilla Fully-Quantum Register as argument!!!\n"
"""
The custom defined message for the Not an Ancilla Fully-Quantum Register Error for
the Qiskrypt's Ancilla Fully-Quantum Register.
"""

MESSAGE_NOT_VALID_ANCILLA_FULLY_QUANTUM_REGISTER_INDEX_EXCEPTION = "Invalid Index: The index of the Qiskrypt's Ancilla Fully-Quantum Register " \
                                                                   "tried to be accessed it is not valid!!!\n"
"""
The custom defined message for the Not a Valid Ancilla Fully-Quantum Register Index Error for
the Qiskrypt's Ancilla Fully-Quantum Register in the Qiskrypt's Quantum Circuit.
"""


class QiskryptNotAncillaFullyQuantumRegisterError(Exception):
    """
    Object Class of the Not an Ancilla Fully-Quantum Register Error for
    the Qiskrypt's Ancilla Fully-Quantum Register.
    """

    def __init__(self, message=MESSAGE_NOT_ANCILLA_FULLY_QUANTUM_REGISTER_EXCEPTION):
        """
        Constructor for the Not an Ancilla Fully-Quantum Register Error for
        the Qiskrypt's Ancilla Fully-Quantum Register.
        :param message: The custom message for the Not an Ancilla Fully-Quantum Register Error for
                        the Qiskrypt's Ancilla Fully-Quantum Register.
        """
        self.message = message
        """
        Set the custom message for the Not an Ancilla Fully-Quantum Register Error for
        the Qiskrypt's Ancilla Fully-Quantum Register.
        """

        super().__init__(self.message)
        """
        Calls the constructor of the super-class Exception.
        """


class QiskryptNotValidAncillaFullyQuantumRegisterIndexError(Exception):
    """
    Object Class of the Not a Valid Ancilla Fully-Quantum Register Index Error for
    the Qiskrypt's Ancilla Fully-Quantum Register in the Qiskrypt's Quantum Circuit.
    """

    def __init__(self, message=MESSAGE_NOT_VALID_ANCILLA_FULLY_QUANTUM_REGISTER_INDEX_EXCEPTION):
        """
        Constructor for the Not a Valid Ancilla Fully-Quantum Register Index Error for
        the Qiskrypt's Ancilla Fully-Quantum Register in the Qiskrypt's Quantum Circuit.

        :param message: The custom message for the Not a Valid Ancilla Fully-Quantum Register Index Error for
                        the Qiskrypt's Ancilla Fully-Quantum Register in the Qiskrypt's Quantum Circuit.
        """

        self.message = message
        """
        Set the custom message for the Not a Valid Ancilla Fully-Quantum Register Index Error for
        the Qiskrypt's Ancilla Fully-Quantum Register in the Qiskrypt's Quantum Circuit.
        """

        super().__init__(self.message)
        """
        Calls the constructor of the super-class Exception.
        """
