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

MESSAGE_UNSUPPORTED_TYPE_REGISTERS_EXCEPTION = "Unsupported type of Registers for the Qiskrypt's Quantum Circuit!!!\n"\
                                               "- The Qiskrypt's Quantum Circuit only supports Register(s) given as list."
"""
The custom defined message for the Unsupported Type for Registers Error for
the Qiskrypt's Quantum Circuit.
"""


class QiskryptQuantumCircuitUnsupportedTypeRegistersError(Exception):
    """
    Object Class of the Unsupported Type of Registers Error for
    the Qiskrypt's Quantum Circuit.
    """

    def __init__(self, message=MESSAGE_UNSUPPORTED_TYPE_REGISTERS_EXCEPTION):
        """
        Constructor for the Unsupported Type of Registers Error for
        the Qiskrypt's Quantum Circuit.
        :param message: The custom message for the Unsupported Type of Registers Error for
                        the Qiskrypt's Quantum Circuit.
        """
        self.message = message
        """
        Set the custom message for the Unsupported Type of Registers Error for
        the Qiskrypt's Quantum Circuit.
        """

        super().__init__(self.message)
        """
        Calls the constructor of the super-class Exception.
        """
