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

from src.quantum_regime.networking_and_communications.mediums.QiskryptMedium \
    import QiskryptMedium
"""
Import the Qiskrypt's Medium.
"""

from src.quantum_regime.networking_and_communications.mediums.QiskryptMedium \
    import POSSIBLE_MEDIUM_TYPES
"""
Import the available medium types for the Qiskrypt's Medium.
"""


class QiskryptFreeSpaceOpticMedium(QiskryptMedium):
    """
    Object class for the Qiskrypt's Free-Space Optic Medium.
    """

    def __init__(self, num: int, name: str,
                 medium_length_in_kms: float):
        """
        Constructor of the Qiskrypt's Free-Space Optic Medium.

        :param num: the number of the Qiskrypt's Medium.
        :param name: the name of the Qiskrypt's Medium.
        :param medium_length_in_kms: the length in KMs (Kilometers) of the Qiskrypt's Medium.
        """

        super().__init__(num, name, POSSIBLE_MEDIUM_TYPES[1], medium_length_in_kms)
        """
        Call of the constructor of the super-class Qiskrypt's Medium.
        """

    def get_num(self) -> int:
        """
        Return the number of the Qiskrypt's Medium.

        :return super().get_num(): the number of the Qiskrypt's Medium.
        """

        """
        Return the number of the Qiskrypt's Medium.
        """
        return super().get_num()

    def get_name(self) -> str:
        """
        Return the name of the Qiskrypt's Medium.

        :return super().get_name(): the name of the Qiskrypt's Medium.
        """

        """
        Return the name of the Qiskrypt's Medium.
        """
        return super().get_name()

    def get_medium_type(self) -> str:
        """
        Return the type of the Qiskrypt's Medium.

        :return super().get_medium_type(): the type of the Qiskrypt's Medium.
        """

        """
        Return the type of the Qiskrypt's Medium.
        """
        return super().get_medium_type()

    def get_medium_length_in_kms(self) -> float:
        """
        Return the length in KMs (Kilometers) of the Qiskrypt's Medium.

        :return self.medium_length_in_kms: the type of the Qiskrypt's Medium.
        """

        """
        Return the length in KMs (Kilometers) of the Qiskrypt's Medium.
        """
        return super().get_medium_length_in_kms()

    def __str__(self) -> str:
        """
        Return the string representation for the Qiskrypt's Medium.

        :return super().__str__(): the string representation for the Qiskrypt's Medium.
        """

        """
        Return the string representation for the Qiskrypt's Medium.
        """
        return super().__str__()
