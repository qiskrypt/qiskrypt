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

MESSAGE_INVALID_DATA_TYPE_EXCEPTION = "Invalid Data Type Error: " \
                                      "The Data Type given to the Quantum Random Numeric Generator is invalid!!!\n"
"""
The custom defined message for the Invalid Data Type Error for
the Qiskrypt's Quantum Random Numeric Generator.
"""


class QiskryptQuantumRandomNumericGeneratorInvalidDataTypeError(Exception):
    """
    Object Class of the Invalid Data Type Error for
    the Qiskrypt's Quantum Random Numeric Generator.
    """

    def __init__(self, message=MESSAGE_INVALID_DATA_TYPE_EXCEPTION):
        """
        Constructor for the Invalid Data Type Error for
        the Qiskrypt's Quantum Random Numeric Generator.

        :param message: the custom message for the Invalid Data Type Error for
                        the Qiskrypt's Quantum Random Numeric Generator.
        """

        self.message = message
        """
        Set the custom message for the Quantum Random Generator Not Configured Yet Error for
        the Qiskrypt's Quantum Random Numeric Generator.
        """

        super().__init__(self.message)
        """
        Call of the constructor of the super-class Exception.
        """
