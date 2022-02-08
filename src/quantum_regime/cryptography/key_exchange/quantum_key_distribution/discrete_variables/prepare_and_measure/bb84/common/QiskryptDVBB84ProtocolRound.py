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

from src.quantum_regime.cryptography.key_exchange.quantum_key_distribution.QiskryptQuantumKeyDistributionRound \
    import QiskryptQuantumKeyDistributionRound
"""
Import the Qiskrypt's Quantum Key Distribution (QKD) Round.
"""

from src.quantum_regime.circuit.QiskryptQuantumCircuit \
    import QiskryptQuantumCircuit
"""
Import the Qiskrypt's Quantum Circuit.
"""


"""
Definition of Constants and Enumerations.
"""

POSSIBLE_DV_BB84_PROTOCOL_ROUND_TYPES = ["Z-BASIS ROUND", "X-BASIS ROUND",
                                         "CLASSICAL POST-PROCESSING ROUND"]
"""
The available DV (Discrete Variables) BB84 Protocol Round types for
the Qiskrypt's DV (Discrete Variables) BB84 Protocol.
"""


class QiskryptDVBB84ProtocolRound(QiskryptQuantumKeyDistributionRound):
    """
    Object class for the Qiskrypt's DV (Discrete Variables) BB84 Protocol Round.
    """

    def __init__(self, quantum_key_exchange_protocol_round_number,
                 quantum_key_exchange_protocol_round_type,
                 quantum_key_exchange_protocol_round_quantum_circuit):
        """
        Constructor of the Qiskrypt's BB84 Protocol Round with Discrete Variables (DVs).

        :param quantum_key_exchange_protocol_round_number: the number of the Qiskrypt's
                                                           Quantum Key Exchange Protocol Round.
        :param quantum_key_exchange_protocol_round_type: the type of the Qiskrypt's
                                                         Quantum Key Exchange Protocol Round.
        :param: quantum_key_exchange_protocol_round_quantum_circuit: the Qiskrypt's Quantum Circuit for
                                                                     the Qiskrypt's Quantum Key Exchange
                                                                     Protocol Round.
        """

        if quantum_key_exchange_protocol_round_type in POSSIBLE_DV_BB84_PROTOCOL_ROUND_TYPES:
            """
            If the given type of the Qiskrypt's Quantum Key Exchange Protocol Round is
            one of the available (and thus, valid) BB84 Protocol Round types for
            the Qiskrypt's BB84 Protocol with Discrete Variables (DVs).
            """

            super().__init__(quantum_key_exchange_protocol_round_number,
                             quantum_key_exchange_protocol_round_type,
                             quantum_key_exchange_protocol_round_quantum_circuit)
            """
            Call of the constructor of the super-class Qiskrypt's Quantum Key Distribution (QKD) Round.
            """

        else:
            """
            If the given type of the Qiskrypt's Quantum Key Exchange Protocol Round is
            not one of the available (and thus, not valid) BB84 Protocol Round types for
            the Qiskrypt's BB84 Protocol with Discrete Variables (DVs).
            """

            # TODO Throw - Exception

    def get_quantum_key_exchange_protocol_round_number(self) -> int:
        """
        Return the number of the Qiskrypt's Quantum Key Distribution (QKD) Round.

        :return super().get_quantum_key_exchange_protocol_round_number(): the number of the Qiskrypt's
                                                                          Quantum Key Distribution Round.
        """

        """
        Return the number of the Qiskrypt's Quantum Key Exchange Protocol Round.
        """
        return super().get_quantum_key_exchange_protocol_round_number()

    def get_quantum_key_exchange_protocol_round_type(self) -> str:
        """
        Return the type of the Qiskrypt's Quantum Key Exchange Protocol Round.

        :return super().get_quantum_key_exchange_protocol_round_type(): the type of the Qiskrypt's
                                                                        Quantum Key Exchange Protocol Round.
        """

        """
        Return the type of the Qiskrypt's Quantum Key Exchange Protocol Round.
        """
        return super().get_quantum_key_exchange_protocol_round_type()

    def get_quantum_key_exchange_protocol_round_quantum_circuit(self) -> QiskryptQuantumCircuit:
        """
        Return the Qiskrypt's Quantum Circuit of the Qiskrypt's Quantum Key Exchange Protocol Round.

        :return super().get_quantum_key_exchange_protocol_round_quantum_circuit(): the Qiskrypt's Quantum Circuit of
                                                                                   the Qiskrypt's Quantum Key Exchange
                                                                                   Protocol Round.
        """

        """
        Return the Qiskrypt's Quantum Circuit of the Qiskrypt's Quantum Key Exchange Protocol Round.
        """
        return super().get_quantum_key_exchange_protocol_round_quantum_circuit()
