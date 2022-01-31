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

    def __init__(self, uuid_version=0, uuid_bytes=None, uuid_node=None,
                 uuid_clock_sequence=None, uuid_name=None, uuid_namespace=None):
        """
        Constructor of the Qiskrypt's Link.

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

        self.medium = None
        """
        Set the Qiskrypt's Medium for the Qiskrypt's Link, initially, as None.
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

        self.register = None
        """
        Set the Qiskrypt's Register for the Qiskrypt's Link, initially, as None.
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

    def get_medium(self) -> QiskryptMedium:
        """
        Return the Qiskrypt's Medium of the Qiskrypt's Link.

        :return self.medium: the Qiskrypt's Medium of the Qiskrypt's Link.
        """

        if self.is_established():
            """
            If the Qiskrypt's Link is already established.
            """

            """
            Return the Qiskrypt's Medium of the Qiskrypt's Link.
            """
            return self.medium

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

    def establish(self, medium: QiskryptMedium, communication_channel: QiskryptCommunicationChannel):
        """
        Establish a Qiskrypt's Link from a Qiskrypt's Medium and a Qiskrypt's Communication Channel.

        :param medium: the Qiskrypt's Medium to establish the Qiskrypt's Link.
        :param communication_channel: the Qiskrypt's Communication Channel to establish the Qiskrypt's Link.
        """

        if not self.is_established():
            """
            If the Qiskrypt's Link is not established yet
            from a Qiskrypt's Medium and a Qiskrypt's Communication Channel.
            """

            self.medium = medium
            """
            Set the Qiskrypt's Medium for the Qiskrypt's Link.
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
            If the Qiskrypt's Link is already established
            from a Qiskrypt's Medium and a Qiskrypt's Communication Channel.
            """

            # TODO Throw - Exception

    def get_register(self) -> list:
        """
        Return the Qiskrypt's Register of the Qiskrypt's Link.

        :return self.register: the Qiskrypt's Register of the Qiskrypt's Link.
        """

        """
        Return the Qiskrypt's Register of the Qiskrypt's Link.
        """
        return self.register

    def set_quantum_register(self, quantum_register: QiskryptQuantumRegister):
        """
        Set a given Qiskrypt's Quantum Register to be
        the Qiskrypt's Register of the Qiskrypt's Link, if it is possible.

        :param quantum_register: the Qiskrypt's Quantum Register to be set as
                                 the Qiskrypt's Register of the Qiskrypt's Link.
        """

    def set_classical_register(self, classical_register: QiskryptClassicalRegister):
        """
        Set a given Qiskrypt's Classical Register to be
        the Qiskrypt's Register of the Qiskrypt's Link, if it is possible.

        :param classical_register: the Qiskrypt's Classical Register to be set as
                                   the Qiskrypt's Register of the Qiskrypt's Link.
        """

        if self.is_established():
            """
            If the Qiskrypt's Link is already established
            from a Qiskrypt's Medium and a Qiskrypt's Communication Channel.
            """

            self.register = classical_register
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
