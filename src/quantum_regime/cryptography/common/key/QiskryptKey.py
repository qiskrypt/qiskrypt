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

from src.classical_regime.common.QiskryptTimestampGenerator \
    import QiskryptTimestampGenerator
"""
Import the Qiskrypt's Timestamp Generator.
"""


class QiskryptKey:
    """
    Object class for the Qiskrypt's Key.
    """

    def __init__(self, bits: str, owner_uuid: UUID):
        """
        Constructor of the Qiskrypt's Key.

        :param bits: the bits of the Qiskrypt's Key.
        :param owner_uuid: the UUID (Universally Unique IDentifier) of
                           the Qiskrypt's Party Client owning the Qiskrypt's Key.
        """

        self.bits = bits
        """
        Set the bits of the Qiskrypt's Key.
        """

        self.owner_uuid = owner_uuid
        """
        Set the UUID (Universally Unique IDentifier) of
        the Qiskrypt's Party Client owning the Qiskrypt's Key.
        """

        self.creation_timestamp = \
            QiskryptTimestampGenerator("key_timestamp_generation")\
            .get_date_and_time_initialisation_timestamp()
        """
        Set the timestamp for the creation of the Qiskrypt's Key.
        """

    def get_bits(self) -> str:
        """
        Return the bits of the Qiskrypt's Key.

        :return self.bits: the bits of the Qiskrypt's Key.
        """

        """
        Return the bits of the Qiskrypt's Key.
        """
        return self.bits

    def get_owner_uuid(self) -> UUID:
        """
        Return the UUID (Universally Unique IDentifier) of the Qiskrypt's Key.

        :return self.owner_uuid: the UUID (Universally Unique IDentifier) of the Qiskrypt's Key.
        """

        """
        Return the UUID (Universally Unique IDentifier) of the Qiskrypt's Key.
        """
        return self.owner_uuid

    def get_creation_timestamp(self) -> float:
        """
        Return the timestamp for the creation of the Qiskrypt's Key.

        :return self.creation_timestamp: the timestamp for the creation of the Qiskrypt's Key.
        """

        """
        Return the timestamp for the creation of the Qiskrypt's Key.
        """
        return self.creation_timestamp
