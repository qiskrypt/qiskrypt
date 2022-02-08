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

from src.quantum_regime.cryptography.key_exchange.quantum_key_distribution.QiskryptQuantumKeyDistribution \
    import QiskryptQuantumKeyDistribution
"""
Import the Qiskrypt's Quantum Key Distribution (QKD).
"""

from src.quantum_regime.cryptography.QiskryptQuantumCryptographicPrimitive \
    import POSSIBLE_QUANTUM_CRYPTOGRAPHIC_PRIMITIVE_SIGNAL_VARIABLE_TYPES
"""
Import the available Quantum Cryptographic Primitive signal variable types for
the Qiskrypt's Quantum Cryptographic Primitives.
"""

from src.quantum_regime.cryptography.QiskryptQuantumCryptographicPrimitive \
    import POSSIBLE_QUANTUM_CRYPTOGRAPHIC_PRIMITIVE_SCENARIOS
"""
Import the available Quantum Cryptographic Primitive scenarios for
the Qiskrypt's Quantum Cryptographic Primitives.
"""

from src.quantum_regime.cryptography.key_exchange.quantum_key_distribution.QiskryptQuantumKeyDistribution \
    import POSSIBLE_QUANTUM_KEY_DISTRIBUTION_TYPES
"""
Import the available Quantum Key Distribution (QKD) types for
the Qiskrypt's Quantum Key Distribution (QKD).
"""

"""
Definition of Constants and Enumerations.
"""

DV_BB84_PROTOCOL_NAME = "DV (DISCRETE VARIABLES) BB84 PROTOCOL"
"""
The name of the DV (Discrete Variables) BB84 Protocol.
"""

DV_BB84_PROTOCOL_NUM_ROUNDS_FOR_QUANTUM_TRANSMISSION = 1024
"""
The default number of rounds for the Quantum Transmission of
the Qiskrypt's DV (Discrete Variable) BB84 Protocol.
"""


class QiskryptDVBB84Protocol(QiskryptQuantumKeyDistribution):
    """
    Object class for the Qiskrypt's DV (Discrete Variables) BB84 Protocol.

    Reference(s):
    1) Quantum cryptography: Public key distribution and coin tossing:
       - Authors: Charles Bennet and Gilles Brassard
       - Year: 1984
       - Link:https://arxiv.org/abs/2003.06557v1
    """

    def __init__(self, quantum_cryptographic_primitive_scenario: str,
                 quantum_key_exchange_protocol_num_rounds_for_quantum_transmission=DV_BB84_PROTOCOL_NUM_ROUNDS_FOR_QUANTUM_TRANSMISSION):
        """
        Constructor of the Qiskrypt's DV (Discrete Variables) BB84 Protocol.

        :param quantum_cryptographic_primitive_scenario: the scenario of the Qiskrypt's
                                                         Quantum Cryptographic Primitive.
        :param quantum_key_exchange_protocol_num_rounds_for_quantum_transmission: the number of rounds for
                                                                                  the Quantum Transmission in
                                                                                  the Qiskrypt's Quantum Key
                                                                                  Exchange Protocol.
        """

        quantum_cryptographic_primitive_properties = list()
        """
        Create an empty list of properties of the Qiskrypt's
        Quantum Cryptographic Primitive.
        """

        if quantum_cryptographic_primitive_scenario in \
                POSSIBLE_QUANTUM_CRYPTOGRAPHIC_PRIMITIVE_SCENARIOS:
            """
            If the scenario of the Qiskrypt's Quantum Cryptographic Primitive is valid.
            """

            super().__init__(DV_BB84_PROTOCOL_NAME,
                             POSSIBLE_QUANTUM_CRYPTOGRAPHIC_PRIMITIVE_SIGNAL_VARIABLE_TYPES[0],
                             quantum_cryptographic_primitive_properties,
                             quantum_cryptographic_primitive_scenario,
                             quantum_key_exchange_protocol_num_rounds_for_quantum_transmission,
                             POSSIBLE_QUANTUM_KEY_DISTRIBUTION_TYPES[0])
            """
            Call of the constructor of the super-class Qiskrypt's Quantum Key Distribution (QKD).
            """

        else:
            """
            If the scenario of the Qiskrypt's Quantum Cryptographic Primitive is not valid.
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

        :return super().get_quantum_cryptographic_primitive_signal_variable_type(): the signal variable type of the
                                                                                    Qiskrypt's Quantum Cryptographic
                                                                                    Primitive.
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
        return super().get_quantum_key_exchange_protocol_type()

    def get_quantum_key_exchange_protocol_num_rounds_for_quantum_transmission(self) -> int:
        """
        Return the number of rounds for the Quantum Transmission in
        the Qiskrypt's Quantum Key Exchange Protocol.

        :return super().get_quantum_key_exchange_protocol_num_rounds_for_quantum_transmission():
                the number of rounds for the Quantum Transmission in
                the Qiskrypt's Quantum Key Exchange Protocol.
        """

        """
        Return the number of rounds for the Quantum Transmission in
        the Qiskrypt's Quantum Key Exchange Protocol.
        """
        return super().get_quantum_key_exchange_protocol_num_rounds_for_quantum_transmission()

    def is_configured(self) -> bool:
        """
        Return the boolean flag to determine if the Qiskrypt's Key Exchange Protocol
        is configured.

        :return self.configured: the boolean flag to determine if the Qiskrypt's Key Exchange Protocol
                                 is configured.
        """

        """
        Return the boolean flag to determine if the Qiskrypt's Key Exchange Protocol
        is configured.
        """
        return super().is_configured()

    def set_as_configured(self):
        """
        Set the boolean flag to determine if the Qiskrypt's Key Exchange Protocol
        is configured, as True, if it is not yet defined as True.
        """

        if not super().is_configured():
            """
            If the boolean flag to determine if the Qiskrypt's Key Exchange Protocol
            is configured, as False.
            """

            super().set_as_configured()
            """
            Set the boolean flag to determine if the Qiskrypt's Key Exchange Protocol
            is configured, as True.
            """

        else:
            """
            If the boolean flag to determine if the Qiskrypt's Key Exchange Protocol
            is configured, as True.
            """

            # TODO Throw - Exception

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
