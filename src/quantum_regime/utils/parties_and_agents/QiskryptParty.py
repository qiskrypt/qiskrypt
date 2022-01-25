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


class QiskryptParty:
    """
    Object class for the Qiskrypt's Party.
    """

    def __init__(self, num: int, name: str, context: str):
        """
        Constructor of the Qiskrypt's Party.

        :param num: the number of the Qiskrypt's Party.
        :param name: the name of the Qiskrypt's Party.
        :param context: the context of the Qiskrypt's Party.
        """

        self.num = num
        """
        Set the number of the Qiskrypt's Party.
        """

        self.name = name
        """
        Set the name of the Qiskrypt's Party.
        """

        self.context = context
        """
        Set the context of the Qiskrypt's Party.
        """

    def get_num(self) -> int:
        """
        Return the number of the Qiskrypt's Party.

        :return self.num: the number of the Qiskrypt's Party.
        """

        """
        Return the number of the Qiskrypt's Party.
        """
        return self.num

    def get_name(self) -> str:
        """
        Return the name of the Qiskrypt's Party.

        :return self.name: the name of the Qiskrypt's Party.
        """

        """
        Return the name of the Qiskrypt's Party.
        """
        return self.name

    def get_context(self) -> str:
        """
        Return the context of the Qiskrypt's Party.

        :return self.context: the context of the Qiskrypt's Party.
        """

        """
        Return the context of the Qiskrypt's Party.
        """
        return self.context

    def __str__(self) -> str:
        """
        Return the string representation for the Qiskrypt's Party.

        :return qiskrypt_party_string_representation: the string representation for the Qiskrypt's Party.
        """

        qiskrypt_party_string_representation = "Party #{}:\n- Name: {}\n- Context: {}"\
            .format(self.num, self.name, self.context)
        """
        Set the string representation for the Qiskrypt's Party.
        """

        """
        Return the string representation for the Qiskrypt's Party.
        """
        return qiskrypt_party_string_representation
