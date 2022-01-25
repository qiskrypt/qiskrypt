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

from src.quantum_regime.utils.parties_and_agents.QiskryptParty \
    import QiskryptParty
"""
Import the Qiskrypt's Party.
"""

from src.quantum_regime.utils.parties_and_agents.QiskryptParty \
    import POSSIBLE_PARTY_CONTEXTS
"""
Import the available Party contexts for the Qiskrypt's Parties.
"""


class QiskryptSemiQuantumParty(QiskryptParty):
    """
    Object class for the Qiskrypt's Semi-Quantum Party.
    """

    def __init__(self, semi_quantum_party_num: int, semi_quantum_party_name: str):
        """
        Constructor of the Qiskrypt's Semi-Quantum Party.

        :param semi_quantum_party_num: the number of the Qiskrypt's Semi-Quantum Party.
        :param semi_quantum_party_name: the name of the Qiskrypt's Semi-Quantum Party.
        """

        super().__init__(semi_quantum_party_num, semi_quantum_party_name,
                         POSSIBLE_PARTY_CONTEXTS[2])
        """
        Call of the constructor of the super-class Qiskrypt's Party.
        """

    def get_num(self) -> int:
        """
        Return the number of the Qiskrypt's Party.

        :return super().get_num(): the number of the Qiskrypt's Party.
        """

        """
        Return the number of the Qiskrypt's Party.
        """
        return super().get_num()

    def get_name(self) -> str:
        """
        Return the name of the Qiskrypt's Party.

        :return super().get_name(): the name of the Qiskrypt's Party.
        """

        """
        Return the name of the Qiskrypt's Party.
        """
        return super().get_name()

    def get_context(self) -> str:
        """
        Return the context of the Qiskrypt's Party.

        :return super().get_context(): the context of the Qiskrypt's Party.
        """

        """
        Return the context of the Qiskrypt's Party.
        """
        return super().get_context()

    def __str__(self) -> str:
        """
        Return the string representation for the Qiskrypt's Party.

        :return super().__str__(): the string representation for the Qiskrypt's Party.
        """

        """
        Return the string representation for the Qiskrypt's Party.
        """
        return super().__str__()
