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
Definition of Constants and Enumerations.
"""

POSSIBLE_MEDIUM_TYPES = ["FIBER-OPTIC", "FREE-SPACE-OPTIC"]
"""
The available medium types for the Qiskrypt's Medium.
"""


class QiskryptMedium:
    """
    Object class for the Qiskrypt's Medium.
    """

    def __init__(self, num: int, name: str,
                 medium_type: str, length_in_kms: float):
        """
        Constructor of the Qiskrypt's Medium.

        :param num: the number of the Qiskrypt's Medium.
        :param name: the name of the Qiskrypt's Medium.
        :param medium_type: the type of the Qiskrypt's Medium.
        :param length_in_kms: the length in KMs (Kilometers) of the Qiskrypt's Medium.
        """

        self.num = num
        """
        Set the number of the Qiskrypt's Medium.
        """

        self.name = name
        """
        Set the name of the Qiskrypt's Medium.
        """

        self.medium_type = medium_type
        """
        Set the type of the Qiskrypt's Medium.
        """

        self.length_in_kms = length_in_kms
        """
        Set the length in KMs (Kilometers) of the Qiskrypt's Medium.
        """

    def get_num(self) -> int:
        """
        Return the number of the Qiskrypt's Medium.

        :return self.num: the number of the Qiskrypt's Medium.
        """

        """
        Return the number of the Qiskrypt's Medium.
        """
        return self.num

    def get_name(self) -> str:
        """
        Return the name of the Qiskrypt's Medium.

        :return self.name: the name of the Qiskrypt's Medium.
        """

        """
        Return the name of the Qiskrypt's Medium.
        """
        return self.name

    def get_medium_type(self) -> str:
        """
        Return the type of the Qiskrypt's Medium.

        :return self.medium_type: the type of the Qiskrypt's Medium.
        """

        """
        Return the type of the Qiskrypt's Medium.
        """
        return self.medium_type

    def get_length_in_kms(self) -> float:
        """
        Return the length in KMs (Kilometers) of the Qiskrypt's Medium.

        :return self.medium_length_in_kms: the type of the Qiskrypt's Medium.
        """

        """
        Return the length in KMs (Kilometers) of the Qiskrypt's Medium.
        """
        return self.length_in_kms

    def __str__(self) -> str:
        """
        Return the string representation for the Qiskrypt's Medium.

        :return qiskrypt_medium_string_representation: the string representation for the Qiskrypt's Medium.
        """

        qiskrypt_medium_string_representation = "Medium #{}:\n- Name: {}\n- Type: {}\n- Length (in KMs): {}"\
            .format(self.num, self.name, self.medium_type, self.length_in_kms)
        """
        Set the string representation for the Qiskrypt's Medium.
        """

        """
        Return the string representation for the Qiskrypt's Medium.
        """
        return qiskrypt_medium_string_representation
