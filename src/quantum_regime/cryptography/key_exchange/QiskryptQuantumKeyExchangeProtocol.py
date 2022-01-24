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

from src.quantum_regime.cryptography.QiskryptQuantumCryptographicPrimitive \
    import QiskryptQuantumCryptographicPrimitive
"""
Import the Qiskrypt's Quantum Cryptographic Primitive.
"""

from src.quantum_regime.cryptography.QiskryptQuantumCryptographicPrimitive \
    import POSSIBLE_QUANTUM_CRYPTOGRAPHIC_PRIMITIVE_TYPES
"""
Import the Qiskrypt's Quantum Cryptographic Primitive.
"""


"""
Definition of Constants and Enumerations.
"""

POSSIBLE_QUANTUM_KEY_EXCHANGE_PROTOCOL_TYPES = ["QUANTUM KEY DISTRIBUTION (QKD)",
                                                "SEMI-QUANTUM KEY DISTRIBUTION (SQKD)",
                                                "QUANTUM CONFERENCE KEY AGREEMENT (QCKA)",
                                                "SEMI-QUANTUM CONFERENCE KEY AGREEMENT (SQCKA)"]
"""
The available Quantum Key Exchange Protocol types for
the Qiskrypt's Quantum Key Exchange Protocol.
"""


class QiskryptQuantumKeyExchangeProtocol(QiskryptQuantumCryptographicPrimitive):
    """
    Object class for the Qiskrypt's Quantum Key Exchange Protocol.
    """

    def __init__(self, name: str,
                 quantum_cryptographic_primitive_cardinality: str,
                 quantum_cryptographic_primitive_signal_variable: str,
                 quantum_cryptographic_primitive_scenario: str,
                 quantum_key_exchange_protocol_type: str):
        """
        Constructor of the Qiskrypt's Quantum Cryptographic Primitive.

        :param name: the name of the Qiskrypt's Quantum Cryptographic Primitive.
        :param quantum_cryptographic_primitive_cardinality: the cardinality of the Qiskrypt's
                                                            Quantum Cryptographic Primitive.
        :param quantum_cryptographic_primitive_signal_variable: the signal variable of the Qiskrypt's
                                                                 Quantum Cryptographic Primitive.
        :param quantum_cryptographic_primitive_scenario: the scenario of the Qiskrypt's
                                                         Quantum Cryptographic Primitive.
        :param quantum_key_exchange_protocol_type: the type of the Qiskrypt's
                                                   Quantum Key Exchange Protocol.
        """

        if quantum_key_exchange_protocol_type in \
                POSSIBLE_QUANTUM_KEY_EXCHANGE_PROTOCOL_TYPES:
            """
            If the given type of the Qiskrypt's Quantum Key Exchange Protocol is valid.
            """

            super().__init__(name, quantum_cryptographic_primitive_cardinality,
                             quantum_cryptographic_primitive_signal_variable,
                             quantum_cryptographic_primitive_scenario,
                             POSSIBLE_QUANTUM_CRYPTOGRAPHIC_PRIMITIVE_TYPES[1])
            """
            Call of the constructor of the super-class Qiskrypt's Quantum Entanglement.
            """

        else:
            """
            If the given type of the Qiskrypt's Quantum Key Exchange Protocol is not valid.
            """

            # TODO Throw - Exception

    def start_quantum_transmission_phase(self):
        """
        Start the Quantum Transmission Phase of the
        Qiskrypt's Quantum Key Exchange Protocol.
        """

        """
        Raise a Not Implemented Error since this abstract method
        should be implemented in its sub-classes.
        """
        # TODO - Throw a Not Implemented Error

    def start_classical_post_processing_phase(self):
        """
        Start the Classical Post-Processing Phase of the
        Qiskrypt's Quantum Key Exchange Protocol.
        """

        """
        Raise a Not Implemented Error since this abstract method
        should be implemented in its sub-classes.
        """
        # TODO - Throw a Not Implemented Error
