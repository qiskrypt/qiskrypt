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
Definition of the custom Exception messages.
"""

MESSAGE_COIN_NOT_TOSSED_YET_EXCEPTION = "Coin Not Tossed Yet Error: The Coin of the Quantum Coin Tossing was not tossed yet!!!\n"
"""
The custom defined message for the Coin Not Tossed Yet Error for
the Qiskrypt's Quantum Coin Tossing.
"""

MESSAGE_COIN_ALREADY_TOSSED_EXCEPTION = "Coin Already Tossed Error: The Coin was already tossed!!!\n"
"""
The custom defined message for the Coin Already Tossed Error for
the Qiskrypt's Quantum Coin Tossing.
"""


class QiskryptQuantumCoinTossingCoinNotTossedYetError(Exception):
    """
    Object Class of the Coin Not Tossed Yet Error for the Qiskrypt's Quantum Coin Tossing.
    """

    def __init__(self, message=MESSAGE_COIN_NOT_TOSSED_YET_EXCEPTION):
        """
        Constructor for the Coin Not Tossed Yet Error for the Qiskrypt's Quantum Coin Tossing.

        :param message: the custom message for the Coin Not Tossed Yet Error for the Qiskrypt's Quantum Coin Tossing.
        """

        self.message = message
        """
        Set the custom message for the Coin Not Tossed Yet Error for the Qiskrypt's Quantum Coin Tossing.
        """

        super().__init__(self.message)
        """
        Calls the constructor of the super-class Exception.
        """


class QiskryptQuantumCoinTossingCoinAlreadyTossedError(Exception):
    """
    Object Class of the Coin Already Tossed Error for the Qiskrypt's Quantum Coin Tossing.
    """

    def __init__(self, message=MESSAGE_COIN_ALREADY_TOSSED_EXCEPTION):
        """
        Constructor for the Coin Already Tossed Error for the Qiskrypt's Quantum Coin Tossing.

        :param message: the custom message for the Coin Already Tossed Error for the Qiskrypt's Quantum Coin Tossing.
        """

        self.message = message
        """
        Set the custom message for the Coin Already Tossed Error for the Qiskrypt's Quantum Coin Tossing.
        """

        super().__init__(self.message)
        """
        Calls the constructor of the super-class Exception.
        """
