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
- NOVA LINCS, Portugal.
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
Definition of the custom Exception messages.
"""

MESSAGE_NOT_QUANTUM_REGISTER_EXCEPTION = "Not a Quantum Register Error: " \
                                         "It was expected a Qiskrypt's Quantum Register as argument!!!\n"
"""
The custom defined message for the Not a Quantum Register Error for
the Qiskrypt's Quantum Register.
"""

MESSAGE_NOT_VALID_QUANTUM_REGISTER_INDEX_EXCEPTION = "Not a Valid Quantum Register Index Error: " \
                                                     "The index of the Qiskrypt's Quantum Register " \
                                                     "tried to be accessed it is invalid!!!\n"
"""
The custom defined message for the Not a Valid Quantum Register Index Error for
the Qiskrypt's Quantum Register in the Qiskrypt's Quantum Circuit.
"""


class QiskryptNotQuantumRegisterError(Exception):
    """
    Object Class of the Not a Quantum Register Error for
    the Qiskrypt's Quantum Register.
    """

    def __init__(self, message=MESSAGE_NOT_QUANTUM_REGISTER_EXCEPTION):
        """
        Constructor for the Not a Quantum Register Error for
        the Qiskrypt's Quantum Register.

        :param message: the custom message for the Not a Quantum Register Error for
                        the Qiskrypt's Quantum Register.
        """

        self.message = message
        """
        Set the custom message for the Not a Quantum Register Error for
        the Qiskrypt's Quantum Register.
        """

        super().__init__(self.message)
        """
        Call of the constructor of the super-class Exception.
        """


class QiskryptNotValidQuantumRegisterIndexError(Exception):
    """
    Object Class of the Not a Valid Quantum Register Index Error for
    the Qiskrypt's Quantum Register in the Qiskrypt's Quantum Circuit.
    """

    def __init__(self, message=MESSAGE_NOT_VALID_QUANTUM_REGISTER_INDEX_EXCEPTION):
        """
        Constructor for the Not a Valid Quantum Register Index Error for
        the Qiskrypt's Quantum Register in the Qiskrypt's Quantum Circuit.

        :param message: the custom message for the Not a Valid Quantum Register Index Error for
                        the Qiskrypt's Quantum Register in the Qiskrypt's Quantum Circuit.
        """

        self.message = message
        """
        Set the custom message for the Not a Valid Quantum Register Index Error for
        the Qiskrypt's Quantum Register in the Qiskrypt's Quantum Circuit.
        """

        super().__init__(self.message)
        """
        Call of the constructor of the super-class Exception.
        """
