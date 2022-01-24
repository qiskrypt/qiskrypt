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

from src.quantum_regime.cryptography.key_exchange.QiskryptQuantumKeyExchangeProtocol \
    import QiskryptQuantumKeyExchangeProtocol
"""
Import the Qiskrypt's Quantum Key Exchange Protocol.
"""

from src.quantum_regime.cryptography.QiskryptQuantumCryptographicPrimitive \
    import POSSIBLE_QUANTUM_CRYPTOGRAPHIC_PRIMITIVE_CARDINALITIES
"""
Import the available Quantum Cryptographic Primitive cardinalities for
the Qiskrypt's Quantum Cryptographic Primitives.
"""

from src.quantum_regime.cryptography.key_exchange.QiskryptQuantumKeyExchangeProtocol \
    import POSSIBLE_QUANTUM_KEY_EXCHANGE_PROTOCOL_TYPES
"""
Import the available Quantum Key Exchange Protocol types for
the Qiskrypt's Quantum Key Exchange Protocols.
"""


"""
Definition of Constants and Enumerations.
"""

POSSIBLE_QUANTUM_KEY_DISTRIBUTION_TYPES = ["PREPARE-AND-MEASURE (PM)",
                                           "ENTANGLEMENT-BASED (EB)"]
"""
The available Quantum Key Exchange Protocol types for
the Qiskrypt's Quantum Key Exchange Protocol.
"""


class QiskryptQuantumKeyDistribution(QiskryptQuantumKeyExchangeProtocol):
    """
    Object class for the Qiskrypt's Quantum Key Distribution (QKD).
    """

    def __init__(self, name: str,
                 quantum_cryptographic_primitive_signal_variable: str,
                 quantum_cryptographic_primitive_scenario: str,
                 quantum_key_distribution_type: str):
        """
        Constructor of the Qiskrypt's Quantum Key Distribution (QKD).

        :param name: the name of the Qiskrypt's Quantum Key Distribution (QKD).
        :param quantum_cryptographic_primitive_signal_variable: the signal variable of the Qiskrypt's
                                                                Quantum Cryptographic Primitive.
        :param quantum_cryptographic_primitive_scenario: the scenario of the Qiskrypt's
                                                         Quantum Cryptographic Primitive.
        :param quantum_key_distribution_type: the type of the Qiskrypt's Quantum Key Distribution (QKD).
        """

        if quantum_key_distribution_type in \
                POSSIBLE_QUANTUM_KEY_DISTRIBUTION_TYPES:
            """
            If the given type of the Qiskrypt's Quantum Key Distribution (QKD) is valid.
            """

            super().__init__(name, POSSIBLE_QUANTUM_CRYPTOGRAPHIC_PRIMITIVE_CARDINALITIES[0],
                             quantum_cryptographic_primitive_signal_variable,
                             quantum_cryptographic_primitive_scenario,
                             POSSIBLE_QUANTUM_KEY_EXCHANGE_PROTOCOL_TYPES[0])
            """
            Call of the constructor of the super-class Qiskrypt's Quantum Key Exchange Protocol.
            """

        else:
            """
            If the given type of the Qiskrypt's Quantum Key Distribution (QKD) is not valid.
            """

            # TODO Throw - Exception
