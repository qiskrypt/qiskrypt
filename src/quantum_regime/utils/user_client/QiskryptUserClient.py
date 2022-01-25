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

from src.quantum_regime.utils.parties_and_agents.QiskryptParty \
    import QiskryptParty
"""
Import the Qiskrypt's Party.
"""


class QiskryptUserClient:
    """
    Object class for the Qiskrypt's User Client.
    """

    def __init__(self, party: QiskryptParty,
                 uuid_version=0, uuid_bytes=None, uuid_node=None,
                 uuid_clock_sequence=None, uuid_name=None, uuid_namespace=None):
        """
        Constructor of the Qiskrypt's User Client.

        :param party:
        :param uuid_version:
        :param uuid_bytes:
        :param uuid_node:
        :param uuid_clock_sequence:
        :param uuid_name:
        :param uuid_namespace:
        """

        if uuid_version == 0:
            """
            If the Qiskrypt's User Client is configured with
            general UUID (Universally Unique IDentifier).
            """

            if uuid_bytes is not None:
                """
                If was given specific bytes for the UUID (Universally Unique IDentifier).
                """

                self.uuid = UUID(bytes=uuid_bytes)
                """
                Set the UUID (Universally Unique IDentifier) for the Qiskrypt's User Client.
                """

            else:
                """
                If was not given specific bytes for the UUID (Universally Unique IDentifier).
                """

                # TODO - Generate a binary string

                self.uuid = UUID(bytes=uuid_bytes)
                """
                Set the UUID (Universally Unique IDentifier) for the Qiskrypt's User Client.
                """

        if uuid_version == 1:
            """
            If the Qiskrypt's User Client is configured with
            UUID (Universally Unique IDentifier) version 1.
            """

            self.uuid = uuid1(uuid_node, uuid_clock_sequence)
            """
            Set the UUID (Universally Unique IDentifier) for the Qiskrypt's User Client.
            """

        elif uuid_version == 3:
            """
            If the Qiskrypt's User Client is configured with
            UUID (Universally Unique IDentifier) version 3.
            """

            self.uuid = uuid3(uuid_namespace, uuid_name)
            """
            Set the UUID (Universally Unique IDentifier) for the Qiskrypt's User Client.
            """

        elif uuid_version == 4:
            """
            If the Qiskrypt's User Client is configured with
            UUID (Universally Unique IDentifier) version 4.
            """

            self.uuid = uuid4()
            """
            Set the UUID (Universally Unique IDentifier) for the Qiskrypt's User Client.
            """

        elif uuid_version == 5:
            """
            If the Qiskrypt's User Client is configured with
            UUID (Universally Unique IDentifier) version 5.
            """

            self.uuid = uuid5(uuid_namespace, uuid_name)
            """
            Set the UUID (Universally Unique IDentifier) for the Qiskrypt's User Client.
            """

        else:
            """
            If the Qiskrypt's User Client is configured with an invalid version.
            """

            # TODO Throw - Exception

        self.party = party
        """
        Set the Qiskrypt's Party for the Qiskrypt's User Client.
        """

        self.registers = []
        """
        Set the Qiskrypt's Register
        """
