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

from src.quantum_regime.cryptography.QiskryptQuantumCryptographicPrimitive \
    import POSSIBLE_QUANTUM_CRYPTOGRAPHIC_PRIMITIVE_CONTEXTS
"""
Import the available Quantum Cryptographic Primitive contexts for
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
                 quantum_cryptographic_primitive_signal_variable_type: str,
                 quantum_cryptographic_primitive_properties: list,
                 quantum_cryptographic_primitive_scenario: str,
                 quantum_key_distribution_type: str):
        """
        Constructor of the Qiskrypt's Quantum Key Distribution (QKD).

        :param name: the name of the Qiskrypt's Quantum Key Distribution (QKD).
        :param quantum_cryptographic_primitive_signal_variable_type: the signal variable of the Qiskrypt's
                                                                     Quantum Cryptographic Primitive.
        :param quantum_cryptographic_primitive_properties: the list of properties of the Qiskrypt's
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
                             quantum_cryptographic_primitive_signal_variable_type,
                             POSSIBLE_QUANTUM_CRYPTOGRAPHIC_PRIMITIVE_CONTEXTS[0],
                             quantum_cryptographic_primitive_properties,
                             quantum_cryptographic_primitive_scenario,
                             POSSIBLE_QUANTUM_KEY_EXCHANGE_PROTOCOL_TYPES[0])
            """
            Call of the constructor of the super-class Qiskrypt's Quantum Key Exchange Protocol.
            """

            self.quantum_key_distribution_type = quantum_key_distribution_type
            """
            Set the type of the Qiskrypt's Quantum Key Distribution (QKD).
            """

        else:
            """
            If the given type of the Qiskrypt's Quantum Key Distribution (QKD) is not valid.
            """

            # TODO Throw - Exception

    def get_name(self) -> str:
        """
        Return the name of the Qiskrypt's Quantum Cryptographic Primitive.

        :return super().get_name(): the name of the Qiskrypt's
                                    Quantum Cryptographic Primitive.
        """

        """
        Return the name of the Qiskrypt's Quantum Cryptographic Primitive.
        """
        return super().get_name()

    def get_quantum_cryptographic_primitive_cardinality(self) -> str:
        """
        Return the cardinality of the Qiskrypt's Quantum Cryptographic Primitive.

        :return super().get_quantum_cryptographic_primitive_cardinality(): the cardinality of the Qiskrypt's
                                                                           Quantum Cryptographic Primitive.
        """

        """
        Return the cardinality of the Qiskrypt's Quantum Cryptographic Primitive.
        """
        return super().get_quantum_cryptographic_primitive_cardinality()

    def get_quantum_cryptographic_primitive_signal_variable_type(self) -> str:
        """
        Return the signal variable type of the Qiskrypt's Quantum Cryptographic Primitive.

        :return super().get_quantum_cryptographic_primitive_signal_variable_type(): the signal variable type of the Qiskrypt's
                                                                                    Quantum Cryptographic Primitive.
        """

        """
        Return the signal variable type of the Qiskrypt's Quantum Cryptographic Primitive.
        """
        return super().get_quantum_cryptographic_primitive_signal_variable_type()

    def get_quantum_cryptographic_primitive_context(self) -> str:
        """
        Return the context of the Qiskrypt's Quantum Cryptographic Primitive.

        :return super().get_quantum_cryptographic_primitive_context(): the context of the Qiskrypt's
                                                                       Quantum Cryptographic Primitive.
        """

        """
        Return the context of the Qiskrypt's Quantum Cryptographic Primitive.
        """
        return super().get_quantum_cryptographic_primitive_context()

    def get_quantum_cryptographic_primitive_properties(self) -> list:
        """
        Return the list of properties of the Qiskrypt's Quantum Cryptographic Primitive.

        :return super().get_quantum_cryptographic_primitive_properties(): the list of properties of the Qiskrypt's
                                                                          Quantum Cryptographic Primitive.
        """

        """
        Return the list of properties of the Qiskrypt's Quantum Cryptographic Primitive.
        """
        return super().get_quantum_cryptographic_primitive_properties()

    def get_quantum_cryptographic_primitive_scenario(self) -> str:
        """
        Return the scenario of the Qiskrypt's Quantum Cryptographic Primitive.

        :return super().get_quantum_cryptographic_primitive_scenario(): the scenario of the Qiskrypt's
                                                                        Quantum Cryptographic Primitive.
        """

        """
        Return the scenario of the Qiskrypt's Quantum Cryptographic Primitive.
        """
        return super().get_quantum_cryptographic_primitive_scenario()

    def get_quantum_cryptographic_primitive_type(self) -> str:
        """
        Return the type of the Qiskrypt's Quantum Cryptographic Primitive.

        :return super().get_quantum_cryptographic_primitive_type(): the type of the Qiskrypt's
                                                                    Quantum Cryptographic Primitive.
        """

        """
        Return the type of the Qiskrypt's Quantum Cryptographic Primitive.
        """
        return super().get_quantum_cryptographic_primitive_type()

    def get_quantum_key_exchange_protocol_type(self) -> str:
        """
        Return the type of the Qiskrypt's Quantum Key Exchange Protocol.

        :return self.quantum_key_exchange_protocol_type: the type of the Qiskrypt's
                                                         Quantum Key Exchange Protocol.
        """

        """
        Return the type of the Qiskrypt's Quantum Key Exchange Protocol.
        """
        return self.quantum_key_exchange_protocol_type

    def get_quantum_key_distribution_type(self) -> str:
        """
        Return the type of the Qiskrypt's Quantum Key Distribution (QKD).

        :return self.quantum_key_distribution_type: the type of the Qiskrypt's
                                                    Quantum Key Distribution (QKD).
        """

        """
        Return the type of the Qiskrypt's Quantum Key Distribution (QKD).
        """
        return self.quantum_key_distribution_type

    def start_quantum_transmission_phase(self):
        """
        Start the Quantum Transmission Phase of the
        Qiskrypt's Quantum Key Exchange Protocol.
        """

        self.prepare_quantum_states()
        """
        Prepare the Quantum States for the Quantum Transmission Phase of
        the Quantum Key Distribution (QKD).
        """

        self.transmit_quantum_states()
        """
        Transmit the Quantum States for the Quantum Transmission Phase of
        the Quantum Key Distribution (QKD).
        """

        self.measure_quantum_states()
        """
        Measure the Quantum States for the Quantum Transmission Phase of
        the Quantum Key Distribution (QKD).
        """

    def start_classical_post_processing_phase(self):
        """
        Start the Classical Post-Processing Phase of the
        Qiskrypt's Quantum Key Exchange Protocol.
        """

        self.sift_raw_key()
        """
        Sift the Raw Key for the Classical Post-Processing Phase of
        the Quantum Key Distribution (QKD).
        """

        self.estimate_parameters()
        """
        Estimate the Parameters for the Classical Post-Processing Phase of
        the Quantum Key Distribution (QKD).
        """

        self.reconcile_information()
        """
        Reconcile the Information for the Classical Post-Processing Phase of
        the Quantum Key Distribution (QKD).
        """

        self.amplify_privacy()
        """
        Amplify the Privacy for the Classical Post-Processing Phase of
        the Quantum Key Distribution (QKD).
        """

    def prepare_quantum_states(self):
        """
        Prepare the Quantum States for the
        Qiskrypt's Quantum Key Distribution (QKD).
        """

        """
        Raise a Not Implemented Error since this abstract method
        should be implemented in its sub-classes.
        """
        # TODO Throw - Exception

    def transmit_quantum_states(self):
        """
        Transmit the Quantum States for the
        Qiskrypt's Quantum Key Distribution (QKD).
        """

        """
        Raise a Not Implemented Error since this abstract method
        should be implemented in its sub-classes.
        """
        # TODO Throw - Exception

    def measure_quantum_states(self):
        """
        Measure the Quantum States for the
        Qiskrypt's Quantum Key Distribution (QKD).
        """

        """
        Raise a Not Implemented Error since this abstract method
        should be implemented in its sub-classes.
        """
        # TODO Throw - Exception

    def sift_raw_key(self):
        """
        Sift the Secret Key for the
        Qiskrypt's Quantum Key Distribution (QKD).
        """

        """
        Raise a Not Implemented Error since this abstract method
        should be implemented in its sub-classes.
        """
        # TODO Throw - Exception

    def estimate_parameters(self):
        """
        Estimate the Parameters for the
        Qiskrypt's Quantum Key Distribution (QKD).
        """

        """
        Raise a Not Implemented Error since this abstract method
        should be implemented in its sub-classes.
        """
        # TODO Throw - Exception

    def reconcile_information(self):
        """
        Reconcile the Information for the
        Qiskrypt's Quantum Key Distribution (QKD).
        """

        """
        Raise a Not Implemented Error since this abstract method
        should be implemented in its sub-classes.
        """
        # TODO Throw - Exception

    def amplify_privacy(self):
        """
        Amplify the Privacy for the
        Qiskrypt's Quantum Key Distribution (QKD).
        """

        """
        Raise a Not Implemented Error since this abstract method
        should be implemented in its sub-classes.
        """
        # TODO Throw - Exception
