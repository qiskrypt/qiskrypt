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

from src.quantum_regime.networking_and_communications.channels\
    .classical.noiseless.QiskryptNoiselessClassicalCommunicationChannel \
    import QiskryptNoiselessClassicalCommunicationChannel
"""
Import the Qiskrypt's Noiseless Classical Communication Channel.
"""

from src.quantum_regime.networking_and_communications.channels.QiskryptCommunicationChannel \
    import POSSIBLE_COMMUNICATION_CHANNEL_TYPES
"""
Import the scenarios for the Qiskrypt's Communication Channel.
"""


class QiskryptP2PNoiselessClassicalCommunicationChannel(QiskryptNoiselessClassicalCommunicationChannel):
    """
    Object class for the Qiskrypt's Unicast (One-to-One) Noiseless
    Classical Communication Channel.
    """

    def __init__(self, num: int, name: str, directions: list):
        """
        Constructor of the Qiskrypt's Unicast (One-to-One) Noiseless
        Classical Communication Channel.

        :param num: the number of the Qiskrypt's Communication Channel.
        :param name: the name of the Qiskrypt's Communication Channel.
        :param directions: the list of directions of the Qiskrypt's Communication Channel.
        """

        super().__init__(num, name, POSSIBLE_COMMUNICATION_CHANNEL_TYPES[0], directions)
        """
        Call of the constructor of the super-class Qiskrypt's Noiseless
        Classical Communication Channel.
        """

    def get_num(self) -> int:
        """
        Return the number of the Qiskrypt's Communication Channel.

        :return super().get_num(): the number of the Qiskrypt's Communication Channel.
        """

        """
        Return the number of the Qiskrypt's Communication Channel.
        """
        return super().get_num()

    def get_name(self) -> str:
        """
        Return the name of the Qiskrypt's Communication Channel.

        :return super().get_name(): the name of the Qiskrypt's Communication Channel.
        """

        """
        Return the name of the Qiskrypt's Communication Channel.
        """
        return super().get_name()

    def get_context(self) -> str:
        """
        Return the context of the Qiskrypt's Communication Channel.

        :return super().get_context(): the context of the Qiskrypt's Communication Channel.
        """

        """
        Return the context of the Qiskrypt's Communication Channel.
        """
        return super().get_context()

    def get_scenario(self) -> str:
        """
        Return the scenario of the Qiskrypt's Communication Channel.

        :return super().get_scenario(): the scenario of the Qiskrypt's Communication Channel.
        """

        """
        Return the scenario of the Qiskrypt's Communication Channel.
        """
        return super().get_scenario()

    def get_channel_type(self) -> str:
        """
        Return the type of the Qiskrypt's Communication Channel.

        :return super().get_channel_type(): the type of the Qiskrypt's Communication Channel.
        """

        """
        Return the type of the Qiskrypt's Communication Channel.
        """
        return super().get_channel_type()

    def get_directions(self) -> list:
        """
        Return the list of directions of the Qiskrypt's Communication Channel.

        :return super().get_directions(): the list of directions of
                                          the Qiskrypt's Communication Channel.
        """

        """
        Return the list of directions of the Qiskrypt's Communication Channel.
        """
        return super().get_directions()

    def is_operational(self) -> bool:
        """
        Return the boolean flag to keep information about if
        the Qiskrypt's Communication Channel is operational.

        :return super().is_operational(): the boolean flag to keep information about if
                                          the Qiskrypt's Communication Channel is operational.
        """

        """
        Return the boolean flag to keep information about if
        the Qiskrypt's Communication Channel is operational.
        """
        return super().is_operational()

    def set_operational(self, operational: bool):
        """
        Set the boolean flag to keep information about if
        the Qiskrypt's Communication Channel is operational, with a given Boolean value.
        """

        super().set_operational(operational)
        """
        Set the boolean flag to keep information about if
        the Qiskrypt's Communication Channel is operational,
        with the given Boolean value.
        """

    def is_installed(self) -> bool:
        """
        Return the boolean flag to keep information about if
        the Qiskrypt's Communication Channel is installed.

        :return super().is_installed(): the boolean flag to keep information about if
                                        the Qiskrypt's Communication Channel is installed.
        """

        """
        Return the boolean flag to keep information about if
        the Qiskrypt's Communication Channel is installed.
        """
        return super().is_installed()

    def set_installed(self, installed: bool):
        """
        Set the boolean flag to keep information about if
        the Qiskrypt's Communication Channel is installed, with a given Boolean value.
        """

        super().set_installed(installed)
        """
        Set the boolean flag to keep information about if
        the Qiskrypt's Communication Channel is installed,
        with the given Boolean value.
        """
