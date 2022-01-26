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
Definition of Constants and Enumerations.
"""

POSSIBLE_COMMUNICATION_CHANNELS_CONTEXTS = ["QUANTUM", "CLASSICAL"]
"""
The available Communication Channel contexts for the Qiskrypt's Communication Channel.
"""


class QiskryptCommunicationChannel:
    """
    Object class for the Qiskrypt's Communication Channel.
    """

    def __init__(self, communication_channel_num: int, communication_channel_name: str):
        """
        Constructor of the Qiskrypt's Communication Channel.

        :param communication_channel_num: the number of the Qiskrypt's Communication Channel.
        :param communication_channel_name: the name of the Qiskrypt's Communication Channel.
        """

        self.communication_channel_num = communication_channel_num
        """
        Set the number of the Qiskrypt's Communication Channel.
        """

        self.communication_channel_name = communication_channel_name
        """
        Set the name of the Qiskrypt's Communication Channel.
        """

    def get_communication_channel_num(self) -> int:
        """
        Return the number of the Qiskrypt's Communication Channel.

        :return self.communication_channel_num: the number of the Qiskrypt's Communication Channel.
        """

        """
        Return the number of the Qiskrypt's Communication Channel.
        """
        return self.communication_channel_num

    def get_communication_channel_name(self) -> str:
        """
        Return the name of the Qiskrypt's Communication Channel.

        :return self.communication_channel_name: the name of the Qiskrypt's Communication Channel.
        """

        """
        Return the name of the Qiskrypt's Communication Channel.
        """
        return self.communication_channel_name
