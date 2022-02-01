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

POSSIBLE_AGENT_CONTEXTS = ["QUANTUM", "FULLY-QUANTUM", "SEMI-QUANTUM", "CLASSICAL"]
"""
The available Agent contexts for the Qiskrypt's Agent.
"""


class QiskryptAgent:
    """
    Object class for the Qiskrypt's Agent.
    """

    def __init__(self, num: int, name: str, context: str):
        """
        Constructor of the Qiskrypt's Agent.

        :param num: the number of the Qiskrypt's Agent.
        :param name: the name of the Qiskrypt's Agent.
        :param context: the context of the Qiskrypt's Agent.
        """

        self.num = num
        """
        Set the number of the Qiskrypt's Agent.
        """

        self.name = name
        """
        Set the name of the Qiskrypt's Agent.
        """

        self.context = context
        """
        Set the context of the Qiskrypt's Agent.
        """

    def get_num(self) -> int:
        """
        Return the number of the Qiskrypt's Agent.

        :return self.num: the number of the Qiskrypt's Agent.
        """

        """
        Return the number of the Qiskrypt's Agent.
        """
        return self.num

    def get_name(self) -> str:
        """
        Return the name of the Qiskrypt's Agent.

        :return self.name: the name of the Qiskrypt's Agent.
        """

        """
        Return the name of the Qiskrypt's Agent.
        """
        return self.name

    def get_context(self) -> str:
        """
        Return the context of the Qiskrypt's Agent.

        :return self.context: the context of the Qiskrypt's Agent.
        """

        """
        Return the context of the Qiskrypt's Agent.
        """
        return self.context

    def __str__(self) -> str:
        """
        Return the string representation for the Qiskrypt's Agent.

        :return qiskrypt_agent_string_representation: the string representation for the Qiskrypt's Agent.
        """

        qiskrypt_agent_string_representation = "Agent #{}:\n- Name: {}\n- Context: {}"\
            .format(self.num, self.name, self.context)
        """
        Set the string representation for the Qiskrypt's Agent.
        """

        """
        Return the string representation for the Qiskrypt's Agent.
        """
        return qiskrypt_agent_string_representation
