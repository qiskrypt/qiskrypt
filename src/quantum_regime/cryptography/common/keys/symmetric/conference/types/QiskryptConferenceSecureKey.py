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

from src.quantum_regime.cryptography.common.keys.symmetric.conference.QiskryptConferenceKey \
    import QiskryptConferenceKey
"""
Import the Qiskrypt's Conference Key.
"""

from src.quantum_regime.cryptography.common.keys.QiskryptKey \
    import POSSIBLE_KEY_TYPES
"""
Import the available types of keys for the Qiskrypt's Key.
"""


class QiskryptConferenceReconciledKey(QiskryptConferenceKey):
    """
    Object class for the Qiskrypt's Conference Reconciled Key.
    """

    def __init__(self, bits: str, owner_uuid: UUID):
        """
        Constructor of the Qiskrypt's Conference Reconciled Key.

        :param bits: the bits of the Qiskrypt's Key.
        :param owner_uuid: the UUID (Universally Unique IDentifier) of
                           the Qiskrypt's Party Client owning the Qiskrypt's Key.
        """

        super().__init__(bits, owner_uuid, POSSIBLE_KEY_TYPES[3], True)
        """
        Call of the constructor of the super-class Qiskrypt's Conference Key.
        """

    def get_bits(self) -> str:
        """
        Return the bits of the Qiskrypt's Key.

        :return super().get_bits(): the bits of the Qiskrypt's Key.
        """

        """
        Return the bits of the Qiskrypt's Key.
        """
        return super().get_bits()

    def get_owner_uuid(self) -> UUID:
        """
        Return the UUID (Universally Unique IDentifier) of the Qiskrypt's Key.

        :return super().get_owner_uuid(): the UUID (Universally Unique IDentifier) of
                                          the Qiskrypt's Key.
        """

        """
        Return the UUID (Universally Unique IDentifier) of the Qiskrypt's Key.
        """
        return super().get_owner_uuid()

    def get_key_category(self) -> str:
        """
        Return the category of the Qiskrypt's Key.

        :return super().get_key_category(): the category of the Qiskrypt's Key.
        """

        """
        Return the category of the Qiskrypt's Key.
        """
        return super().get_key_category()

    def get_key_privacy_level(self) -> str:
        """
        Return the privacy level of the Qiskrypt's Key.

        :return super().get_key_privacy_level(): the privacy level of the Qiskrypt's Key.
        """

        """
        Return the privacy level of the Qiskrypt's Key.
        """
        return super().get_key_privacy_level()

    def get_key_type(self) -> str:
        """
        Return the type of the Qiskrypt's Key.

        :return super().get_key_type(): the type of the Qiskrypt's Key.
        """

        """
        Return the type of the Qiskrypt's Key.
        """
        return super().get_key_type()

    def is_final(self) -> bool:
        """
        Return the boolean flag to keep the information about if
        the Qiskrypt's Key is final or not.

        :return super().is_final(): the boolean flag to keep the information about if
                                    the Qiskrypt's Key is final or not.
        """

        """
        Return the boolean flag to keep the information about if
        the Qiskrypt's Key is final or not.
        """
        return super().is_final()

    def get_creation_timestamp(self) -> float:
        """
        Return the timestamp for the creation of the Qiskrypt's Key.

        :return super().get_creation_timestamp(): the timestamp for the creation of
                                                  the Qiskrypt's Key.
        """

        """
        Return the timestamp for the creation of the Qiskrypt's Key.
        """
        return super().get_creation_timestamp()
