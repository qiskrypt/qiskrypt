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
Import required Libraries and Packages.
"""

from uuid import UUID
"""
Import the general UUID (Universally Unique IDentifier).
"""

from uuid import uuid1
"""
Import the general UUID (Universally Unique IDentifier) version 1.
"""

from uuid import uuid3
"""
Import the general UUID (Universally Unique IDentifier) version 3.
"""

from uuid import uuid4
"""
Import the general UUID (Universally Unique IDentifier) version 4.
"""

from uuid import uuid5
"""
Import the general UUID (Universally Unique IDentifier) version 5.
"""

from src.quantum_regime.networking_and_communications.mediums.QiskryptMedium \
    import QiskryptMedium
"""
Import the Qiskrypt's Medium.
"""

from src.quantum_regime.circuit.registers.quantum.QiskryptQuantumRegister \
    import QiskryptQuantumRegister
"""
Import the Qiskrypt's Quantum Register.
"""

from src.quantum_regime.circuit.registers.classical.QiskryptClassicalRegister \
    import QiskryptClassicalRegister
"""
Import the Qiskrypt's Classical Register.
"""

from src.quantum_regime.networking_and_communications.channels.QiskryptCommunicationChannel \
    import QiskryptCommunicationChannel
"""
Import the Qiskrypt's Communication Channel.
"""

from src.quantum_regime.networking_and_communications.channels.quantum.QiskryptQuantumCommunicationChannel \
    import QiskryptQuantumCommunicationChannel
"""
Import the Qiskrypt's Quantum Communication Channel.
"""

from src.quantum_regime.networking_and_communications.channels\
    .quantum.discrete_variables.QiskryptDVQuantumCommunicationChannel \
    import QiskryptDVQuantumCommunicationChannel
"""
Import the Qiskrypt's DV (Discrete Variable) Quantum Communication Channel.
"""

from src.quantum_regime.networking_and_communications.channels.classical.QiskryptClassicalCommunicationChannel \
    import QiskryptClassicalCommunicationChannel
"""
Import the Qiskrypt's Classical Communication Channel.
"""

from src.quantum_regime.true_random.random_generator.binary.QiskryptQuantumRandomBinaryGenerator \
    import QiskryptQuantumRandomBinaryGenerator
"""
Import the Qiskrypt's Quantum Random Binary Generator.
"""

from src.classical_regime.common.QiskryptClassicalUtilities \
    import QiskryptClassicalUtilities
"""
Import the Qiskrypt's Classical Utilities.
"""

from src.quantum_regime.networking_and_communications.channels.QiskryptCommunicationChannel \
    import POSSIBLE_COMMUNICATION_CHANNEL_CONTEXTS
"""
Import the available Communication Channel contexts for the Qiskrypt's Communication Channel.
"""

from src.quantum_regime.networking_and_communications.channels.QiskryptCommunicationChannel \
    import POSSIBLE_COMMUNICATION_CHANNEL_TYPES
"""
Import the available Communication Channel types for the Qiskrypt's Communication Channel.
"""

from src.quantum_regime.networking_and_communications.channels\
    .quantum.QiskryptQuantumCommunicationChannel \
    import POSSIBLE_QUANTUM_COMMUNICATION_CHANNEL_SIGNAL_VARIABLE_TYPES
"""
Import the available Communication Channel signal variable types for
the Qiskrypt's Quantum Communication Channel.
"""

from src.classical_regime.common.QiskryptClassicalUtilities \
    import SIZE_BYTE_IN_NUM_BITS
"""
Import the size of a byte in number of bits.
"""


"""
Definition of Constants and Enumerations.
"""

NUM_BYTES_FOR_UUID = 16
"""
The number of bytes to be used in an UUID (Universally Unique IDentifier)
for the Qiskrypt's Link.
"""


class QiskryptLink:
    """
    Object class for the Qiskrypt's Link.
    """

    def __init__(self, num_possible_listeners: int,
                 uuid_version=0, uuid_bytes=None, uuid_node=None,
                 uuid_clock_sequence=None, uuid_name=None, uuid_namespace=None):
        """
        Constructor of the Qiskrypt's Link.

        :param num_possible_listeners: the number of possible listeners
                                       for the Qiskrypt's Link.
        :param uuid_version: the version of the UUID (Universally Unique IDentifier)
                             for the Qiskrypt's Link.
        :param uuid_bytes: the bytes to build the UUID (Universally Unique IDentifier)
                           for the Qiskrypt's Link.
        :param uuid_node: the node to build the UUID (Universally Unique IDentifier)
                          for the Qiskrypt's Link.
        :param uuid_clock_sequence: the clock sequence to build the UUID (Universally Unique IDentifier)
                          for the Qiskrypt's Link.
        :param uuid_name: the name to build the UUID (Universally Unique IDentifier)
                          for the Qiskrypt's Link.
        :param uuid_namespace: the namespace to build the UUID (Universally Unique IDentifier)
                               for the Qiskrypt's Link.
        """

        if uuid_version == 0:
            """
            If the Qiskrypt's Link is configured with
            general UUID (Universally Unique IDentifier).
            """

            if uuid_bytes is None:
                """
                If was given specific bytes for the UUID (Universally Unique IDentifier).
                """

                quantum_random_binary_generator = \
                    QiskryptQuantumRandomBinaryGenerator("qu_rng_binary")
                """
                Create a Qiskrypt's Quantum Random Binary Generator.
                """

                quantum_random_binary_generator.initiate((NUM_BYTES_FOR_UUID * SIZE_BYTE_IN_NUM_BITS))
                """
                Initiate the Qiskrypt's Quantum Random Binary Generator, for 128 bits (16 bytes).
                """

                random_binary_string_bits = \
                    quantum_random_binary_generator.generate_binary_string()
                """
                Generate a random binary string in bits, with 128 bits (16 bytes).
                """

                random_binary_string_bytes = \
                    QiskryptClassicalUtilities.convert_binary_string_to_bytes(random_binary_string_bits)
                """
                Convert the random binary string in bits to a random binary string in bytes,
                with 128 bits (16 bytes).
                """

                self.uuid = UUID(bytes=random_binary_string_bytes)
                """
                Set the UUID (Universally Unique IDentifier) for the Qiskrypt's Link.
                """

            else:
                """
                If was not given specific bytes for the UUID (Universally Unique IDentifier).
                """

                self.uuid = UUID(bytes=uuid_bytes)
                """
                Set the UUID (Universally Unique IDentifier) for the Qiskrypt's Link.
                """

        if uuid_version == 1:
            """
            If the Qiskrypt's Link is configured with
            UUID (Universally Unique IDentifier) version 1.
            """

            self.uuid = uuid1(uuid_node, uuid_clock_sequence)
            """
            Set the UUID (Universally Unique IDentifier) for the Qiskrypt's Link.
            """

        elif uuid_version == 3:
            """
            If the Qiskrypt's Link is configured with
            UUID (Universally Unique IDentifier) version 3.
            """

            self.uuid = uuid3(uuid_namespace, uuid_name)
            """
            Set the UUID (Universally Unique IDentifier) for the Qiskrypt's Link.
            """

        elif uuid_version == 4:
            """
            If the Qiskrypt's Link is configured with
            UUID (Universally Unique IDentifier) version 4.
            """

            self.uuid = uuid4()
            """
            Set the UUID (Universally Unique IDentifier) for the Qiskrypt's Link.
            """

        elif uuid_version == 5:
            """
            If the Qiskrypt's Link is configured with
            UUID (Universally Unique IDentifier) version 5.
            """

            self.uuid = uuid5(uuid_namespace, uuid_name)
            """
            Set the UUID (Universally Unique IDentifier) for the Qiskrypt's Link.
            """

        else:
            """
            If the Qiskrypt's Link is configured with an invalid version.
            """

            # TODO Throw - Exception

        self.num_possible_listeners = num_possible_listeners
        """
        Set the number of possible listeners for the Qiskrypt's Link.
        """

        self.mediums = list()
        """
        Set the list of Qiskrypt's Mediums for the Qiskrypt's Link, initially, as an empty list.
        """

        self.communication_channel = None
        """
        Set the Qiskrypt's Communication Channel for the Qiskrypt's Link, initially, as None.
        """

        self.established = False
        """
        Set the boolean flag to keep the information about if
        the Qiskrypt's Link is established or not.
        """

        self.registers = list()
        """
        Set the Qiskrypt's Registers for the Qiskrypt's Link, initially, as an empty list.
        """

    def get_uuid(self) -> UUID:
        """
        Return the UUID (Universally Unique IDentifier) of
        the Qiskrypt's Link.

        :return self.uuid: the UUID (Universally Unique IDentifier) of
                           the Qiskrypt's Link.
        """

        """
        Return the UUID (Universally Unique IDentifier) of
        the Qiskrypt's Link.
        """
        return self.uuid

    def get_num_possible_listeners(self) -> int:
        """
        Return the number of possible listeners for the Qiskrypt's Link.

        :return self.num_possible_listeners: the number of possible listeners for
                                             the Qiskrypt's Link.
        """

        """
        Return the number of possible listeners for the Qiskrypt's Link.
        """
        return self.num_possible_listeners

    def get_mediums(self) -> list:
        """
        Return the list of Qiskrypt's Mediums of the Qiskrypt's Link.

        :return self.mediums: the list of Qiskrypt's Mediums of the Qiskrypt's Link.
        """

        if self.is_established():
            """
            If the Qiskrypt's Link is already established.
            """

            """
            Return the list of Qiskrypt's Mediums of the Qiskrypt's Link.
            """
            return self.mediums

        else:
            """
            If the Qiskrypt's Link is not established yet.
            """

            # TODO Throw - Exception

    def get_communication_channel(self) -> QiskryptCommunicationChannel:
        """
        Return the Qiskrypt's Communication Channel of the Qiskrypt's Link.

        :return self.endpoint: the Qiskrypt's Endpoint of the Qiskrypt's Link.
        """

        if self.is_established():
            """
            If the Qiskrypt's Link is already established.
            """

            """
            Return the Qiskrypt's Communication Channel of the Qiskrypt's Link.
            """
            return self.communication_channel

        else:
            """
            If the Qiskrypt's Link is not established yet.
            """

            # TODO Throw - Exception

    def is_established(self) -> bool:
        """
        Return the boolean flag to keep the information about if
        the Qiskrypt's Link is established or not.

        :return self.established: the boolean flag to keep the information about if
                                  the Qiskrypt's Link is established or not.
        """

        """
        Return the boolean flag to keep the information about if
        the Qiskrypt's Link is established or not.
        """
        return self.established

    def set_established(self, established: bool):
        """
        Set the boolean flag to keep the information about if
        the Qiskrypt's Link is established or not, with a new boolean value.

        :param established: the new boolean flag to keep the information about if
                            the Qiskrypt's Link is established or not.
        """

        if established != self.is_established():
            """
            If the boolean new boolean flag to keep the information about if
            the Qiskrypt's Link is established or not is equal to the current one.
            """

            """
            Set the boolean flag to keep the information about if
            the Qiskrypt's Link is established or not, with a new boolean value.
            """
            self.established = established

        else:
            """
            If the boolean new boolean flag to keep the information about if
            the Qiskrypt's Link is established or not is equal to the current one.
            """

            if self.is_established():
                """
                If the Qiskrypt's Link is already established.
                """

                # TODO Throw - Exception

            else:
                """
                If the Qiskrypt's Link is not established yet.
                """

                # TODO Throw - Exception

    def establish(self, mediums: list, communication_channel: QiskryptCommunicationChannel):
        """
        Establish a Qiskrypt's Link from a Qiskrypt's Medium and a Qiskrypt's Communication Channel.

        :param mediums: the list of Qiskrypt's Mediums to establish the Qiskrypt's Link.
        :param communication_channel: the Qiskrypt's Communication Channel to establish the Qiskrypt's Link.
        """

        if not self.is_established():
            """
            If the Qiskrypt's Link is not established yet
            from a Qiskrypt's Medium and a Qiskrypt's Communication Channel.
            """

            num_mediums_to_add = len(mediums)
            """
            Retrieve the number of possible Qiskrypt's Mediums to add to the Qiskrypt's Link.
            """

            if num_mediums_to_add == self.get_num_possible_listeners():
                """
                If the number of possible Qiskrypt's Mediums to add to the Qiskrypt's Link
                corresponds to the number of possible listeners of the same Qiskrypt's Link.
                """

                for current_medium_index in range(num_mediums_to_add):
                    """
                    For each object's index in the given list of possible Qiskrypt's Mediums.
                    """

                    current_medium = mediums[current_medium_index]
                    """
                    Retrieve the current object for a possible Qiskrypt's Medium.
                    """

                    if not isinstance(current_medium, QiskryptMedium):
                        """
                        Check if the current object is not a Qiskrypt's Medium.
                        """

                        # TODO Throw - Exception

                self.mediums = mediums
                """        
                Set the list of Qiskrypt's Mediums for the Qiskrypt's Link, with the given list.
                """

                self.communication_channel = communication_channel
                """
                Set the Qiskrypt's Communication Channel for the Qiskrypt's Link.
                """

                """
                Set the boolean flag to keep the information about if
                the Qiskrypt's Link is established or not, as True.
                """
                self.set_established(True)

            else:
                """
                If the number of possible Qiskrypt's Mediums to add to the Qiskrypt's Link
                does not correspond to the number of possible listeners of the same Qiskrypt's Link.
                """

                # TODO Throw - Exception

        else:
            """
            If the Qiskrypt's Link is already established
            from a Qiskrypt's Medium and a Qiskrypt's Communication Channel.
            """

            # TODO Throw - Exception

    def get_registers(self) -> list:
        """
        Return the Qiskrypt's Registers of the Qiskrypt's Link.

        :return self.registers: the Qiskrypt's Registers of the Qiskrypt's Link.
        """

        """
        Return the Qiskrypt's Registers of the Qiskrypt's Link.
        """
        return self.registers

    def get_num_registers(self) -> int:
        """
        Return the number of Qiskrypt's Registers of the Qiskrypt's Link.

        :return len(self.registers): the number of Qiskrypt's Registers of the Qiskrypt's Link.
        """

        """
        Return the number of Qiskrypt's Registers of the Qiskrypt's Link.
        """
        return len(self.registers)

    def set_quantum_registers(self, quantum_registers: list):
        """
        Set a given list of Qiskrypt's Quantum Registers to be
        the Qiskrypt's Register of the Qiskrypt's Link, if it is possible.

        :param quantum_registers: the list of possible Qiskrypt's Quantum Registers to be set as
                                  the Qiskrypt's Registers of the Qiskrypt's Link.
        """

        if self.get_num_registers() == 0:
            """
            If the Qiskrypt's Link does not have any Qiskrypt's Register yet.
            """

            num_registers_to_add = len(quantum_registers)
            """
            Retrieve the number of possible Qiskrypt's Registers to add to the Qiskrypt's Link.
            """

            if num_registers_to_add > 0:
                """
                If the list of possible Qiskrypt's Quantum Registers to be set as
                the Qiskrypt's Registers of the Qiskrypt's Link is not empty.
                """

                for current_register_index in range(num_registers_to_add):
                    """
                    For each object's index in the given list of possible Qiskrypt's Quantum Registers.
                    """

                    current_register = quantum_registers[current_register_index]
                    """
                    Retrieve the current object for a possible Qiskrypt's Quantum Register.
                    """

                    if not isinstance(current_register, QiskryptQuantumRegister):
                        """
                        Check if the current object is not a Qiskrypt's Quantum Register.
                        """

                        # TODO Throw - Exception

                communication_channel = self.get_communication_channel()
                """
                Retrieve the Qiskrypt's Communication Channel.
                """

                communication_channel_context = communication_channel.get_context()
                """
                Retrieve the context of the Qiskrypt's Communication Channel.
                """

                if (communication_channel_context == POSSIBLE_COMMUNICATION_CHANNEL_CONTEXTS[0]) and \
                        (isinstance(communication_channel, QiskryptQuantumCommunicationChannel)):
                    """
                    If the Qiskrypt's Communication Channel is in the Quantum Context and
                    it is a Qiskrypt's Quantum Communication Channel, and thus, it is valid.
                    """

                    quantum_communication_channel_signal_variable_type = \
                        communication_channel.get_signal_variable_type()
                    """
                    Retrieve the signal variable type of the Qiskrypt's Quantum Communication Channel.
                    """

                    if quantum_communication_channel_signal_variable_type == \
                       POSSIBLE_QUANTUM_COMMUNICATION_CHANNEL_SIGNAL_VARIABLE_TYPES[0]:
                        """
                        If the signal variable type of the Qiskrypt's Quantum Communication Channel
                        is represented by DVs (Discrete Variables), it can only carry one individual qubit.
                        """

                        for current_quantum_register_index in range(num_registers_to_add):
                            """
                            For each Qiskrypt's Quantum Register in
                            the given list of Qiskrypt's Quantum Registers.
                            """

                            current_quantum_register = quantum_registers[current_quantum_register_index]
                            """
                            Retrieve the current Qiskrypt's Quantum Register.
                            """

                            if isinstance(current_quantum_register, QiskryptQuantumRegister) and \
                                isinstance(communication_channel, QiskryptDVQuantumCommunicationChannel) and \
                                    (current_quantum_register.get_num_qubits() != 1):
                                """
                                Check if the current Qiskrypt's Quantum Register does not have
                                exactly one single qubit, since it should represent a
                                Qiskrypt's DV (Discrete Variable) Quantum Communication Channel,
                                which can only carry one individual qubit.
                                """

                                # TODO Throw - Exception

                    communication_channel_type = communication_channel.get_channel_type()
                    """
                    Retrieve the type of the Qiskrypt's Quantum Communication Channel.
                    """

                    if communication_channel_type == POSSIBLE_COMMUNICATION_CHANNEL_TYPES[0]:
                        """
                        If the type of the Qiskrypt's Quantum Communication Channel is Unicast (One-to-One).
                        """

                        if (num_registers_to_add == 1) and (num_registers_to_add == self.get_num_possible_listeners()):
                            """
                            Since the type of the Qiskrypt's Communication Channel is Unicast (One-to-One),
                            it can only be modeled by exactly one single Qiskrypt's Quantum Register,
                            which also represents the only one possible listener of the Qiskrypt's Link.
                            """

                            self.registers = quantum_registers
                            """
                            Set the Qiskrypt's Registers for the Qiskrypt's Link,
                            with the given list of Qiskrypt's Quantum Registers. 
                            """

                        else:
                            """
                            Since the type of the Qiskrypt's Quantum Communication Channel is Unicast (One-to-One),
                            it cannot be modeled by more than one single Qiskrypt's Quantum Register,
                            since also represents the only one possible listener of the Qiskrypt's Link.
                            """

                            # TODO Throw - Exception

                    elif communication_channel_type == POSSIBLE_COMMUNICATION_CHANNEL_TYPES[1]:
                        """
                        If the type of the Qiskrypt's Quantum Communication Channel is Broadcast (One-to-All).
                        """

                        if (num_registers_to_add >= 1) and (num_registers_to_add == self.get_num_possible_listeners()):
                            """
                            Since the type of the Qiskrypt's Quantum Communication Channel is Broadcast (One-to-All),
                            it can only be modeled by one or more Qiskrypt's Quantum Register(s),
                            but in an exactly equal number of possible listeners of the Qiskrypt's Link.
                            """

                            self.registers = quantum_registers
                            """
                            Set the Qiskrypt's Registers for the Qiskrypt's Link,
                            with the given list of Qiskrypt's Quantum Registers. 
                            """

                        else:
                            """
                            Since the type of the Qiskrypt's Quantum Communication Channel is Broadcast (One-to-All),
                            it cannot be modeled by no Qiskrypt's Quantum Register, or even,
                            by a number of Qiskrypt's Register(s) different than
                            the number of possible listeners of the Qiskrypt's Link.
                            """

                            # TODO Throw - Exception

                    elif communication_channel_type == POSSIBLE_COMMUNICATION_CHANNEL_TYPES[2]:
                        """
                        If the type of the Qiskrypt's Quantum Communication Channel is Multicast (One-to-Many).
                        """

                        if (num_registers_to_add >= 1) and (num_registers_to_add <= self.get_num_possible_listeners()):
                            """
                            Since the type of the Qiskrypt's Quantum Communication Channel is Multicast (One-to-Many),
                            it can only be modeled by one or more Qiskrypt's Quantum Register(s),
                            but in a lower number than or equal number to the number of
                            possible listeners of the Qiskrypt's Link.
                            """

                            self.registers = quantum_registers
                            """
                            Set the Qiskrypt's Registers for the Qiskrypt's Link,
                            with the given list of Qiskrypt's Quantum Registers. 
                            """

                        else:
                            """
                            Since the type of the Qiskrypt's Quantum Communication Channel is Multicast (One-to-Many),
                            it cannot be modeled by no Qiskrypt's Quantum Register, or even,
                            by a number of Qiskrypt's Register(s) greater than
                            the number of possible listeners of the Qiskrypt's Link.
                            """

                            # TODO Throw - Exception

                    elif communication_channel_type == POSSIBLE_COMMUNICATION_CHANNEL_TYPES[3]:
                        """
                        If the type of the Qiskrypt's Quantum Communication Channel is Anycast (One-to-Any).
                        """

                        if (num_registers_to_add == 1) and (num_registers_to_add <= self.get_num_possible_listeners()):
                            """
                            Since the type of the Qiskrypt's Quantum Communication Channel is Anycast (One-to-Any),
                            it can only be modeled by exactly one single Qiskrypt's Quantum Register,
                            which also represents one of the one or more possible listener(s) of the Qiskrypt's Link.
                            """

                            self.registers = quantum_registers
                            """
                            Set the Qiskrypt's Registers for the Qiskrypt's Link,
                            with the given list of Qiskrypt's Quantum Registers. 
                            """

                        else:
                            """
                            Since the type of the Qiskrypt's Quantum Communication Channel is Anycast (One-to-Any),
                            it cannot be modeled by more than one single Qiskrypt's Quantum Register, or even,
                            by a number of Qiskrypt's Register(s) greater than
                            the number of possible listeners of the Qiskrypt's Link.
                            """

                            # TODO Throw - Exception

                else:
                    """
                    If the Qiskrypt's Communication Channel is not in the Quantum Context neither
                    it is a Qiskrypt's Quantum Communication Channel, and thus, it is not valid.
                    """

                    # TODO Throw - Exception

            else:
                """
                If the list of possible Qiskrypt's Quantum Registers to be set as
                the Qiskrypt's Registers of the Qiskrypt's Link is empty.
                """

                # TODO Throw - Exception

        else:
            """
            If the Qiskrypt's Link does already have some Qiskrypt's Register.
            """

            # TODO Throw - Exception

    def set_classical_registers(self, classical_registers: list):
        """
        Set a given list of Qiskrypt's Classical Registers to be
        the Qiskrypt's Register of the Qiskrypt's Link, if it is possible.

        :param classical_registers: the list of Qiskrypt's Classical Register to be set as
                                    the Qiskrypt's Register of the Qiskrypt's Link.
        """

        if self.is_established():
            """
            If the Qiskrypt's Link is already established
            from a Qiskrypt's Medium and a Qiskrypt's Communication Channel.
            """

            self.registers = classical_registers
            """
            Set the given Qiskrypt's Classical Register to be
            the Qiskrypt's Register of the Qiskrypt's Link
            """

        else:
            """
            If the Qiskrypt's Link is not established yet
            from a Qiskrypt's Medium and a Qiskrypt's Communication Channel.
            """

            # TODO Throw - Exception
