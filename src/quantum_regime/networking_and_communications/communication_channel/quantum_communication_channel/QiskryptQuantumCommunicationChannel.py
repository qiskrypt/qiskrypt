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

from src.quantum_regime.networking_and_communications.communication_channel.QiskryptCommunicationChannel \
    import QiskryptCommunicationChannel
"""
Import Qiskrypt's Communication Channel.
"""

from src.quantum_regime.circuit.registers.quantum.QiskryptQuantumRegister \
    import QiskryptQuantumRegister
"""
Import Qiskrypt's Quantum Register.
"""

from src.quantum_regime.networking_and_communications.communication_channel.QiskryptCommunicationChannel \
    import POSSIBLE_COMMUNICATION_CHANNEL_CONTEXTS
"""
Import the available Communication Channel contexts for
the Qiskrypt's Communication Channels.
"""


"""
Definition of Constants and Enumerations.
"""

POSSIBLE_COMMUNICATION_CHANNEL_SIGNAL_VARIABLE_TYPES = ["DISCRETE", "CONTINUOUS"]
"""
The available Quantum Communication Channel signal variable types for
the Qiskrypt's Quantum Communication Channel.
"""


class QiskryptQuantumCommunicationChannel(QiskryptCommunicationChannel):
    """
    Object class for the Qiskrypt's Quantum Communication Channel.
    """

    def __init__(self, communication_channel_num: int, communication_channel_name: str,
                 communication_channel_scenario: str, communication_channel_medium: str,
                 communication_channel_distance_in_kms: float,
                 quantum_communication_channel_signal_variable_type: str):
        """
        Constructor of the Qiskrypt's Quantum Communication Channel.

        :param communication_channel_num: the number of the Qiskrypt's Communication Channel.
        :param communication_channel_name: the name of the Qiskrypt's Communication Channel.
        :param communication_channel_scenario: the scenario of the Qiskrypt's Communication Channel.
        :param communication_channel_medium: the medium of the Qiskrypt's Communication Channel.
        :param communication_channel_distance_in_kms: the distance of the Qiskrypt's Communication Channel,
                                                      in KMs (Kilometers).
        :param quantum_communication_channel_signal_variable_type: the signal variable type of the Qiskrypt's
                                                                   Quantum Communication Channel.
        """
        super().__init__(communication_channel_num, communication_channel_name,
                         POSSIBLE_COMMUNICATION_CHANNEL_CONTEXTS[0], communication_channel_scenario,
                         communication_channel_medium, communication_channel_distance_in_kms)
        """
        Call of the constructor of the super-class Qiskrypt's Communication Channel.
        """

        self.quantum_communication_channel_signal_variable_type = \
            quantum_communication_channel_signal_variable_type
        """
        Set the signal variable type of the Qiskrypt's Quantum Communication Channel.
        """

        self.quantum_register = None
        """
        Set the Qiskrypt's Quantum Register of the Qiskrypt's
        Quantum Communication Channel, initially, as None.
        """

    def get_communication_channel_num(self) -> int:
        """
        Return the number of the Qiskrypt's Communication Channel.

        :return super().get_communication_channel_num(): the number of the Qiskrypt's
                                                         Communication Channel.
        """

        """
        Return the number of the Qiskrypt's Communication Channel.
        """
        return super().get_communication_channel_num()

    def get_communication_channel_name(self) -> str:
        """
        Return the name of the Qiskrypt's Communication Channel.

        :return super().get_communication_channel_name(): the name of the Qiskrypt's
                                                          Communication Channel.
        """

        """
        Return the name of the Qiskrypt's Communication Channel.
        """
        return super().get_communication_channel_name()

    def get_communication_channel_context(self) -> str:
        """
        Return the context of the Qiskrypt's Communication Channel.

        :return super().get_communication_channel_context(): the context of the Qiskrypt's
                                                             Communication Channel.
        """

        """
        Return the context of the Qiskrypt's Communication Channel.
        """
        return super().get_communication_channel_context()

    def get_communication_channel_scenario(self) -> str:
        """
        Return the scenario of the Qiskrypt's Communication Channel.

        :return super().get_communication_channel_scenario(): the scenario of the Qiskrypt's
                                                              Communication Channel.
        """

        """
        Return the scenario of the Qiskrypt's Communication Channel.
        """
        return super().get_communication_channel_scenario()

    def get_communication_channel_medium(self) -> str:
        """
        Return the medium of the Qiskrypt's Communication Channel.

        :return super().get_communication_channel_medium(): the medium of the Qiskrypt's
                                                            Communication Channel.
        """

        """
        Return the medium of the Qiskrypt's Communication Channel.
        """
        return super().get_communication_channel_medium()

    def get_communication_channel_distance_in_kms(self) -> float:
        """
        Return the distance of the Qiskrypt's Communication Channel, in KMs (Kilometers).

        :return super().get_communication_channel_distance_in_kms(): the distance of the Qiskrypt's
                                                                     Communication Channel, in KMs (Kilometers).
        """

        """
        Return the distance of the Qiskrypt's Communication Channel, in KMs (Kilometers).
        """
        return super().get_communication_channel_distance_in_kms()

    def get_quantum_communication_channel_signal_variable_type(self) -> str:
        """
        Return the signal variable type of the Qiskrypt's Quantum Communication Channel.

        :return self.quantum_communication_channel_signal_variable_type: the signal variable type of the
                                                                         Qiskrypt's Quantum Communication Channel.
        """

        """
        Return the signal variable type of the Qiskrypt's Quantum Communication Channel.        
        """
        return self.quantum_communication_channel_signal_variable_type

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

        """
        Set the boolean flag to keep information about if
        the Qiskrypt's Communication Channel is operational, with a given Boolean value.
        """
        super().set_operational(operational)

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

        """
        Set the boolean flag to keep information about if
        the Qiskrypt's Communication Channel is installed, with a given Boolean value.
        """
        super().set_installed(installed)

    def is_started(self) -> bool:
        """
        Return the boolean flag to keep information about if
        the Qiskrypt's Communication Channel is started.

        :return super().is_handling_communication(): the boolean flag to keep information about if
                                                     the Qiskrypt's Communication Channel is started.
        """

        """
        Return the boolean flag to keep information about if
        the Qiskrypt's Communication Channel is started.
        """
        return super().is_started()

    def set_started(self, started: bool):
        """
        Set the boolean flag to keep information about if
        the Qiskrypt's Communication Channel is started,
        with a given Boolean value.
        """

        super().set_started(started)
        """
        Set the boolean flag to keep information about if
        the Qiskrypt's Communication Channel is started,
        with the given Boolean value.
        """

    def start(self):
        """
        Starts the Qiskrypt's Quantum Communication Channel.
        """

        if not self.is_started():
            """
            If the Qiskrypt's Quantum Communication Channel is not started yet.
            """

            self.quantum_register = \
                QiskryptQuantumRegister(name=self.get_communication_channel_name())
            """
            Initialise the Qiskrypt's Quantum Register of the Qiskrypt's
            Quantum Communication Channel.
            """

            """
            Set the boolean flag to keep information about if
            the Qiskrypt's Communication Channel is started, as True.
            """
            self.set_started(True)

        else:
            """
            If the Qiskrypt's Quantum Communication Channel is already started.
            """

            # TODO Throw - Exception

    def reset(self):
        """
        Resets the Qiskrypt's Quantum Communication Channel.
        """

        if self.is_started():
            """
            If the Qiskrypt's Quantum Communication Channel is already started.
            """

            quantum_register_name = "{}-{}".format(self.get_communication_channel_name(),
                                                   self.get_communication_channel_num())
            """
            Set the name for the Qiskrypt's Quantum Register.
            """

            self.quantum_register = \
                QiskryptQuantumRegister(name=quantum_register_name)
            """
            Initialise the Qiskrypt's Quantum Register of the Qiskrypt's
            Quantum Communication Channel.
            """

        else:
            """
            If the Qiskrypt's Quantum Communication Channel is not started yet.
            """

            # TODO Throw - Exception

    def stop(self):
        """
        Stops the Qiskrypt's Quantum Communication Channel.
        """

        if self.is_started():
            """
            If the Qiskrypt's Quantum Communication Channel is already started.
            """

            self.quantum_register = None
            """
            Set the Qiskrypt's Quantum Register of the Qiskrypt's
            Quantum Communication Channel, as None.
            """

            """
            Set the boolean flag to keep information about if
            the Qiskrypt's Communication Channel is started, as False.
            """
            self.set_started(False)

        else:
            """
            If the Qiskrypt's Quantum Communication Channel is not started yet.
            """

            # TODO Throw - Exception

    def get_quantum_register(self):
        """
        Return the Qiskrypt's Quantum Register of the Qiskrypt's
        Quantum Communication Channel.

        :return self.quantum_register: the Qiskrypt's Quantum Register of the Qiskrypt's
                                       Quantum Communication Channel.
        """

        """
        Return the Qiskrypt's Quantum Register of the Qiskrypt's
        Quantum Communication Channel.
        """
        return self.quantum_register
