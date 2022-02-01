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
for the Qiskrypt's Client.
"""


class QiskryptClient:
    """
    Object class for the Qiskrypt's Client.
    """

    def __init__(self, uuid_version=0, uuid_bytes=None, uuid_node=None,
                 uuid_clock_sequence=None, uuid_name=None, uuid_namespace=None):
        """
        Constructor of the Qiskrypt's Client.

        :param uuid_version: the version of the UUID (Universally Unique IDentifier)
                             for the Qiskrypt's Client.
        :param uuid_bytes: the bytes to build the UUID (Universally Unique IDentifier)
                           for the Qiskrypt's Client.
        :param uuid_node: the node to build the UUID (Universally Unique IDentifier)
                          for the Qiskrypt's Client.
        :param uuid_clock_sequence: the clock sequence to build the UUID (Universally Unique IDentifier)
                          for the Qiskrypt's Client.
        :param uuid_name: the name to build the UUID (Universally Unique IDentifier)
                          for the Qiskrypt's Client.
        :param uuid_namespace: the namespace to build the UUID (Universally Unique IDentifier)
                               for the Qiskrypt's Client.
        """

        if uuid_version == 0:
            """
            If the Qiskrypt's Client is configured with
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
                Set the UUID (Universally Unique IDentifier) for the Qiskrypt's Client.
                """

            else:
                """
                If was not given specific bytes for the UUID (Universally Unique IDentifier).
                """

                self.uuid = UUID(bytes=uuid_bytes)
                """
                Set the UUID (Universally Unique IDentifier) for the Qiskrypt's Client.
                """

        elif uuid_version == 1:
            """
            If the Qiskrypt's Client is configured with
            UUID (Universally Unique IDentifier) version 1.
            """

            self.uuid = uuid1(uuid_node, uuid_clock_sequence)
            """
            Set the UUID (Universally Unique IDentifier) for the Qiskrypt's Client.
            """

        elif uuid_version == 3:
            """
            If the Qiskrypt's Client is configured with
            UUID (Universally Unique IDentifier) version 3.
            """

            self.uuid = uuid3(uuid_namespace, uuid_name)
            """
            Set the UUID (Universally Unique IDentifier) for the Qiskrypt's Client.
            """

        elif uuid_version == 4:
            """
            If the Qiskrypt's Client is configured with
            UUID (Universally Unique IDentifier) version 4.
            """

            self.uuid = uuid4()
            """
            Set the UUID (Universally Unique IDentifier) for the Qiskrypt's Client.
            """

        elif uuid_version == 5:
            """
            If the Qiskrypt's Client is configured with
            UUID (Universally Unique IDentifier) version 5.
            """

            self.uuid = uuid5(uuid_namespace, uuid_name)
            """
            Set the UUID (Universally Unique IDentifier) for the Qiskrypt's Client.
            """

        else:
            """
            If the Qiskrypt's Client is configured with an invalid version.
            """

            # TODO Throw - Exception

        self.connected = False
        """
        Set the boolean flag to keep the information about if
        the Qiskrypt's Client is connected or not.
        """

        self.registers = []
        """
        Set the Qiskrypt's Registers for the Qiskrypt's Client, as an initially empty list.
        """

    def get_uuid(self) -> UUID:
        """
        Return the UUID (Universally Unique IDentifier) of
        the Qiskrypt's Client.

        :return self.uuid: the UUID (Universally Unique IDentifier) of
                           the Qiskrypt's Client.
        """

        """
        Return the UUID (Universally Unique IDentifier) of
        the Qiskrypt's Client.
        """
        return self.uuid

    def is_connected(self) -> bool:
        """
        Return the boolean flag to keep the information about if
        the Qiskrypt's Client is connected or not.

        :return self.connected: the boolean flag to keep the information about if
                                the Qiskrypt's Client is connected or not.
        """

        """
        Return the boolean flag to keep the information about if
        the Qiskrypt's Client is connected or not.
        """
        return self.connected

    def set_connected(self, connected: bool):
        """
        Set the boolean flag to keep the information about if
        the Qiskrypt's Client is connected or not, with a new boolean value.

        :param connected: the new boolean flag to keep the information about if
                          the Qiskrypt's Client is connected or not.
        """

        if connected != self.is_connected():
            """
            If the boolean new boolean flag to keep the information about if
            the Qiskrypt's Client is connected or not is equal to the current one.
            """

            """
            Set the boolean flag to keep the information about if
            the Qiskrypt's Client is connected or not, with a new boolean value.
            """
            self.connected = connected

        else:
            """
            If the boolean new boolean flag to keep the information about if
            the Qiskrypt's Client is connected or not is equal to the current one.
            """

            if self.is_connected():
                """
                If the Qiskrypt's Client is already connected.
                """

                # TODO Throw - Exception

            else:
                """
                If the Qiskrypt's Client is not connected yet.
                """

                # TODO Throw - Exception

    def get_registers(self) -> list:
        """
        Return the Qiskrypt's Registers of the Qiskrypt's Client.

        :return self.registers: the Qiskrypt's Registers of the Qiskrypt's Client.
        """

        """
        Return the Qiskrypt's Registers of the Qiskrypt's Client.
        """
        return self.registers

    def get_num_registers(self) -> int:
        """
        Return the number of Qiskrypt's Registers in
        the list of Qiskrypt's Registers of the Qiskrypt's Client.

        :return len(self.registers): the number of Qiskrypt's Registers in
                                     the list of Qiskrypt's Registers of
                                     the Qiskrypt's Client.
        """

        """
        Return the number of Qiskrypt's Registers in
        the list of Qiskrypt's Registers of the Qiskrypt's Client.
        """
        return len(self.registers)
