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

POSSIBLE_COMMUNICATION_CHANNELS_SCENARIOS = ["NOISELESS", "NOISY"]
"""
The available Communication Channel scenarios for the Qiskrypt's Communication Channel.
"""

POSSIBLE_COMMUNICATION_CHANNELS_MEDIUMS = ["FIBER-OPTIC", "SATELLITE"]
"""
The available Communication Channel scenarios for the Qiskrypt's Communication Channel.
"""

FIBER_OPTICS_MAX_DISTANCE_KMS_COHERENT_COMMUNICATIONS = 100.0
"""
The maximum distance in KMs (Kilometers) in Fiber Optics, for coherent Communications.
"""


class QiskryptCommunicationChannel:
    """
    Object class for the Qiskrypt's Communication Channel.
    """

    def __init__(self, communication_channel_num: int, communication_channel_name: str,
                 communication_channel_context: str, communication_channel_scenario: str,
                 communication_channel_medium: str, communication_channel_distance_in_kms: float):
        """
        Constructor of the Qiskrypt's Communication Channel.

        :param communication_channel_num: the number of the Qiskrypt's Communication Channel.
        :param communication_channel_name: the name of the Qiskrypt's Communication Channel.
        :param communication_channel_context: the context of the Qiskrypt's Communication Channel.
        :param communication_channel_scenario: the scenario of the Qiskrypt's Communication Channel.
        :param communication_channel_medium: the medium of the Qiskrypt's Communication Channel.
        :param communication_channel_distance_in_kms: the distance of the Qiskrypt's Communication Channel,
                                                      in KMs (Kilometers).
        """

        self.communication_channel_num = communication_channel_num
        """
        Set the number of the Qiskrypt's Communication Channel.
        """

        self.communication_channel_name = communication_channel_name
        """
        Set the name of the Qiskrypt's Communication Channel.
        """

        self.communication_channel_context = communication_channel_context
        """
        Set the context of the Qiskrypt's Communication Channel.
        """

        self.communication_channel_scenario = communication_channel_scenario
        """
        Set the scenario of the Qiskrypt's Communication Channel.
        """

        self.communication_channel_medium = communication_channel_medium
        """
        Set the medium of the Qiskrypt's Communication Channel.
        """

        self.communication_channel_distance_in_kms = communication_channel_distance_in_kms
        """
        Set the distance of the Qiskrypt's Communication Channel, in KMs (Kilometers).
        """

        self.operational = True
        """
        Set the boolean flag to keep information about if
        the Qiskrypt's Communication Channel is operational, initially, as True.
        """

        self.installed = False
        """
        Set the boolean flag to keep information about if
        the Qiskrypt's Communication Channel is installed, initially, as False.
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

    def get_communication_channel_context(self) -> str:
        """
        Return the context of the Qiskrypt's Communication Channel.

        :return self.communication_channel_context: the context of the Qiskrypt's Communication Channel.
        """

        """
        Return the context of the Qiskrypt's Communication Channel.
        """
        return self.communication_channel_context

    def get_communication_channel_scenario(self) -> str:
        """
        Return the scenario of the Qiskrypt's Communication Channel.

        :return self.communication_channel_scenario: the scenario of the Qiskrypt's Communication Channel.
        """

        """
        Return the scenario of the Qiskrypt's Communication Channel.
        """
        return self.communication_channel_scenario

    def get_communication_channel_medium(self) -> str:
        """
        Return the medium of the Qiskrypt's Communication Channel.

        :return self.communication_channel_medium: the medium of the Qiskrypt's Communication Channel.
        """

        """
        Return the medium of the Qiskrypt's Communication Channel.
        """
        return self.communication_channel_medium

    def get_communication_channel_distance_in_kms(self) -> float:
        """
        Return the distance of the Qiskrypt's Communication Channel, in KMs (Kilometers).

        :return self.communication_channel_distance_in_kms: the distance of the Qiskrypt's Communication Channel,
                                                            in KMs (Kilometers).
        """

        """
        Return the distance of the Qiskrypt's Communication Channel, in KMs (Kilometers).
        """
        return self.communication_channel_distance_in_kms

    def is_operational(self) -> bool:
        """
        Return the boolean flag to keep information about if
        the Qiskrypt's Communication Channel is operational.

        :return self.operational: the boolean flag to keep information about if
                                  the Qiskrypt's Communication Channel is operational.
        """

        """
        Return the boolean flag to keep information about if
        the Qiskrypt's Communication Channel is operational.
        """
        return self.operational

    def set_operational(self, operational: bool):
        """
        Set the boolean flag to keep information about if
        the Qiskrypt's Communication Channel is operational, with a given Boolean value.
        """

        if self.operational != operational:
            """
            If the boolean flag to keep information about if
            the Qiskrypt's Communication Channel is operational
            is not equal to the given Boolean value.
            """

            self.operational = operational
            """
            Set the boolean flag to keep information about if
            the Qiskrypt's Communication Channel is operational,
            with the given Boolean value.
            """

        else:
            """
            If the boolean flag to keep information about if
            the Qiskrypt's Communication Channel is operational
            is already equal to the given Boolean value.
            """

            if operational:
                """
                If the boolean flag to keep information about if
                the Qiskrypt's Communication Channel is operational,
                is already set as True.
                """

                # TODO Throw - The Qiskrypt's Communication Channel is already operational

            else:
                """
                If the boolean flag to keep information about if
                the Qiskrypt's Communication Channel is operational,
                is already set as False.
                """

                # TODO Throw - The Qiskrypt's Communication Channel is already not operational

    def is_installed(self) -> bool:
        """
        Return the boolean flag to keep information about if
        the Qiskrypt's Communication Channel is installed.

        :return self.installed: the boolean flag to keep information about if
                                the Qiskrypt's Communication Channel is installed.
        """

        """
        Return the boolean flag to keep information about if
        the Qiskrypt's Communication Channel is installed.
        """
        return self.installed

    def set_installed(self, installed: bool):
        """
        Set the boolean flag to keep information about if
        the Qiskrypt's Communication Channel is installed, with a given Boolean value.
        """

        if self.installed != installed:
            """
            If the boolean flag to keep information about if
            the Qiskrypt's Communication Channel is installed
            is not equal to the given Boolean value.
            """

            self.installed = installed
            """
            Set the boolean flag to keep information about if
            the Qiskrypt's Communication Channel is installed,
            with the given Boolean value.
            """

        else:
            """
            If the boolean flag to keep information about if
            the Qiskrypt's Communication Channel is installed
            is already equal to the given Boolean value.
            """

            if installed:
                """
                If the boolean flag to keep information about if
                the Qiskrypt's Communication Channel is installed,
                is already set as True.
                """

                # TODO Throw - The Qiskrypt's Communication Channel is already installed

            else:
                """
                If the boolean flag to keep information about if
                the Qiskrypt's Communication Channel is installed,
                is already set as False.
                """

                # TODO Throw - The Qiskrypt's Communication Channel is already not installed
