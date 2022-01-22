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
Definition of the custom Exception messages.
"""

MESSAGE_NO_CHARACTERS_GROUP_CHOSEN_EXCEPTION = "No Characters Group Chosen Error: " \
                                               "No characters group chosen for the Quantum Random Alphanumeric Generator!!!\n"
"""
The custom defined message for the No Characters Group Chosen Error for
the Qiskrypt's Quantum Random Alphanumeric Generator.
"""


class QiskryptQuantumRandomAlphanumericGeneratorNoCharactersGroupChosenError(Exception):
    """
    Object Class of the No Characters Group Chosen Error for
    the Qiskrypt's Quantum Random Alphanumeric Generator.
    """

    def __init__(self, message=MESSAGE_NO_CHARACTERS_GROUP_CHOSEN_EXCEPTION):
        """
        Constructor for the No Characters Group Chosen Error for
        the Qiskrypt's Quantum Random Numeric Generator.

        :param message: the custom message for the No Characters Group Chosen Error for
                        the Qiskrypt's Quantum Random Alphanumeric Generator.
        """

        self.message = message
        """
        Set the custom message for the No Characters Group Chosen Error for
        the Qiskrypt's Quantum Random Alphanumeric Generator.
        """

        super().__init__(self.message)
        """
        Calls the constructor of the super-class Exception.
        """
