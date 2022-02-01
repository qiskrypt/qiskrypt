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

POSSIBLE_COMMUNICATION_CHANNEL_CONTEXTS = ["QUANTUM", "CLASSICAL"]
"""
The available Communication Channel contexts for the Qiskrypt's Communication Channel.
"""

POSSIBLE_COMMUNICATION_CHANNEL_SCENARIOS = ["NOISELESS", "NOISY"]
"""
The available Communication Channel scenarios for the Qiskrypt's Communication Channel.
"""

POSSIBLE_COMMUNICATION_CHANNEL_TYPES = ["UNICAST (ONE-TO-ONE)", "BROADCAST (ONE-TO-ALL)",
                                        "MULTICAST (ONE-TO-MANY)", "ANYCAST (ONE-TO-ANY)"]
"""
The available Communication Channel types for the Qiskrypt's Communication Channel.
"""

POSSIBLE_COMMUNICATION_CHANNEL_DIRECTIONS = ["G2G (GROUND-TO-GROUND)", "G2S (GROUND-TO-SATELLITE)",
                                             "S2G (SATELLITE-TO-GROUND)", "S2S (SATELLITE-TO-SATELLITE)",
                                             "UPLINK", "DOWNLINK", "FORWARD LINK", "REVERSE LINK",
                                             "FORWARD LINK (UPLINK)", "FORWARD LINK (DOWNLINK)",
                                             "REVERSE LINK (UPLINK)", "REVERSE LINK (DOWNLINK)"]
"""
The available Communication Channel directions for the Qiskrypt's Communication Channel.
"""


class QiskryptCommunicationChannel:
    """
    Object class for the Qiskrypt's Communication Channel.
    """

    def __init__(self, num: int, name: str, context: str, scenario: str,
                 channel_type: str, directions: list):
        """
        Constructor of the Qiskrypt's Communication Channel.

        :param num: the number of the Qiskrypt's Communication Channel.
        :param name: the name of the Qiskrypt's Communication Channel.
        :param context: the context of the Qiskrypt's Communication Channel.
        :param scenario: the scenario of the Qiskrypt's Communication Channel.
        :param channel_type: the type of the Qiskrypt's Communication Channel.
        :param directions: the list of directions of the Qiskrypt's Communication Channel.
        """

        self.num = num
        """
        Set the number of the Qiskrypt's Communication Channel.
        """

        self.name = name
        """
        Set the name of the Qiskrypt's Communication Channel.
        """

        self.context = context
        """
        Set the context of the Qiskrypt's Communication Channel.
        """

        self.scenario = scenario
        """
        Set the scenario of the Qiskrypt's Communication Channel.
        """

        self.channel_type = channel_type
        """
        Set the type of the Qiskrypt's Communication Channel.
        """

        if directions is not None:
            """
            If some direction is given to the Qiskrypt's Communication Channel.
            """

            self.directions = list()
            """
            Initialise the list of directions of the Qiskrypt's Communication,
            initially, as an empty list.
            """

            for current_direction_index in range(len(directions)):
                """
                For each index of the possibly given directions for
                the Qiskrypt's Communication Channel.
                """

                current_direction = directions[current_direction_index]
                """
                Retrieve the current possible direction for the Qiskrypt's Communication Channel.
                """

                if current_direction in POSSIBLE_COMMUNICATION_CHANNEL_DIRECTIONS:
                    """
                    If the current direction of the Qiskrypt's Communication Channel is valid.
                    """

                    self.directions.append(current_direction)
                    """
                    Append the current direction to the list of directions of
                    the Qiskrypt's Communication Channel.
                    """

                else:
                    """
                    If the current direction of the Qiskrypt's Communication Channel is not valid.
                    """

                    # TODO Throw - Exception

        else:
            """
            If no direction is given to the Qiskrypt's Communication Channel.
            """

            self.directions = list()
            """
            Set the list of directions of the Qiskrypt's Communication Channel, as an empty list.
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

    def get_num(self) -> int:
        """
        Return the number of the Qiskrypt's Communication Channel.

        :return self.num: the number of the Qiskrypt's Communication Channel.
        """

        """
        Return the number of the Qiskrypt's Communication Channel.
        """
        return self.num

    def get_name(self) -> str:
        """
        Return the name of the Qiskrypt's Communication Channel.

        :return self.name: the name of the Qiskrypt's Communication Channel.
        """

        """
        Return the name of the Qiskrypt's Communication Channel.
        """
        return self.name

    def get_context(self) -> str:
        """
        Return the context of the Qiskrypt's Communication Channel.

        :return self.context: the context of the Qiskrypt's Communication Channel.
        """

        """
        Return the context of the Qiskrypt's Communication Channel.
        """
        return self.context

    def get_scenario(self) -> str:
        """
        Return the scenario of the Qiskrypt's Communication Channel.

        :return self.scenario: the scenario of the Qiskrypt's Communication Channel.
        """

        """
        Return the scenario of the Qiskrypt's Communication Channel.
        """
        return self.scenario

    def get_channel_type(self) -> str:
        """
        Return the type of the Qiskrypt's Communication Channel.

        :return self.channel_type: the type of the Qiskrypt's Communication Channel.
        """

        """
        Return the type of the Qiskrypt's Communication Channel.
        """
        return self.channel_type

    def get_directions(self) -> list:
        """
        Return the list of directions of the Qiskrypt's Communication Channel.

        :return self.directions: the list of directions of the Qiskrypt's Communication Channel.
        """

        """
        Return the list of directions of the Qiskrypt's Communication Channel.
        """
        return self.directions

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

        if self.is_operational() != operational:
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

        if self.is_installed() != installed:
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
